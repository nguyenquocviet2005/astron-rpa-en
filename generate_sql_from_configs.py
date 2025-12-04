#!/usr/bin/env python3
"""
Generate init_c_atom_meta_data.sql from English config.yaml files.
This script scans all component config files and generates SQL INSERT statements.
"""

import json
import yaml
import sys
from pathlib import Path
from datetime import datetime


def load_config(config_path):
    """Load and parse a config.yaml file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading {config_path}: {e}")
        return None


def escape_sql_string(s):
    """Escape string for SQL INSERT."""
    if s is None:
        return 'NULL'
    # Convert to string and escape single quotes
    s = str(s).replace("'", "''").replace("\\", "\\\\")
    return f"'{s}'"


def generate_insert_statement(atom_data, atom_id):
    """Generate SQL INSERT statement for an atom."""
    
    # Extract fields
    key = atom_data.get('key', '')
    
    # Serialize the entire atom_data as JSON for atom_content
    atom_content_json = json.dumps(atom_data, ensure_ascii=False)
    
    # Fields for the INSERT matching actual table structure:
    # id, parent_key, atom_key, atom_content, deleted, creator_id, create_time, updater_id, update_time, version, sort, version_num
    atom_key = escape_sql_string(key)
    parent_key = 'NULL'  # Can be derived from atom_key if needed
    atom_content = escape_sql_string(atom_content_json)
    
    # Default values matching actual schema
    deleted = 0
    creator_id = escape_sql_string('73')
    create_time = 'CURRENT_TIMESTAMP'
    updater_id = escape_sql_string('73')
    update_time = 'CURRENT_TIMESTAMP'
    version = escape_sql_string(atom_data.get('version', '1.0.0'))
    sort = atom_id * 1000  # Use ID-based sorting
    version_num = escape_sql_string(atom_data.get('version', '1.0.0'))
    
    sql = f"INSERT INTO c_atom_meta (id, parent_key, atom_key, atom_content, deleted, creator_id, create_time, updater_id, update_time, version, sort, version_num) VALUES ({atom_id}, {parent_key}, {atom_key}, {atom_content}, {deleted}, {creator_id}, {create_time}, {updater_id}, {update_time}, {version}, {sort}, {version_num});"
    
    return sql


def process_component_config(config_path, component_name):
    """Process a single component's config.yaml file."""
    config_data = load_config(config_path)
    
    if not config_data:
        return []
    
    atoms = []
    
    # Config files have an 'atomic' section containing atom definitions
    if isinstance(config_data, dict) and 'atomic' in config_data:
        atomic_section = config_data['atomic']
        
        for atom_key, atom_data in atomic_section.items():
            # Create full atom object with key
            full_atom = {'key': atom_key}
            full_atom.update(atom_data)
            
            # Add version if not present
            if 'version' not in full_atom:
                full_atom['version'] = '1.0.0'
            
            # Add src if not present (construct from component name and atom key)
            if 'src' not in full_atom:
                # Extract component class name (e.g., "browser" from "astronverse-browser")
                component_class = component_name.replace('astronverse-', '')
                class_name = ''.join(word.capitalize() for word in component_class.split('-'))
                
                # Construct src path (this is a best guess based on patterns)
                if '.' in atom_key:
                    parts = atom_key.split('.')
                    full_atom['src'] = f"astronverse.{component_class}.{parts[0].lower()}.{parts[0]}().{parts[1]}"
            
            atoms.append(full_atom)
    
    return atoms


def main():
    """Main function to generate SQL file."""
    
    print("=" * 70)
    print("Generating init_c_atom_meta_data.sql from English Config Files")
    print("=" * 70)
    print()
    
    # Base paths
    components_path = Path(r"E:\astron-rpa\engine\components")
    shared_path = Path(r"E:\astron-rpa\engine\shared")
    output_file = Path(r"E:\astron-rpa\docker\volumes\mysql\init_c_atom_meta_data.sql")
    
    all_atoms = []
    
    # Process components
    print("Processing components...")
    for component_dir in sorted(components_path.iterdir()):
        if not component_dir.is_dir() or not component_dir.name.startswith("astronverse-"):
            continue
        
        config_file = component_dir / "config.yaml"
        if config_file.exists():
            print(f"  📝 {component_dir.name}")
            atoms = process_component_config(config_file, component_dir.name)
            all_atoms.extend(atoms)
            print(f"     Found {len(atoms)} atoms")
    
    # Process shared components
    print("\nProcessing shared components...")
    actionlib_dir = shared_path / "astronverse-actionlib"
    actionlib_config = actionlib_dir / "config.yaml"
    
    if actionlib_config.exists():
        print(f"  📝 astronverse-actionlib")
        atoms = process_component_config(actionlib_config, "astronverse-actionlib")
        all_atoms.extend(atoms)
        print(f"     Found {len(atoms)} atoms")
    
    # Check config_type.yaml files for type definitions
    for component_dir in [components_path / "astronverse-browser", 
                         components_path / "astronverse-excel",
                         components_path / "astronverse-word",
                         shared_path / "astronverse-actionlib"]:
        config_type_file = component_dir / "config_type.yaml"
        if config_type_file.exists():
            print(f"  📝 {component_dir.name}/config_type.yaml")
            # config_type.yaml typically contains type definitions, not atoms
            # Skip for now unless they need to be in the database
    
    print(f"\n✅ Total atoms collected: {len(all_atoms)}")
    
    # Generate SQL file
    print(f"\n📝 Generating SQL file: {output_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("-- Auto-generated atom metadata with English translations\n")
        f.write(f"-- Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"-- Total atoms: {len(all_atoms)}\n\n")
        
        # Generate INSERT statements
        for idx, atom in enumerate(all_atoms, start=1):
            sql = generate_insert_statement(atom, idx)
            f.write(sql + "\n")
    
    print(f"✅ SQL file generated successfully!")
    print(f"   Location: {output_file}")
    print(f"   Total records: {len(all_atoms)}")
    print()
    print("Next steps:")
    print("  1. Stop Docker: docker compose down -v")
    print("  2. Start Docker: docker compose up -d")
    print("  3. The database will initialize with English metadata")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
