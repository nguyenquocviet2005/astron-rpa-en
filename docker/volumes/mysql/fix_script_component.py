# -*- coding: utf-8 -*-
"""Fix the Script.component atom that was skipped during parsing"""
import subprocess
from translate_all_atoms_v2 import translate_text

orig_json = '{"key": "Script.component", "title": "运行组件", "version": "1.0.1", "src": "astronverse.script.script.Script().component", "comment": "运行组件(@{component:组件})", "inputList": [{"types": "Str", "formType": {"type": "INPUT_VARIABLE_PYTHON"}, "key": "component", "title": "选择组件", "name": "component", "tip": "", "value": [{"type": "str", "value": ""}], "required": true}], "outputList": [], "icon": "", "helpManual": ""}'

translated = translate_text(orig_json)
print("Original:", orig_json[:100])
print("Translated:", translated[:100])

# Escape for SQL
escaped = translated.replace("'", "''")
sql = f"UPDATE c_atom_meta SET atom_content = '{escaped}' WHERE id = 311;"

# Save to file
with open('fix_311.sql', 'w', encoding='utf-8') as f:
    f.write(sql)
print("\nSaved to fix_311.sql")

# Execute
cmd = 'docker cp fix_311.sql rpa-opensource-mysql:/tmp/fix_311.sql'
subprocess.run(cmd, shell=True)
cmd = 'docker exec rpa-opensource-mysql bash -c "mysql -u root -prpa123456 rpa < /tmp/fix_311.sql"'
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print(f"Return code: {result.returncode}")
if result.stderr:
    print(f"Stderr: {result.stderr}")
print("Done!")
