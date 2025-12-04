import json
import base64

# Read the properly translated JSON
with open(r'e:\astron-rpa\docker\volumes\mysql\atomCommon_translated.json', 'r', encoding='utf-8') as f:
    json_str = f.read()

# Validate JSON
json.loads(json_str)

# Base64 encode
b64_str = base64.b64encode(json_str.encode('utf-8')).decode('ascii')

# Generate SQL using FROM_BASE64
sql = f"""DELETE FROM `c_atom_meta` WHERE atom_key='atomCommon';
INSERT INTO `c_atom_meta` VALUES (14,'root','atomCommon',FROM_BASE64('{b64_str}'),0,'1','2025-10-14 09:14:46',1,'2025-10-14 09:14:46','1.0.1',NULL,'1000001');"""

# Write to file
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data_b64.sql', 'w', encoding='utf-8') as f:
    f.write(sql)

print(f"✓ Generated SQL with BASE64 encoding, length: {len(b64_str)}")
