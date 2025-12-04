# Simpler approach: Update all atom definitions (298 rows)
import json
import subprocess
import re
import sys

sys.path.insert(0, r'e:\astron-rpa\docker\volumes\mysql')
from translate_all_atoms_v2 import translate_text

# Read the original SQL file
print("Reading original SQL file...")
orig = open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

# Find each row by id pattern and extract
# Pattern: (id,'parent','key','json_content',...
# We'll find each row start and parse from there

rows_data = []

# Find all row starts
row_starts = [(m.start(), int(m.group(1))) for m in re.finditer(r'\n\((\d+),\'', orig)]
print(f"Found {len(row_starts)} rows")

for idx, (start_pos, row_id) in enumerate(row_starts):
    # Get the end position (next row start or end of file)
    if idx + 1 < len(row_starts):
        end_pos = row_starts[idx + 1][0]
    else:
        end_pos = len(orig)
    
    row_content = orig[start_pos+1:end_pos]  # Skip the newline
    
    # Parse the row: (id,'parent_key','atom_key','json_content',rest...)
    # Find the third quoted field (json_content)
    quote_count = 0
    pos = 0
    json_start = None
    json_end = None
    
    while pos < len(row_content):
        if row_content[pos] == "'":
            # Check if it's escaped
            if pos > 0 and row_content[pos-1] == '\\':
                pos += 1
                continue
            
            quote_count += 1
            if quote_count == 5:  # Start of 3rd field (json)
                json_start = pos + 1
            elif quote_count == 6:  # End of 3rd field (json)
                # But we need to handle escaped quotes
                # The real end is when we see ',[0-9] after the json
                pass
            pos += 1
        else:
            pos += 1
    
    # Simpler approach: find the json between 3rd pair of quotes
    # Find 'atom_key',' - the json starts after the second comma
    # Pattern: (id,'parent_key','atom_key','{...}'
    
    # Find the position after 'atom_key','
    key_pattern = re.match(r"\((\d+),'([^']*)','([^']*)','\{", row_content)
    if not key_pattern:
        # Try handling escaped quotes in atom_key
        key_pattern = re.match(r"\((\d+),'([^'\\]*(?:\\.[^'\\]*)*)','([^'\\]*(?:\\.[^'\\]*)*)','\{", row_content)
    
    if key_pattern:
        json_start = key_pattern.end() - 2  # -2 to include the opening '{
        
        # Find the end of json - look for pattern }',number,
        # The json ends with }' followed by ,deleted,creator_id
        # Find }',0, or }',1, (deleted field)
        json_end_match = re.search(r"\}',([01]),", row_content[json_start:])
        if json_end_match:
            json_end = json_start + json_end_match.start() + 1  # +1 to include }
            json_raw = row_content[json_start:json_end]
            
            rows_data.append({
                'id': row_id,
                'atom_key': key_pattern.group(3),
                'json_raw': json_raw
            })
        else:
            print(f"  Row {row_id}: Could not find json end")
    else:
        print(f"  Row {row_id}: Could not parse row start")

print(f"Successfully parsed {len(rows_data)} rows")

# Process each row
updates_sql = []
success_count = 0
error_count = 0

for i, row_data in enumerate(rows_data):
    row_id = row_data['id']
    atom_key = row_data['atom_key']
    json_content_raw = row_data['json_raw']
    
    # Remove leading quote if present (parsing artifact)
    if json_content_raw.startswith("'"):
        json_content_raw = json_content_raw[1:]
    
    # Unescape SQL escaping to get raw JSON
    json_content = json_content_raw.replace("\\'", "'")
    json_content = json_content.replace('\\"', '"')
    json_content = json_content.replace('\\\\', '\\')
    
    # Verify original is valid JSON
    try:
        parsed = json.loads(json_content)
    except json.JSONDecodeError as e:
        print(f"  Row {row_id} ({atom_key}): Original JSON invalid - {e}")
        # Show context
        print(f"    First 100 chars: {json_content[:100]}")
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

if success_count > 0:
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
    
    print(f"Return code: {result.returncode}")
    if result.stderr and 'Warning' not in result.stderr:
        print(f"Stderr: {result.stderr[:500]}")
    
    if result.returncode == 0:
        # Verify
        verify_result = subprocess.run([
            'docker', 'exec', 'rpa-opensource-mysql',
            'mysql', '--default-character-set=utf8mb4', '-uroot', '-prpa123456', 'rpa',
            '-e', "SELECT COUNT(*) as total, SUM(JSON_VALID(atom_content)) as valid_json FROM c_atom_meta;"
        ], capture_output=True, text=True)
        print(f"Row counts: {verify_result.stdout}")
        
        print("\n✅ All atoms translated successfully!")
    else:
        print("\n❌ Update failed!")
