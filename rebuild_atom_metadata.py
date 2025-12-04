#!/usr/bin/env python3
"""
Rebuild atom metadata after translating config files.
Run this script to regenerate all atom metadata with English translations.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_meta_script(component_path):
    """Run meta.py for a component."""
    meta_file = component_path / "meta.py"
    
    if not meta_file.exists():
        print(f"  ⚠️  No meta.py found in {component_path.name}")
        return False
    
    print(f"  📝 Running meta.py for {component_path.name}...")
    
    try:
        # Change to component directory
        original_dir = os.getcwd()
        os.chdir(component_path)
        
        # Run meta.py
        result = subprocess.run(
            [sys.executable, "meta.py"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        os.chdir(original_dir)
        
        if result.returncode == 0:
            print(f"  ✅ Successfully rebuilt {component_path.name}")
            return True
        else:
            print(f"  ❌ Error in {component_path.name}:")
            print(f"     {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"  ⏱️  Timeout in {component_path.name}")
        os.chdir(original_dir)
        return False
    except Exception as e:
        print(f"  ❌ Exception in {component_path.name}: {e}")
        os.chdir(original_dir)
        return False


def main():
    """Main function to rebuild all component metadata."""
    
    print("=" * 70)
    print("Rebuilding Atom Metadata with English Translations")
    print("=" * 70)
    print()
    
    # Base path for components
    components_path = Path(r"e:\astron-rpa\engine\components")
    
    if not components_path.exists():
        print(f"❌ Components directory not found: {components_path}")
        return 1
    
    # Get all component directories
    component_dirs = [d for d in components_path.iterdir() if d.is_dir() and d.name.startswith("astronverse-")]
    
    print(f"Found {len(component_dirs)} components to rebuild\n")
    
    success_count = 0
    failed_count = 0
    skipped_count = 0
    
    for component_dir in sorted(component_dirs):
        print(f"🔨 {component_dir.name}")
        
        meta_file = component_dir / "meta.py"
        if not meta_file.exists():
            print(f"  ⏭️  Skipped (no meta.py)")
            skipped_count += 1
            continue
        
        if run_meta_script(component_dir):
            success_count += 1
        else:
            failed_count += 1
        
        print()
    
    # Summary
    print("=" * 70)
    print("Rebuild Summary:")
    print(f"  ✅ Success: {success_count}")
    print(f"  ❌ Failed:  {failed_count}")
    print(f"  ⏭️  Skipped: {skipped_count}")
    print("=" * 70)
    
    if failed_count == 0:
        print("\n🎉 All metadata successfully rebuilt with English translations!")
        return 0
    else:
        print(f"\n⚠️  {failed_count} component(s) failed to rebuild")
        return 1


if __name__ == "__main__":
    sys.exit(main())
