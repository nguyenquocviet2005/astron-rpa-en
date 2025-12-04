import re

# Read the full SQL file
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the atomCommon INSERT - line starting with (14,'root','atomCommon'
# Split by INSERT INTO pattern
lines = content.split('\n')
atomCommon_line = None
for line in lines:
    if line.startswith("(14,'root','atomCommon'"):
        atomCommon_line = line.strip()
        break

if atomCommon_line:
    # Remove trailing comma if present and add semicolon
    if atomCommon_line.endswith(','):
        atomCommon_line = atomCommon_line[:-1] + ';'
    elif not atomCommon_line.endswith(';'):
        atomCommon_line = atomCommon_line + ';'
    
    # Create complete INSERT statement
    sql = "INSERT INTO c_atom_meta VALUES\n" + atomCommon_line
    
    with open(r'e:\astron-rpa\docker\volumes\mysql\atomcommon_en_only.sql', 'w', encoding='utf-8') as f:
        f.write(sql)
    
    print(f"Extracted atomCommon INSERT ({len(sql)} bytes)")
    print(f"First 200: {sql[:200]}")
else:
    print("atomCommon line not found!")