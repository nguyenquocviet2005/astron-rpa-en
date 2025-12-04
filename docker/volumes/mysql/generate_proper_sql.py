#!/usr/bin/env python3
import json
import sys

# Read JSON from stdin
json_data = sys.stdin.read()

# Validate it's proper JSON
data = json.loads(json_data)

# Output SQL with proper Python string escaping for MySQL
json_str = json.dumps(data, ensure_ascii=False, separators=(',', ':'))

# MySQL needs single quotes escaped as ''
escaped = json_str.replace("\\", "\\\\").replace("'", "\\'")

print(f"DELETE FROM c_atom_meta WHERE atom_key='atomCommon';")
print(f"INSERT INTO c_atom_meta VALUES (14,'root','atomCommon','{escaped}',0,'1','2025-10-14 09:14:46',1,'2025-10-14 09:14:46','1.0.1',NULL,'1000001');")
