import json
import re

# Read original SQL
with open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# Find line 2 which has atomCommon (id=14)
lines = content.split('\n')
for line in lines:
    if line.startswith("(14,'root','atomCommon',"):
        # Extract JSON between the quotes
        # Pattern: (14,'root','atomCommon','JSON_HERE',0,'1',...
        start = line.find(",'atomCommon','") + len(",'atomCommon','")
        # Find the ending pattern: ',0,'1','
        end = line.find("',0,'1','")
        json_sql_escaped = line[start:end]
        
        print(f"Extracted {len(json_sql_escaped)} characters")
        print(f"First 100 chars: {json_sql_escaped[:100]}")
        print(f"Last 100 chars: {json_sql_escaped[-100:]}")
        
        # Save raw extracted string
        with open(r'e:\astron-rpa\docker\volumes\mysql\original_raw.txt', 'w', encoding='utf-8') as f:
            f.write(json_sql_escaped)
        
        print("\n✓ Saved to original_raw.txt")
        break
