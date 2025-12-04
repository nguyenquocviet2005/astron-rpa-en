# Extract original atomCommon INSERT properly
with open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# Find line starting with (14,'root','atomCommon'
lines = content.split('\n')
for i, line in enumerate(lines):
    if line.startswith("(14,'root','atomCommon'"):
        # Remove trailing comma if present and add semicolon
        atom_line = line.rstrip()
        if atom_line.endswith(','):
            atom_line = atom_line[:-1]  # Remove comma
        
        # Create INSERT statement with proper ending
        sql = "INSERT INTO `c_atom_meta` VALUES\n" + atom_line + ";"
        
        with open(r'e:\astron-rpa\docker\volumes\mysql\original_atomcommon_only.sql', 'w', encoding='utf-8') as f:
            f.write(sql)
        print(f"Extracted line {i+1}, length {len(line)}")
        print(f"SQL ends with: {sql[-50:]}")
        break
