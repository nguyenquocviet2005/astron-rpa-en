# Split the SQL into individual INSERT statements
content = open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

lines = content.split('\n')
header = lines[0]  # INSERT INTO `c_atom_meta` VALUES

# Create individual INSERT statements
output = []
for i, line in enumerate(lines[1:], 1):
    line = line.strip()
    if not line:
        continue
    # Remove trailing comma and add semicolon
    if line.endswith(','):
        line = line[:-1] + ';'
    
    sql = f"{header}\n{line}\n"
    output.append(sql)

# Write to file
with open(r'e:\astron-rpa\docker\volumes\mysql\atoms_split.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f'Created {len(output)} individual INSERT statements')
