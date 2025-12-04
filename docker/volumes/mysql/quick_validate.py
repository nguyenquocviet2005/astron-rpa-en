import json

try:
    with open(r'e:\astron-rpa\docker\volumes\mysql\final_test.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    
    print("✓ JSON is VALID!")
    print(f"Keys: {list(data.keys())}")
    print(f"Total categories: {len(data['atomicTree'])}")
    print(f"First category: {data['atomicTree'][0]['title']}")
    
    if 'atomics' in data['atomicTree'][0] and len(data['atomicTree'][0]['atomics']) > 0:
        first_sub = data['atomicTree'][0]['atomics'][0]
        print(f"First subcategory: {first_sub['title']}")
        
except Exception as e:
    print(f"✗ JSON is INVALID: {e}")
