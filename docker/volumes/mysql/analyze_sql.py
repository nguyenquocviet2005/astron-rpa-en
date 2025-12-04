# Analyze the SQL structure
content = open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

# Count values tuples
values_count = content.count(",'root','")
print(f'Number of value tuples: {values_count}')

# Check structure
if content.startswith('INSERT INTO'):
    print('Starts with INSERT INTO')
    
# Find all line counts
lines = content.split('\n')
print(f'Total lines: {len(lines)}')

# Check what each line starts with
for i, line in enumerate(lines[:10]):
    print(f'Line {i}: {line[:80] if len(line) > 80 else line}...')
