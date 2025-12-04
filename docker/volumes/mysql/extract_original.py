import json
import re

# Read original SQL 
with open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the atomCommon JSON from line 2
# Find the JSON between the first ,' and the next ',0 pattern for atomCommon
match = re.search(r"\(14,'root','atomCommon','(.+?)',0,'1'", content, re.DOTALL)
if match:
    json_escaped = match.group(1)
    # The SQL escaping: \' -> ' (single quote), \\ -> \ 
    # But inside JSON, \" are escaped double quotes that need to stay as \"
    # First decode SQL escaping for single quotes
    json_str = json_escaped.replace("\\'", "'")
    
    # Parse JSON - the \" sequences are valid JSON escapes
    data = json.loads(json_str)
    
    print("Keys:", list(data.keys()))
    print("Dict template:", repr(data['types']['Dict']['template']))
    print("Dict funcList useSrc:", data['types']['Dict']['funcList'][0]['useSrc'])
    
    # Save to file for comparison
    with open(r'e:\astron-rpa\docker\volumes\mysql\original_atomCommon.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("\n✓ Saved original atomCommon to original_atomCommon.json")
else:
    print("Could not find atomCommon in SQL")
