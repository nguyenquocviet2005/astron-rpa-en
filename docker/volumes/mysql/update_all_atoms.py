# Update all atom definitions (298 rows) via Python MySQL UPDATE statements
import json
import subprocess
import re
import sys

sys.path.insert(0, r'e:\astron-rpa\docker\volumes\mysql')
from translate_all_atoms_v2 import translate_text

# Read the original SQL file
print("Reading original SQL file...")
orig = open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

# Parse all rows from the INSERT statement
# Format: INSERT INTO `c_atom_meta` VALUES (id,'parent_key','atom_key','json_content',deleted,creator_id,'create_time',updater_id,'update_time','version',sort,'version_num')
# The SQL uses \' for escaping quotes within strings

# First, let's split by each row - rows are separated by ),\n(
# Get just the VALUES part
values_start = orig.find("VALUES\n")
if values_start == -1:
    values_start = orig.find("VALUES\r\n")
values_content = orig[values_start + 7:]  # Skip "VALUES\n"

# Remove the trailing );
if values_content.rstrip().endswith(');'):
    values_content = values_content.rstrip()[:-2]

# Each row is separated by ),\n( - but we need to be careful with escaped content
# Let's parse manually
rows_data = []
current_pos = 0
row_num = 0

while current_pos < len(values_content):
    # Skip leading whitespace and (
    while current_pos < len(values_content) and values_content[current_pos] in ' \r\n\t(':
        current_pos += 1
    if current_pos >= len(values_content):
        break
    
    # Parse id (number)
    id_start = current_pos
    while values_content[current_pos].isdigit():
        current_pos += 1
    row_id = int(values_content[id_start:current_pos])
    
    # Skip comma and quote
    while values_content[current_pos] in ", '":
        current_pos += 1
    current_pos -= 1  # Back to the quote
    
    # Parse parent_key (string)
    if values_content[current_pos] != "'":
        print(f"Expected ' at pos {current_pos}, got {values_content[current_pos]}")
        break
    current_pos += 1
    parent_key_start = current_pos
    while True:
        if values_content[current_pos] == "\\" and values_content[current_pos+1] == "'":
            current_pos += 2
        elif values_content[current_pos] == "'":
            break
        else:
            current_pos += 1
    parent_key = values_content[parent_key_start:current_pos].replace("\\'", "'")
    current_pos += 1  # Skip closing '
    
    # Skip comma
    while values_content[current_pos] in ", ":
        current_pos += 1
    
    # Parse atom_key (string)
    if values_content[current_pos] != "'":
        print(f"Expected ' for atom_key at pos {current_pos}")
        break
    current_pos += 1
    atom_key_start = current_pos
    while True:
        if values_content[current_pos] == "\\" and current_pos + 1 < len(values_content) and values_content[current_pos+1] == "'":
            current_pos += 2
        elif values_content[current_pos] == "'":
            break
        else:
            current_pos += 1
    atom_key = values_content[atom_key_start:current_pos].replace("\\'", "'")
    current_pos += 1  # Skip closing '
    
    # Skip comma
    while values_content[current_pos] in ", ":
        current_pos += 1
    
    # Parse json_content (string) - this is the big one
    if values_content[current_pos] != "'":
        print(f"Expected ' for json at pos {current_pos}")
        break
    current_pos += 1
    json_start = current_pos
    while True:
        if values_content[current_pos] == "\\" and current_pos + 1 < len(values_content):
            current_pos += 2  # Skip escaped char
        elif values_content[current_pos] == "'":
            # Check if this is the end or an escaped '
            if current_pos + 1 < len(values_content) and values_content[current_pos+1] == "'":
                current_pos += 2  # SQL-style escaped '
            else:
                break
        else:
            current_pos += 1
    json_content_raw = values_content[json_start:current_pos]
    current_pos += 1  # Skip closing '
    
    # Add to rows
    rows_data.append({
        'id': row_id,
        'parent_key': parent_key,
        'atom_key': atom_key,
        'json_raw': json_content_raw
    })
    
    # Skip to next row - find ),\n(
    next_row = values_content.find('),(', current_pos)
    if next_row == -1:
        break
    current_pos = next_row + 2  # Skip ),
    row_num += 1

