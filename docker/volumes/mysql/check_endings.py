# Check if the issue is with line endings
orig = open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'rb').read()
trans = open(r'e:\astron-rpa\docker\volumes\mysql\atoms_replace.sql', 'rb').read()

# Count line endings
print(f"Original CR count: {orig.count(b'\\r')}")
print(f"Original LF count: {orig.count(b'\\n')}")
print(f"Original CRLF count: {orig.count(b'\\r\\n')}")

print(f"\nTranslated CR count: {trans.count(b'\\r')}")
print(f"Translated LF count: {trans.count(b'\\n')}")
print(f"Translated CRLF count: {trans.count(b'\\r\\n')}")

# Check for any unusual bytes around the first line
print(f"\nOriginal first 100 bytes: {orig[:100]}")
print(f"\nTranslated first 100 bytes: {trans[:100]}")
