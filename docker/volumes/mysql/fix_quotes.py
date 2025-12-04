# Script to fix the curly quotes issue

# Read current file
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# The problem: straight quotes ("Hello") should be curly quotes ("Hello")
# Replace "Hello" (straight) with "Hello" (curly: U+201C and U+201D)
content = content.replace('"Hello"', '\u201cHello\u201d')

# Similarly fix other template values that might have the same issue
# Check for patterns like \"\"<word>\"\" and fix them

# Save fixed content
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open(r'e:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8') as f:
    content = f.read()
    hello_idx = content.find('Hello')
    if hello_idx > 0:
        chunk = content[hello_idx-10:hello_idx+15]
        print(f"Around Hello: {repr(chunk)}")
        for c in chunk:
            print(f"  '{c}' = {ord(c)}")