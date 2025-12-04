import json

with open(r'e:\astron-rpa\docker\volumes\mysql\current_atomCommon.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

print('✓ JSON is valid')
print(f'Keys: {list(data.keys())}')
print(f'First atom: {data["atomicTree"][0]["title"]}')
print(f'Total categories: {len(data["atomicTree"])}')

# Check if there are any problematic escape sequences
json_str = json.dumps(data, ensure_ascii=False)
if "\\'" in json_str:
    print("⚠ Warning: Found escaped single quotes")
if '\\"' in json_str:
    print("⚠ Warning: Found escaped double quotes") 
