# Replace curly quotes with their escaped hex equivalents for MySQL
content = open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

# The curly quotes: " (U+201C) and " (U+201D)
# In MySQL we can use their UTF-8 byte sequences
# U+201C = E2 80 9C
# U+201D = E2 80 9D

# Actually, let's just try removing them entirely and using regular quotes
# since they're just for display
content = content.replace('\u201c', "'")
content = content.replace('\u201d', "'")

with open(r'e:\astron-rpa\docker\volumes\mysql\atoms_fixed.sql', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Wrote {len(content)} bytes with curly quotes replaced')
