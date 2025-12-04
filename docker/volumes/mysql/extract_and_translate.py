# Load atomCommon JSON and insert via Python
import json

# Read the original atomCommon row
orig = open(r'e:\astron-rpa\astron-rpa-original\docker\volumes\mysql\init_c_atom_meta_data.sql', 'r', encoding='utf-8').read()

# Find atomCommon's content
start = orig.find("(14,'root','atomCommon','")
start_json = start + len("(14,'root','atomCommon','")
# Find end of JSON - look for ',0,1,' or ',1,1,' pattern (deleted,creator_id)
import re
# The format is '...',deleted,creator_id - but need to handle escaped quotes
# Look for pattern ',0,' or ',1,' followed by timestamp
match = re.search(r"',0,1,'20", orig[start_json:])
if not match:
    match = re.search(r"',1,1,'20", orig[start_json:])
if match:
    end_json = start_json + match.start()
    json_content = orig[start_json:end_json]
    print(f"Found JSON from {start_json} to {end_json}, length={len(json_content)}")
else:
    print("Could not find end of JSON")
    print(f"Searching from position {start_json}")
    print(f"Next 200 chars: {orig[start_json:start_json+200]}")
    exit(1)

# Unescape the SQL string escaping
# SQL uses '' for ' and \" for "
# Actually, in this format: \' for literal ' and \" for literal "
json_content = json_content.replace("\\'", "'")
json_content = json_content.replace('\\"', '"')
json_content = json_content.replace('\\\\', '\\')

# Now translate
import sys
sys.path.insert(0, r'e:\astron-rpa\docker\volumes\mysql')
from translate_all_atoms_v2 import translate_text

json_translated = translate_text(json_content)

# Replace curly quotes with single quotes (for the template "Hello")
json_translated = json_translated.replace('\u201c', "'")
json_translated = json_translated.replace('\u201d', "'")

# Verify it's valid JSON
try:
    parsed = json.loads(json_translated)
    print("JSON is valid!")
    print(f"JSON depth: approximately {len(str(parsed))} chars")
except json.JSONDecodeError as e:
    print(f"JSON error: {e}")
    # Show around error position
    pos = e.pos
    print(f"Context around error: {json_translated[max(0,pos-50):pos+50]}")
    exit(1)

# Save the translated JSON
with open(r'e:\astron-rpa\docker\volumes\mysql\atomcommon_translated.json', 'w', encoding='utf-8') as f:
    f.write(json_translated)

print(f"Saved atomcommon_translated.json ({len(json_translated)} bytes)")
