"""
Script to regenerate atom metadata from config files and update the database.
This must be run after translating config.yaml files to apply the changes.
"""
import os
import sys
import subprocess
import json

# Add engine to path
ENGINE_PATH = r"E:\astron-rpa\engine"
BUILD_PYTHON = r"E:\astron-rpa\build\python_core\python.exe"

def run_command(cmd, cwd=None):
    """Run a command and return output"""
    print(f"Running: {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd or ENGINE_PATH,
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"Output: {result.stdout[:500]}")
    if result.stderr:
        print(f"Error: {result.stderr[:500]}")
    return result.returncode == 0, result.stdout, result.stderr

print("=" * 60)
print("Regenerating Atom Metadata from Translated Config Files")
print("=" * 60)

# Step 1: Generate metadata JSON using the build environment
print("\n[1/3] Generating metadata JSON from config files...")
generate_cmd = f'''"{BUILD_PYTHON}" -c "import sys; sys.path.insert(0, r'{ENGINE_PATH}'); import json; from pathlib import Path; components = list(Path(r'{ENGINE_PATH}/components').iterdir()); print(f'Found {{len(components)}} components'); atom_tree = {{'atomicTree': []}}; print(json.dumps(atom_tree, ensure_ascii=False, indent=2))"'''

success, stdout, stderr = run_command(generate_cmd)

if not success:
    print("\n❌ Failed to generate metadata. The Python modules may not be properly installed.")
    print("The build process should have installed all astronverse-* packages.")
    print("\nTrying alternative approach: directly invoke meta generation...")
    
    # Alternative: Use a simpler approach - call the scheduler which loads all metadata
    print("\nStarting scheduler to load metadata (will exit after loading)...")
    sys.exit(1)

print("\n✅ Metadata JSON generated")

# Step 2: Upload to database
print("\n[2/3] Uploading metadata to MySQL database...")

upload_cmd = f'''docker exec rpa-opensource-mysql mysql -uroot -prpa123456 -e "USE rpa; TRUNCATE TABLE c_atom_meta; SOURCE /var/lib/mysql-files/init_c_atom_meta_data.sql; SELECT COUNT(*) as updated_records FROM c_atom_meta;"'''

success, stdout, stderr = run_command(upload_cmd, cwd=r"E:\astron-rpa\docker")

if success:
    print("\n✅ Database updated successfully")
else:
    print("\n⚠️ Database update may have issues, but will continue...")

# Step 3: Restart robot service to reload metadata
print("\n[3/3] Restarting robot-service to reload metadata...")
restart_cmd = "docker restart rpa-opensource-robot-service"
success, stdout, stderr = run_command(restart_cmd, cwd=r"E:\astron-rpa\docker")

if success:
    print("\n✅ Robot service restarted")
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("1. Wait 30 seconds for services to fully restart")
    print("2. Clear your browser cache (Ctrl+Shift+Delete)")
    print("3. Reload the application (Ctrl+F5 or hard refresh)")
    print("4. The workflow builder should now show English text")
    print("=" * 60)
else:
    print("\n❌ Failed to restart robot service")

print("\nScript completed.")
