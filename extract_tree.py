# Extract atomicTree structure from SQL backup
import json
import re

with open('c8a7071_sql.txt', encoding='utf-8') as f:
    content = f.read()

# Find the atomCommon row which contains atomicTree
# Looking for pattern: 'atomCommon', '{"atomicTree":...}'
match = re.search(r"'atomCommon',\s*'(\{.*?\})'\)", content, re.DOTALL)

if match:
    json_str = match.group(1)
    # Unescape single quotes
    json_str = json_str.replace("\\'", "'")
    
    try:
        data = json.loads(json_str)
        tree = data.get('atomicTree', [])
        
        print("="*60)
        print("ATOMIC TREE STRUCTURE (Categories and Hierarchy)")
        print("="*60)
        
        def print_tree(items, level=0):
            indent = "  " * level
            for item in items:
                key = item.get('key', 'unknown')
                title = item.get('title', '')
                children = item.get('atomics', [])
                
                if children:
                    # This is a category/parent
                    print(f"{indent}📁 {key} ({title}) - {len(children)} children")
                    print_tree(children, level + 1)
                else:
                    # This is a leaf atom
                    print(f"{indent}📄 {key}")
        
        print_tree(tree)
        
        # Also print top-level categories summary
        print("\n" + "="*60)
        print("TOP LEVEL CATEGORIES SUMMARY:")
        print("="*60)
        for cat in tree:
            key = cat.get('key')
            title = cat.get('title')
            children = cat.get('atomics', [])
            sub_count = len([c for c in children if 'atomics' in c])
            leaf_count = len([c for c in children if 'atomics' not in c])
            print(f"  {key} ({title}): {sub_count} sub-categories, {leaf_count} leaf atoms")
            
    except json.JSONDecodeError as e:
        print(f"JSON Parse Error: {e}")
        print("Raw JSON (first 1000 chars):")
        print(json_str[:1000])
else:
    print("Could not find atomCommon in SQL file")
    # Let's try a different approach - find atomicTree directly
    print("\nSearching for atomicTree directly...")
    if "atomicTree" in content:
        idx = content.find("atomicTree")
        print(f"Found at position {idx}")
        print(content[idx:idx+500])
