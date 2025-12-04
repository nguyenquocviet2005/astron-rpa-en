# Direct database update using Python MySQL connector
import json

# Read the original atomCommon row from the original SQL file
orig = open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

# Find atomCommon's JSON content
start = orig.find("(14,'root','atomCommon','")
start_json = start + len("(14,'root','atomCommon','")
# Find end - next row starts with (15,
end_row = orig.find("\n(15,'", start)
# Go backwards from end_row to find the closing of the JSON
# Format: ...json...'},deleted,creator_id,'timestamp',updater_id,'timestamp','version',sort,'version_num')
# Find the last '}' before the comma sequence
row_content = orig[start:end_row]
# The JSON ends with }' - find the last occurrence
last_json_end = row_content.rfind("}'")
json_content = orig[start_json:start + last_json_end + 1]

print(f"Extracted JSON: {len(json_content)} bytes")
print(f"First 100 chars: {json_content[:100]}")
print(f"Last 100 chars: {json_content[-100:]}")

# Unescape SQL escaping to get raw JSON
# SQL uses \' for ' and \" for "
json_content = json_content.replace("\\'", "'")
json_content = json_content.replace('\\"', '"')
json_content = json_content.replace('\\\\', '\\')

# Verify it's valid JSON before translation
try:
    parsed = json.loads(json_content)
    print("Original JSON is valid!")
except json.JSONDecodeError as e:
    print(f"Original JSON error: {e}")
    print(f"Context: {json_content[max(0,e.pos-50):e.pos+50]}")
    exit(1)

# Now translate
import sys
sys.path.insert(0, r'e:\astron-rpa\docker\volumes\mysql')
from translate_all_atoms_v2 import translate_text

json_translated = translate_text(json_content)

# Replace curly quotes with single quotes (for the template "Hello")
json_translated = json_translated.replace('\u201c', "'")
json_translated = json_translated.replace('\u201d', "'")

# Verify translated JSON is valid
try:
    parsed = json.loads(json_translated)
    print("Translated JSON is valid!")
except json.JSONDecodeError as e:
    print(f"Translated JSON error: {e}")
    print(f"Context: {json_translated[max(0,e.pos-50):e.pos+50]}")
    exit(1)

# Save the translated JSON for reference
with open(r'e:\astron-rpa\docker\volumes\mysql\atomcommon_translated.json', 'w', encoding='utf-8') as f:
    f.write(json_translated)
print(f"Saved atomcommon_translated.json")

# Now use Docker exec to update the database
import subprocess
import shlex

# Escape the JSON for MySQL
# We need to escape backslashes and single quotes for the MySQL string
# Also need to escape for shell
json_for_mysql = json_translated.replace('\\', '\\\\').replace("'", "\\'")

# Write to a temporary file inside the container
with open(r'e:\astron-rpa\docker\volumes\mysql\atomcommon_for_update.json', 'w', encoding='utf-8') as f:
    f.write(json_translated)

# Copy to container
subprocess.run([
    'docker', 'cp', 
    r'e:\astron-rpa\docker\volumes\mysql\atomcommon_for_update.json',
    'rpa-opensource-mysql:/tmp/atomcommon.json'
], check=True)
print("Copied JSON to container")

# Use MySQL's LOAD_FILE or just UPDATE with file content
# Actually, let's use a Python approach inside the container
update_script = '''
import json
import mysql.connector

# Read the JSON
with open('/tmp/atomcommon.json', 'r', encoding='utf-8') as f:
    json_content = f.read()

# Connect and update
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rpa123456',
    database='rpa',
    charset='utf8mb4'
)
cursor = conn.cursor()
cursor.execute("UPDATE c_atom_meta SET atom_content = %s WHERE id = 14", (json_content,))
conn.commit()
print(f"Updated! Rows affected: {cursor.rowcount}")
cursor.execute("SELECT JSON_VALID(atom_content), JSON_DEPTH(atom_content) FROM c_atom_meta WHERE id = 14")
row = cursor.fetchone()
print(f"JSON_VALID={row[0]}, JSON_DEPTH={row[1]}")
cursor.close()
conn.close()
'''

# Wait, the container might not have Python with mysql connector. Let's use a different approach.
# Use mysql with a file that contains just the UPDATE statement

# Create an UPDATE statement using the JSON file
# MySQL can use LOAD_FILE to read from filesystem

# First check if secure_file_priv allows /tmp
result = subprocess.run([
    'docker', 'exec', 'rpa-opensource-mysql',
    'mysql', '--default-character-set=utf8mb4', '-uroot', '-prpa123456', 'rpa',
    '-e', "SHOW VARIABLES LIKE 'secure_file_priv';"
], capture_output=True, text=True)
print(f"secure_file_priv: {result.stdout}")

# Alternative: pipe the UPDATE directly via stdin
# Build the UPDATE SQL with proper escaping
# For MySQL, we need to escape ' as '' and \ as \\
json_escaped = json_translated.replace('\\', '\\\\').replace("'", "''")

# Create a small SQL file with just the UPDATE
update_sql = f"UPDATE c_atom_meta SET atom_content = '{json_escaped}' WHERE id = 14;"
with open(r'e:\astron-rpa\docker\volumes\mysql\update_atomcommon.sql', 'w', encoding='utf-8') as f:
    f.write(update_sql)
print(f"Created update_atomcommon.sql ({len(update_sql)} bytes)")

# Copy to container
subprocess.run([
    'docker', 'cp', 
    r'e:\astron-rpa\docker\volumes\mysql\update_atomcommon.sql',
    'rpa-opensource-mysql:/tmp/update_atomcommon.sql'
], check=True)

# Run the update
result = subprocess.run([
    'docker', 'exec', 'rpa-opensource-mysql',
    'bash', '-c', 'mysql --default-character-set=utf8mb4 -uroot -prpa123456 rpa < /tmp/update_atomcommon.sql'
], capture_output=True, text=True)
print(f"Update result stdout: {result.stdout}")
print(f"Update result stderr: {result.stderr}")
print(f"Return code: {result.returncode}")

if result.returncode == 0:
    # Verify
    result2 = subprocess.run([
        'docker', 'exec', 'rpa-opensource-mysql',
        'mysql', '--default-character-set=utf8mb4', '-uroot', '-prpa123456', 'rpa',
        '-e', "SELECT JSON_VALID(atom_content), JSON_DEPTH(atom_content) FROM c_atom_meta WHERE id = 14;"
    ], capture_output=True, text=True)
    print(f"Verification: {result2.stdout}")

print("Done!")
