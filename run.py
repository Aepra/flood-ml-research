#!/usr/bin/env python3
"""
Interactive runner for Flood ML Research project with Docker
One command to run everything!
"""

import os
import subprocess
import sys
import platform
from pathlib import Path

def print_banner():
    print("\n" + "="*60)
    print("🌊 FLOOD ML RESEARCH - Interactive Runner")
    print("="*60 + "\n")

def get_notebooks():
    """Get list of available Jupyter notebooks"""
    notebooks_dir = Path("notebooks")
    if not notebooks_dir.exists():
        return []
    return sorted([f.name for f in notebooks_dir.glob("*.ipynb") if not f.name.startswith(".")])

def get_scripts():
    """Get list of available Python scripts"""
    scripts_dir = Path("src")
    if not scripts_dir.exists():
        return []
    return sorted([f.name for f in scripts_dir.rglob("*.py") if not f.name.startswith("__")])

def check_docker():
    """Check if docker-compose is available"""
    result = subprocess.run(
        ["docker-compose", "--version"],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("❌ ERROR: Docker Compose tidak terinstall!")
        print("Install Docker Desktop dari: https://www.docker.com/products/docker-desktop")
        sys.exit(1)
    print(f"✅ {result.stdout.strip()}\n")

def start_container():
    """Start Docker container if not running"""
    print("🚀 Memulai container Docker...\n")
    result = subprocess.run(
        ["docker-compose", "up", "-d", "--build"],
        capture_output=False,
        text=True
    )
    if result.returncode != 0:
        print("❌ Gagal start container!")
        sys.exit(1)
    print("\n✅ Container siap!\n")

def run_notebook(notebook_name):
    """Execute Jupyter notebook"""
    print(f"\n📓 Menjalankan notebook: {notebook_name}\n")
    cmd = [
        "docker-compose", "exec", "-T", "flood-ml",
        "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        f"notebooks/{notebook_name}",
        "--output", f"notebooks/outputs/{notebook_name}"
    ]
    subprocess.run(cmd)

def run_script(script_path):
    """Execute Python script"""
    print(f"\n🐍 Menjalankan script: {script_path}\n")
    cmd = ["docker-compose", "exec", "-T", "flood-ml", "python", script_path]
    subprocess.run(cmd)

def open_jupyter():
    """Get Jupyter Lab URL"""
    print("\n🔗 Membuka Jupyter Lab...\n")
    cmd = ["docker-compose", "logs", "flood-ml"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Find token in logs
    for line in result.stdout.split("\n"):
        if "token=" in line and "http" in line:
            print(f"✅ Copy & paste URL ini di browser:\n")
            print(line.strip())
            return
    print("⚠️  Buka: http://localhost:8888")

def find_vscode():
    """Find VS Code installation path"""
    system = platform.system()
    
    if system == "Windows":
        # Common VS Code paths on Windows
        paths = [
            "C:\\Program Files\\Microsoft VS Code\\bin\\code.cmd",
            "C:\\Program Files (x86)\\Microsoft VS Code\\bin\\code.cmd",
            os.path.expanduser("~\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code.cmd"),
        ]
        
        # Try each path
        for path in paths:
            if os.path.exists(path):
                return path
        
        # Try to find via command
        try:
            result = subprocess.run(["where", "code"], capture_output=True, text=True, check=True)
            return result.stdout.strip().split('\n')[0]
        except:
            pass
    
    else:  # Linux/Mac
        try:
            result = subprocess.run(["which", "code"], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except:
            pass
    
    return None

def open_vscode_remote():
    """Open VS Code with Remote Container extension"""
    print("\n🔌 Membuka VS Code dengan remote container...\n")
    
    # Find VS Code
    code_path = find_vscode()
    
    if not code_path:
        print("❌ VS Code tidak ditemukan di PATH!")
        print("\n📝 Solusi:")
        print("  1. Pastikan VS Code sudah ter-install")
        print("  2. Restart komputer (agar PATH ter-update)")
        print("  3. Atau buka VS Code secara manual:")
        print("     - Buka folder project di VS Code")
        print("     - Ctrl+Shift+P → 'Remote-Containers: Reopen in Container'")
        return False
    
    # Open with remote container
    try:
        subprocess.Popen([code_path, "."])
        print("✅ VS Code terbuka!")
        return True
    except Exception as e:
        print(f"⚠️  Tidak bisa membuka VS Code otomatis: {e}")
        print("\n💡 Buka VS Code manual:")
        print("   - Buka folder project di VS Code")
        print("   - Ctrl+Shift+P → 'Remote-Containers: Reopen in Container'")
        return False

def interactive_menu():
    """Show interactive menu"""
    print_banner()
    check_docker()
    
    notebooks = get_notebooks()
    scripts = get_scripts()
    
    print("Pilih aksi:\n")
    print("1️⃣  Buka VS Code + Remote Container + Jupyter kernel")
    print("2️⃣  Start container & buka Jupyter Lab (Browser)")
    print("3️⃣  Jalankan notebook")
    print("4️⃣  Jalankan Python script")
    print("5️⃣  Stop container")
    print("6️⃣  Keluar\n")
    
    choice = input("Pilihan (1-6): ").strip()
    
    if choice == "1":
        start_container()
        print("\n✅ Container siap!")
        result = open_vscode_remote()
        if result:
            print("✨ VS Code dengan remote container terbuka!")
            print("📝 Tunggu beberapa saat hingga extension ter-install...")
            print("💡 Setelah selesai, pilih kernel: Ctrl+Shift+P → 'Jupyter: Select Kernel'")
        else:
            print("\n💡 Setup manual:")
            print("   1. Buka folder project ini di VS Code")
            print("   2. Ctrl+Shift+P → 'Remote-Containers: Reopen in Container'")
            print("   3. Tunggu container ter-attach")
            print("   4. Buka notebook dan pilih kernel!")
        
    elif choice == "2":
        start_container()
        open_jupyter()
        print("\n✨ Jupyter Lab siap! Buka URL di browser Anda.\n")
        
    elif choice == "3":
        if not notebooks:
            print("❌ Tidak ada notebook ditemukan!")
            return
        print("\nNotebook yang tersedia:\n")
        for i, nb in enumerate(notebooks, 1):
            print(f"{i}. {nb}")
        print()
        nb_choice = input("Pilih notebook (nomor): ").strip()
        try:
            notebook = notebooks[int(nb_choice) - 1]
            run_notebook(notebook)
            print(f"\n✅ Notebook selesai! Output tersimpan di notebooks/outputs/{notebook}\n")
        except (ValueError, IndexError):
            print("❌ Pilihan tidak valid!")
            
    elif choice == "4":
        if not scripts:
            print("❌ Tidak ada script ditemukan!")
            return
        print("\nScript yang tersedia:\n")
        for i, script in enumerate(scripts, 1):
            print(f"{i}. {script}")
        print()
        script_choice = input("Pilih script (nomor): ").strip()
        try:
            script = scripts[int(script_choice) - 1]
            run_script(f"src/{script}")
            print(f"\n✅ Script selesai!\n")
        except (ValueError, IndexError):
            print("❌ Pilihan tidak valid!")
            
    elif choice == "5":
        print("\n⏹️  Menghentikan container...\n")
        subprocess.run(["docker-compose", "down"])
        print("✅ Container dihentikan!\n")
        
    elif choice == "6":
        print("👋 Bye!\n")
        sys.exit(0)
    else:
        print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    try:
        interactive_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Dibatalkan!\n")
        sys.exit(0)
