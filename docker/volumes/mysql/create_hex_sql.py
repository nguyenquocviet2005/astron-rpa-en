import json

# Read the properly translated JSON
with open(r'e:\astron-rpa\docker\volumes\mysql\atomCommon_translated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert to JSON string
json_str = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

# Convert to hex for MySQL
hex_str = json_str.encode('utf-8').hex()

# Generate SQL using hex notation
sql = f"""DELETE FROM `c_atom_meta` WHERE atom_key='atomCommon';
INSERT INTO `c_atom_meta` VALUES (14,'root','atomCommon',UNHEX('{hex_str}'),0,'1','2025-10-14 09:14:46',1,'2025-10-14 09:14:46','1.0.1',NULL,'1000001');"""

# Write to file
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data_hex.sql', 'w', encoding='utf-8') as f:
    f.write(sql)

print("✓ Generated SQL with HEX encoding")
print(f"JSON length: {len(json_str)}")
print(f"HEX length: {len(hex_str)}")
