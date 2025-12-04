# Read original content
with open(r'e:\astron-rpa\docker\volumes\mysql\original_raw.txt', 'r', encoding='utf-8') as f:
    original = f.read()

# Find Dict template
idx = original.find('Dict\\":{')
section = original[idx:idx+150]

# Count backslashes before specific quotes
template_start = section.find('template')
print(f"Section around template:\n{section[template_start:template_start+50]}")
print()

# Now look character by character at 'template\":\"{'
s = section[template_start:]
i = s.find('{')
print(f"Characters before and around the brace:")
for j in range(i-5, i+10):
    c = s[j]
    print(f"  pos {j}: char '{c}' (0x{ord(c):02x})")

