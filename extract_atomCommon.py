#!/usr/bin/env python3
"""
Script to extract atomCommon JSON from SQL and fix escaping.
"""

import json

# Read the SQL file
with open('E:/astron-rpa/docker/volumes/mysql/init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the atomCommon JSON
marker = "'atomCommon','"
start = content.find(marker)
if start > 0:
    json_start = start + len(marker)
    # Find matching closing brace
    depth = 0
    json_end = json_start
    in_string = False
    escape_next = False
    
    for i in range(json_start, len(content)):
        char = content[i]
        
        if escape_next:
            escape_next = False
            continue
            
        if char == '\\':
            escape_next = True
            continue
            
        if char == '"' and not escape_next:
            in_string = not in_string
            continue
            
        if not in_string:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0:
                    json_end = i + 1
                    break
    
    json_str = content[json_start:json_end]
    print(f'Extracted JSON length: {len(json_str)}')
    
    # The SQL escapes special characters:
    # - \" becomes " in the actual JSON
    # - \' becomes ' 
    # Just unescape the backslash-quote sequences
    json_str = json_str.replace('\\"', '"')
    json_str = json_str.replace("\\'", "'")
    
    # Save
    with open('E:/astron-rpa/atomCommon_original.json', 'w', encoding='utf-8') as f:
        f.write(json_str)
    
    # Test parse
    try:
        data = json.loads(json_str)
        print(f'JSON parsed successfully! Keys: {list(data.keys())}')
    except json.JSONDecodeError as e:
        print(f'JSON parse error at position {e.pos}: {e.msg}')
        # Show context around error
        start_ctx = max(0, e.pos - 50)
        end_ctx = min(len(json_str), e.pos + 50)
        print(f'Context: ...{json_str[start_ctx:end_ctx]}...')
else:
    print('atomCommon not found in SQL file!')
