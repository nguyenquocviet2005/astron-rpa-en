# Check original Str type template
with open(r'e:\astron-rpa\docker\volumes\mysql\original_raw.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Find Str type
search = '\\"Str\\":'
idx = content.find(search)
if idx >= 0:
    print('Str type section:')
    section = content[idx:idx+300]
    print(section)
    print()
    print('Repr:')
    print(repr(section))
