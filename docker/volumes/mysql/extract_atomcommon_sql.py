# Extract just the atomCommon INSERT from the full SQL
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data_en.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the atomCommon line
lines = content.split('\n')
for line in lines:
    if line.startswith("(14,'root','atomCommon',"):
        # Create a single INSERT statement
        sql = f"INSERT INTO `c_atom_meta` VALUES\n{line}"
        # Remove trailing comma if present
        if sql.endswith(','):
            sql = sql[:-1] + ';'
        elif not sql.endswith(';'):
            sql = sql + ';'
            
        with open(r'e:\astron-rpa\docker\volumes\mysql\atomcommon_only_en.sql', 'w', encoding='utf-8') as f:
            f.write(sql)
        
        print(f"✓ Generated atomcommon_only_en.sql ({len(sql)} bytes)")
        break
