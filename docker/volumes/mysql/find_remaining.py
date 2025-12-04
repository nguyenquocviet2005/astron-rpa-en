# Find remaining Chinese phrases in database
import re
import subprocess
import sys

result = subprocess.run([
    'docker', 'exec', 'rpa-opensource-mysql', 
    'mysql', '--default-character-set=utf8mb4', '-uroot', '-prpa123456', 'rpa', 
    '-N', '-e', 'SELECT atom_content FROM c_atom_meta'
], capture_output=True, encoding='utf-8', errors='replace')

content = result.stdout or ""
if not content:
    print("No output from database")
    print("stderr:", result.stderr)
    sys.exit(1)

chinese_regex = re.compile(r'[\u4e00-\u9fff]+')
remaining = chinese_regex.findall(content)
unique_remaining = sorted(set(remaining), key=lambda x: -len(x))

print(f'Remaining Chinese phrases: {len(unique_remaining)}')
print('\nPhrases to add to translations:')
for phrase in unique_remaining[:100]:
    print(f'    "{phrase}": "",')
