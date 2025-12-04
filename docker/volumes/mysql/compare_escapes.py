# Find differences between original and translated files
orig = open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()
trans = open(r'e:\astron-rpa\docker\volumes\mysql\atoms_replace.sql', 'r', encoding='utf-8').read()

# Look for any backslash patterns
import re

# Find all escape sequences in both files
orig_escapes = set(re.findall(r'\\\\?.', orig))
trans_escapes = set(re.findall(r'\\\\?.', trans))

print("Original escape sequences:", sorted(orig_escapes)[:20])
print("\nTranslated escape sequences:", sorted(trans_escapes)[:20])

print("\n\nIn translated but not original:")
for e in sorted(trans_escapes - orig_escapes):
    print(f"  {repr(e)}")

print("\n\nIn original but not translated:")
for e in sorted(orig_escapes - trans_escapes):
    print(f"  {repr(e)}")
