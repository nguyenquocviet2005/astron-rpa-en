# Create UPDATE statements instead of INSERT
# This avoids the full INSERT parsing

content = open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

# Replace curly quotes with regular single quotes (for Str template display)
content = content.replace('\u201c', "'")
content = content.replace('\u201d', "'")

# Convert to REPLACE INTO which handles duplicates
content = content.replace('INSERT INTO', 'REPLACE INTO')

with open(r'e:\astron-rpa\docker\volumes\mysql\atoms_replace.sql', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Created REPLACE INTO statements: {len(content)} bytes')
