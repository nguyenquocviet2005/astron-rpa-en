# Test by loading only a small chunk
orig = open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

# Find atomCommon's content
start = orig.find("(14,'root','atomCommon'")
# Find end - next tuple starts with (15,
end = orig.find("\n(15,'")

atomCommon_orig = "INSERT INTO `c_atom_meta` VALUES\n" + orig[start:end].rstrip(',') + ";"

# Load and apply translations
import sys
sys.path.insert(0, r'e:\astron-rpa\docker\volumes\mysql')
from translate_all_atoms_v2 import translate_text

atomCommon_trans = translate_text(atomCommon_orig)

# Replace curly quotes 
atomCommon_trans = atomCommon_trans.replace('\u201c', "'")
atomCommon_trans = atomCommon_trans.replace('\u201d', "'")

# Save both for comparison
with open(r'e:\astron-rpa\docker\volumes\mysql\test_orig.sql', 'w', encoding='utf-8') as f:
    f.write(atomCommon_orig)
    
with open(r'e:\astron-rpa\docker\volumes\mysql\test_trans.sql', 'w', encoding='utf-8') as f:
    f.write(atomCommon_trans)

print(f"Original: {len(atomCommon_orig)} bytes")
print(f"Translated: {len(atomCommon_trans)} bytes")