print(f"Parsed {len(rows_data)} rows from original SQL")

# Process each row
updates_sql = []
success_count = 0
error_count = 0

for i, row_data in enumerate(rows_data):
    row_id = row_data['id']
    atom_key = row_data['atom_key']
    json_content_raw = row_data['json_raw']
    
    # Unescape SQL escaping to get raw JSON
    json_content = json_content_raw.replace("\\'", "'")
    json_content = json_content.replace('\\"', '"')
    json_content = json_content.replace('\\\\', '\\')
    json_content = json_content.replace("''", "'")  # SQL escaping for '
    
    # Verify original is valid JSON
    try:
        parsed = json.loads(json_content)
    except json.JSONDecodeError as e:
        print(f"  Row {row_id} ({atom_key}): Original JSON invalid - {e}")
        error_count += 1
        continue
    
    # Translate
    json_translated = translate_text(json_content)
    
    # Replace curly quotes with single quotes (for template "Hello")
    json_translated = json_translated.replace('\u201c', "'")
    json_translated = json_translated.replace('\u201d', "'")
    
    # Verify translated is valid JSON
    try:
        parsed = json.loads(json_translated)
    except json.JSONDecodeError as e:
        print(f"  Row {row_id} ({atom_key}): Translated JSON invalid - {e}")
        error_count += 1
        continue
    
    # Escape for MySQL UPDATE
    json_for_mysql = json_translated.replace('\\', '\\\\').replace("'", "''")
    
    # Create UPDATE statement
    update_sql = f"UPDATE c_atom_meta SET atom_content = '{json_for_mysql}' WHERE id = {row_id};"
    updates_sql.append(update_sql)
    success_count += 1
    
    if (i + 1) % 50 == 0:
        print(f"  Processed {i + 1}/{len(rows_data)} rows...")

print(f"\nGenerated {success_count} UPDATE statements ({error_count} errors)")

# Write all updates to a file
all_updates = '\n'.join(updates_sql)
with open(r'e:\astron-rpa\docker\volumes\mysql\all_updates.sql', 'w', encoding='utf-8') as f:
    f.write(all_updates)
print(f"Saved all_updates.sql ({len(all_updates)} bytes)")

# Copy to container and execute
print("Copying to container...")
subprocess.run([
    'docker', 'cp', 
    r'e:\astron-rpa\docker\volumes\mysql\all_updates.sql',
    'rpa-opensource-mysql:/tmp/all_updates.sql'
], check=True)

print("Executing updates...")
result = subprocess.run([
    'docker', 'exec', 'rpa-opensource-mysql',
    'bash', '-c', 'mysql --default-character-set=utf8mb4 -uroot -prpa123456 rpa < /tmp/all_updates.sql'
], capture_output=True, text=True)

print(f"Result stdout: {result.stdout}")
print(f"Result stderr: {result.stderr[:500] if len(result.stderr) > 500 else result.stderr}")
print(f"Return code: {result.returncode}")

if result.returncode == 0:
    # Verify a few rows
    verify_result = subprocess.run([
        'docker', 'exec', 'rpa-opensource-mysql',
        'mysql', '--default-character-set=utf8mb4', '-uroot', '-prpa123456', 'rpa',
        '-e', "SELECT id, atom_key, JSON_VALID(atom_content) as valid FROM c_atom_meta WHERE JSON_VALID(atom_content) = 0 LIMIT 10;"
    ], capture_output=True, text=True)
    print(f"\nInvalid JSON rows (should be empty): {verify_result.stdout}")
    
    # Count rows
    count_result = subprocess.run([
        'docker', 'exec', 'rpa-opensource-mysql',
        'mysql', '--default-character-set=utf8mb4', '-uroot', '-prpa123456', 'rpa',
        '-e', "SELECT COUNT(*) as total, SUM(JSON_VALID(atom_content)) as valid_json FROM c_atom_meta;"
    ], capture_output=True, text=True)
    print(f"Row counts: {count_result.stdout}")
    
    print("\n✅ All atoms translated successfully!")
else:
    print("\n❌ Update failed!")
