"""
Load English atom metadata from translated config files and upload to database via API.
This script reads the translated config.yaml files and pushes them to the robot-service API.
"""
import sys
import os
import yaml
import json
import requests
from pathlib import Path

# Configuration
ROBOT_SERVICE_URL = "http://localhost:8080/robot"
ENGINE_PATH = Path("E:/astron-rpa/engine")
COMPONENTS_PATH = ENGINE_PATH / "components"

def load_config_files():
    """Load all config.yaml files from components"""
    configs = {}
    
    for component_dir in COMPONENTS_PATH.iterdir():
        if not component_dir.is_dir():
            continue
            
        config_file = component_dir / "config.yaml"
        if config_file.exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config_data = yaml.safe_load(f)
                    if config_data and 'atomic' in config_data:
                        configs[component_dir.name] = config_data
                        print(f"✓ Loaded {component_dir.name}")
            except Exception as e:
                print(f"✗ Error loading {component_dir.name}: {e}")
    
    return configs

def build_atom_map(configs):
    """Build atom map for API upload"""
    atom_map = {}
    
    for component_name, config in configs.items():
        if 'atomic' not in config:
            continue
            
        for atom_key, atom_def in config['atomic'].items():
            # Convert YAML structure to the format expected by the API
            atom_map[atom_key] = {
                "key": atom_key,
                "title": atom_def.get('title', ''),
                "version": atom_def.get('version', '1.0.0'),
                "src": atom_def.get('src', ''),
                "comment": atom_def.get('comment', ''),
                "icon": atom_def.get('icon', ''),
                "helpManual": atom_def.get('helpManual', ''),
                "inputList": atom_def.get('inputList', []),
                "outputList": atom_def.get('outputList', []),
            }
            
            # Add optional fields
            if 'noAdvanced' in atom_def:
                atom_map[atom_key]['noAdvanced'] = atom_def['noAdvanced']
                
    return atom_map

def upload_to_api(atom_map):
    """Upload atom metadata to robot-service API"""
    api_url = f"{ROBOT_SERVICE_URL}/atom/save-atomics"
    
    payload = {
        "atomMap": atom_map,
        "saveWay": "replace"  # or "update"
    }
    
    try:
        print(f"\nUploading {len(atom_map)} atoms to {api_url}...")
        response = requests.post(api_url, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Upload successful: {result}")
            return True
        else:
            print(f"✗ Upload failed: HTTP {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"✗ Error uploading: {e}")
        return False

def main():
    print("=" * 60)
    print("Loading English Atom Metadata from Translated Config Files")
    print("=" * 60)
    
    # Step 1: Load config files
    print("\n[1/3] Loading config.yaml files...")
    configs = load_config_files()
    print(f"Loaded {len(configs)} component configs")
    
    # Step 2: Build atom map
    print("\n[2/3] Building atom map...")
    atom_map = build_atom_map(configs)
    print(f"Built atom map with {len(atom_map)} atoms")
    
    # Save to file for inspection
    output_file = "atom_metadata_english.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(atom_map, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_file} for inspection")
    
    # Step 3: Upload to API
    print("\n[3/3] Uploading to robot-service API...")
    success = upload_to_api(atom_map)
    
    if success:
        print("\n" + "=" * 60)
        print("SUCCESS! English metadata loaded into database")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Clear your browser cache (Ctrl+Shift+Delete)")
        print("2. Reload the application (Ctrl+F5)")
        print("3. Check the workflow builder - atoms should now be in English!")
    else:
        print("\n" + "=" * 60)
        print("FAILED - Could not upload metadata")
        print("=" * 60)
        print("\nTroubleshooting:")
        print("1. Ensure Docker services are running: docker compose ps")
        print("2. Check robot-service logs: docker logs rpa-opensource-robot-service")
        print("3. Verify the API is accessible: curl http://localhost:8080/robot/atom/tree")

if __name__ == "__main__":
    main()
