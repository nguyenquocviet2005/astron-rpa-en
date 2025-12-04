import yaml
from pathlib import Path

COMPONENTS_PATH = Path("E:/astron-rpa/engine/components")

for component_dir in sorted(COMPONENTS_PATH.iterdir()):
    if not component_dir.is_dir():
        continue
    
    config_file = component_dir / "config.yaml"
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
            print(f"OK: {component_dir.name}")
        except Exception as e:
            print(f"ERROR: {component_dir.name}")
            if hasattr(e, 'problem_mark'):
                print(f"  Line {e.problem_mark.line + 1}, Column {e.problem_mark.column + 1}")
                # Read the problematic line
                with open(config_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if e.problem_mark.line < len(lines):
                        print(f"  Content: {lines[e.problem_mark.line].strip()}")
