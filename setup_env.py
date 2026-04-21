#!/usr/bin/env python3
"""
Setup Python virtual environment for Flood ML Research
Creates 'research-env' and installs all dependencies
"""

import os
import sys
import subprocess
import platform

def print_banner():
    print("\n" + "="*60)
    print("🌊 FLOOD ML RESEARCH - Environment Setup")
    print("="*60 + "\n")

def create_venv():
    """Create virtual environment"""
    env_name = "research-env"
    
    print(f"📦 Creating virtual environment: {env_name}...\n")
    
    try:
        subprocess.run([sys.executable, "-m", "venv", env_name], check=True)
        print(f"✅ Virtual environment '{env_name}' created!\n")
        return env_name
    except Exception as e:
        print(f"❌ Error creating virtual environment: {e}")
        sys.exit(1)

def get_activation_command(env_name):
    """Get activation command based on OS"""
    system = platform.system()
    
    if system == "Windows":
        return f"{env_name}\\Scripts\\activate.bat"
    else:  # Linux/Mac
        return f"source {env_name}/bin/activate"

def install_requirements(env_name):
    """Install requirements.txt in virtual environment"""
    print("📥 Installing Python packages...\n")
    print("⚠️  This may take 5-10 minutes (first time)...\n")
    
    system = platform.system()
    
    if system == "Windows":
        pip_path = f"{env_name}\\Scripts\\pip.exe"
    else:
        pip_path = f"{env_name}/bin/pip"
    
    try:
        # Upgrade pip
        subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
        
        # Install requirements
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        
        print("\n✅ All packages installed successfully!\n")
        return True
    except Exception as e:
        print(f"\n❌ Error installing packages: {e}")
        return False

def print_instructions(env_name):
    """Print usage instructions"""
    system = platform.system()
    
    print("="*60)
    print("✨ SETUP COMPLETE!")
    print("="*60)
    
    if system == "Windows":
        print("\n📝 To use this environment:\n")
        print("1. Activate environment:")
        print(f"   {env_name}\\Scripts\\activate.bat\n")
        print("2. Then run Jupyter:")
        print("   jupyter notebook\n")
        print("3. Or run run.bat (dari menu akan langsung pakai env ini)")
    else:
        print("\n📝 To use this environment:\n")
        print("1. Activate environment:")
        print(f"   source {env_name}/bin/activate\n")
        print("2. Then run Jupyter:")
        print("   jupyter notebook\n")
        print("3. Or run ./run.sh (dari menu akan langsung pakai env ini)")
    
    print("\n💡 Quick start:")
    print(f"   • Kernel name: Python (research-env)")
    print("   • Location: ./" + env_name)
    print("   • To deactivate: deactivate")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    print_banner()
    
    # Check if venv already exists
    if os.path.exists("research-env"):
        print("⚠️  'research-env' already exists!")
        response = input("Overwrite? (y/n): ").strip().lower()
        if response != 'y':
            print("Cancelled.\n")
            sys.exit(0)
        
        # Remove existing venv
        print("Removing existing environment...\n")
        if platform.system() == "Windows":
            os.system("rmdir /s /q research-env")
        else:
            os.system("rm -rf research-env")
    
    # Create environment
    env_name = create_venv()
    
    # Install requirements
    if install_requirements(env_name):
        print_instructions(env_name)
        print("🎉 Ready to use! Run: run.bat (or run.sh on Linux/Mac)\n")
    else:
        print("\n❌ Setup failed!\n")
        sys.exit(1)
