import json

# Read translated SQL-escaped string
with open(r'e:\astron-rpa\docker\volumes\mysql\translated_escaped.txt', 'r', encoding='utf-8') as f:
    escaped = f.read()

# The file contains SQL-escaped JSON:
# - \" means literal quote in JSON
# - \\" means literal backslash + quote (for nested JSON strings like template values)
# - \' means literal single quote

# For validation, we need to convert SQL escaping to actual JSON
# Step 1: Replace \' with ' (SQL single quote escape)
unescaped = escaped.replace("\\'", "'")

# Step 2: Replace \" with " (SQL double quote escape) 
# But be careful - \\\" means \ + \" which is escaped quote inside a JSON string value
# First, let's try direct replacement and see
unescaped = unescaped.replace('\\"', '"')

try:
    data = json.loads(unescaped)
    print("✓ JSON is VALID!")
    print(f"Keys: {list(data.keys())}")
    print(f"atomicTree count: {len(data['atomicTree'])}")
    print(f"First atom: {data['atomicTree'][0]['title']}")
    # Check the Str template
    str_type = data.get('types', {}).get('Str', {})
    print(f"Str template: {repr(str_type.get('template'))}")
    # Check Dict template  
    dict_type = data.get('types', {}).get('Dict', {})
    print(f"Dict template: {repr(dict_type.get('template'))}")
except json.JSONDecodeError as e:
    print(f"✗ JSON is INVALID: {e}")
    # Show context around error
    pos = e.pos
    print(f"\nContext around error (pos {pos}):")
    print(unescaped[max(0, pos-50):pos+50])
