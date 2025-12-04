import re

# Read original SQL file
with open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
    original_sql = f.read()

# Read translated escaped JSON
with open(r'e:\astron-rpa\docker\volumes\mysql\translated_escaped.txt', 'r', encoding='utf-8') as f:
    translated_json = f.read()

# Find and replace the atomCommon JSON in the SQL
# The pattern is: (14,'root','atomCommon','...JSON...',0,'1',...
lines = original_sql.split('\n')
new_lines = []

for line in lines:
    if line.startswith("(14,'root','atomCommon',"):
        # Replace the JSON part
        # Find the pattern: 'atomCommon','OLD_JSON',0,'1'
        start = line.find(",'atomCommon','") + len(",'atomCommon','")
        end = line.find("',0,'1','")
        
        # Reconstruct the line with translated JSON
        new_line = line[:start] + translated_json + line[end:]
        new_lines.append(new_line)
        print(f"✓ Replaced atomCommon JSON")
    else:
        new_lines.append(line)

# Write new SQL file
new_sql = '\n'.join(new_lines)
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data_en.sql', 'w', encoding='utf-8') as f:
    f.write(new_sql)

print(f"\n✓ Generated init_c_atom_meta_data_en.sql")
print(f"Original SQL size: {len(original_sql)} bytes")
print(f"New SQL size: {len(new_sql)} bytes")
