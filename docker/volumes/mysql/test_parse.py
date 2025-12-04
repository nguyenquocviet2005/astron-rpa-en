import json

# Test parsing the extracted JSON
with open(r'e:\astron-rpa\docker\volumes\mysql\atomCommon_original.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

print("✓ JSON parsed successfully!")
print(f"Keys: {list(data.keys())}")
print(f"First atom tree item: {data['atomicTree'][0]['title']}")
print(f"Total atom categories: {len(data['atomicTree'])}")
