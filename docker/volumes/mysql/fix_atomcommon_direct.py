import json
import mysql.connector

# Read the translated JSON
with open(r'e:\astron-rpa\docker\volumes\mysql\atomCommon_translated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert to JSON string (no escaping needed - MySQL connector handles it)
json_str = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

# Connect to MySQL in Docker container
conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3307,  # Will need to expose this port or run inside container
    user='root',
    password='rpa123456',
    database='rpa'
)

cursor = conn.cursor()

# Delete existing record
cursor.execute("DELETE FROM c_atom_meta WHERE atom_key='atomCommon'")

# Insert with proper escaping handled by MySQL connector
sql = """INSERT INTO c_atom_meta VALUES 
    (14, 'root', 'atomCommon', %s, 0, '1', '2025-10-14 09:14:46', 1, '2025-10-14 09:14:46', '1.0.1', NULL, '1000001')"""

cursor.execute(sql, (json_str,))

conn.commit()
cursor.close()
conn.close()

print(f"✓ Successfully updated atomCommon ({len(json_str)} bytes)")
