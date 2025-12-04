#!/usr/bin/env python3
"""
Verify that all Chinese text has been translated to English in config files.
This script scans config.yaml files for remaining Chinese characters.
"""

import re
from pathlib import Path


def contains_chinese(text):
    """Check if text contains Chinese characters."""
    if not text or not isinstance(text, str):
        return False
    return bool(re.search(r'[\u4e00-\u9fa5]', text))


def scan_yaml_file(file_path):
    """Scan a YAML file for Chinese characters."""
    issues = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Skip comment lines
                if line.strip().startswith('#'):
                    continue
                
                # Check for Chinese characters
                if contains_chinese(line):
                    # Extract the relevant part (value after colon)
                    if ':' in line:
                        key_value = line.split(':', 1)
                        if len(key_value) > 1:
                            value = key_value[1].strip()
                            if contains_chinese(value):
                                issues.append((line_num, line.strip()))
                    else:
                        issues.append((line_num, line.strip()))
    
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return None
    
    return issues


def main():
    """Main function to verify all translations."""
    
    print("=" * 70)
    print("Verifying Chinese to English Translation")
    print("=" * 70)
    print()
    
    # Scan config.yaml files
    components_path = Path(r"e:\astron-rpa\engine\components")
    config_files = list(components_path.glob("*/config.yaml"))
    
    # Also check config_type.yaml files
    config_type_files = list(components_path.glob("*/config_type.yaml"))
    
    # Check actionlib config_type.yaml
    actionlib_config = Path(r"e:\astron-rpa\engine\shared\astronverse-actionlib\config_type.yaml")
    if actionlib_config.exists():
        config_type_files.append(actionlib_config)
    
    all_files = config_files + config_type_files
    
    print(f"Scanning {len(all_files)} configuration files...\n")
    
    total_issues = 0
    files_with_issues = 0
    
    for config_file in sorted(all_files):
        relative_path = config_file.relative_to(Path(r"e:\astron-rpa"))
        
        issues = scan_yaml_file(config_file)
        
        if issues is None:
            continue
        
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            
            print(f"⚠️  {relative_path}")
            print(f"   Found {len(issues)} line(s) with Chinese text:")
            
            for line_num, line_content in issues[:5]:  # Show first 5 issues
                print(f"   Line {line_num}: {line_content[:80]}...")
            
            if len(issues) > 5:
                print(f"   ... and {len(issues) - 5} more")
            
            print()
        else:
            print(f"✅ {relative_path}")
    
    # Summary
    print("\n" + "=" * 70)
    print("Verification Summary:")
    print(f"  Total files scanned: {len(all_files)}")
    print(f"  Files with Chinese text: {files_with_issues}")
    print(f"  Total Chinese text instances: {total_issues}")
    print("=" * 70)
    
    if files_with_issues == 0:
        print("\n🎉 All configuration files are fully translated to English!")
        return 0
    else:
        print(f"\n⚠️  {files_with_issues} file(s) still contain Chinese text")
        print("   Please review and complete the translation.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
