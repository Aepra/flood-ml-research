#!/usr/bin/env python3
"""
Interactive runner for Flood ML Research
Supports both Virtual Environment and Docker modes
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

def check_venv():
    """Check if research-env virtual environment exists"""
    return os.path.exists("research-env")

def check_docker():
    """Check if docker-compose is available"""
    result = subprocess.run(["docker-compose", "--version"], capture_output=True, text=True)
    return result.returncode == 0

def get_python_executable():
    """Get Python executable from virtual environment"""
    system = platform.system()
    
    if check_venv():
        if system == "Windows":
            return "research-env\\Scripts\\python.exe"
        else:
            return "research-env/bin/python"
    return sys.executable

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

def run_jupyter():
    """Start Jupyter Lab"""
    python_exe = get_python_executable()
    print("\n🚀 Starting Jupyter Lab...\n")
    print("📝 Opening http://localhost:8888 in your browser...\n")
    subprocess.run([python_exe, "-m", "jupyter", "lab", "--ip=127.0.0.1", "--port=8888"])

def run_notebook(notebook_name):
    """Execute Jupyter notebook"""
    python_exe = get_python_executable()
    print(f"\n📓 Running notebook: {notebook_name}\n")
    cmd = [
        python_exe, "-m", "jupyter", "nbconvert",
        "--to", "notebook",
        "--execute",
        f"notebooks/{notebook_name}",
        "--output", f"notebooks/outputs/{notebook_name}"
    ]
    subprocess.run(cmd)

def run_script(script_path):
    """Execute Python script"""
    python_exe = get_python_executable()
    print(f"\n🐍 Running script: {script_path}\n")
    subprocess.run([python_exe, script_path])

def interactive_menu():
    """Main interactive menu"""
    print_banner()
    
    has_venv = check_venv()
    has_docker = check_docker()
    
    if not has_venv and not has_docker:
        print("⚠️  No environment found!\n")
        print("Setup options:\n")
        print("1️⃣  Create virtual environment (recommended)")
        print("2️⃣  Setup Docker\n")
        choice = input("Choose (1-2): ").strip()
        if choice == "1":
            subprocess.run([sys.executable, "setup_env.py"])
        return
    
    notebooks = get_notebooks()
    scripts = get_scripts()
    
    if has_venv:
        print("✅ Virtual Environment detected (research-env)\n")
    elif has_docker:
        print("✅ Docker detected\n")
    
    print("Menu:\n")
    print("1️⃣  Start Jupyter Lab")
    print("2️⃣  Run notebook")
    print("3️⃣  Run Python script")
    if not has_venv:
        print("4️⃣  Create virtual environment")
    print("5️⃣  Exit\n")
    
    choice = input("Choose (1-5): ").strip()
    
    if choice == "1":
        run_jupyter()
        
    elif choice == "2":
        if not notebooks:
            print("❌ No notebooks found!")
            return
        print("\nAvailable notebooks:\n")
        for i, nb in enumerate(notebooks, 1):
            print(f"{i}. {nb}")
        nb_idx = input("\nSelect (number): ").strip()
        try:
            notebook = notebooks[int(nb_idx) - 1]
            run_notebook(notebook)
            print(f"\n✅ Done! Output: notebooks/outputs/{notebook}\n")
        except (ValueError, IndexError):
            print("❌ Invalid choice!")
            
    elif choice == "3":
        if not scripts:
            print("❌ No scripts found!")
            return
        print("\nAvailable scripts:\n")
        for i, script in enumerate(scripts, 1):
            print(f"{i}. {script}")
        script_idx = input("\nSelect (number): ").strip()
        try:
            script = scripts[int(script_idx) - 1]
            run_script(f"src/{script}")
            print("\n✅ Done!\n")
        except (ValueError, IndexError):
            print("❌ Invalid choice!")
    
    elif choice == "4":
        print("\n🔧 Setting up environment...\n")
        subprocess.run([sys.executable, "setup_env.py"])
        
    elif choice == "5":
        print("👋 Bye!\n")
        sys.exit(0)

if __name__ == "__main__":
    try:
        interactive_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Cancelled!\n")
        sys.exit(0)
