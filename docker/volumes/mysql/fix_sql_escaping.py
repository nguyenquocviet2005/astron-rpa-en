import json

# Read the properly translated JSON
with open(r'e:\astron-rpa\docker\volumes\mysql\atomCommon_translated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("✓ Loaded translated JSON successfully")

# Convert to JSON string (this is what goes in the database as-is)
json_str = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

print(f"JSON string length: {len(json_str)}")

# For MySQL INSERT, we need to escape ONLY:
# 1. Single quotes ' → \'  
# 2. Backslashes \ → \\
# We do NOT escape double quotes because the JSON string itself contains them

# The correct escaping order:
escaped_json = json_str.replace('\\', '\\\\').replace("'", "\\'")

# Generate the SQL statement
sql = f"""INSERT INTO `c_atom_meta` VALUES (14,'root','atomCommon','{escaped_json}',0,'1','2025-10-14 09:14:46',1,'2025-10-14 09:14:46','1.0.1',NULL,'1000001');"""

# Write to file
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'w', encoding='utf-8') as f:
    f.write(sql)

print("✓ Generated correct SQL file")
print(f"Escaped JSON length: {len(escaped_json)}")

# Verify by simulating what MySQL will store
# MySQL will unescape \\ → \ and \' → ' 
stored_value = escaped_json.replace('\\\\', '\x00').replace("\\'", "'").replace('\x00', '\\')

# Try to parse it as JSON
try:
    test_data = json.loads(stored_value)
    print("✓ Verified: The stored value will be valid JSON")
    print(f"First category: {test_data['atomicTree'][0]['title']}")
except Exception as e:
    print(f"✗ ERROR: Stored value will NOT be valid JSON: {e}")
