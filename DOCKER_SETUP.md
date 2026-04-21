# Setup Guide - Docker or Virtual Environment

## 🚀 **Option 1: Virtual Environment (RECOMMENDED - Simpler)**

### Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/flood-ml-research.git
cd flood-ml-research

# Windows
setup_env.bat

# Linux/Mac
./setup_env.sh
```

**⏳ Wait 5-10 minutes** (first time only - installs all packages)

Then run:

```bash
run.bat    # Windows
./run.sh   # Linux/Mac
```

**Menu will appear:**
```
1️⃣  Start Jupyter Lab
2️⃣  Run notebook
3️⃣  Run Python script
5️⃣  Exit
```

### What happens?
- ✅ Creates `research-env/` folder with Python environment
- ✅ Installs all packages from `requirements.txt`
- ✅ Kernel name: `Python (research-env)`
- ✅ **No Docker needed!**

---

## 🐳 **Option 2: Docker (If you prefer)**

```bash
git clone https://github.com/YOUR_USERNAME/flood-ml-research.git
cd flood-ml-research

# Windows
run.bat
# Then choose: Setup Docker option

# Linux/Mac
./run.sh
```

See [DOCKER_LEGACY.md](DOCKER_LEGACY.md) for full Docker setup.

---

## 📋 Which option to choose?

| Feature | Virtual Env | Docker |
|---------|-------------|--------|
| Setup time | 5-10 min | 15-30 min |
| Disk space | ~500MB | ~1-2GB |
| Complexity | Simple | Medium |
| Reproducibility | Good | Excellent |
| Remote work | ✅ | ✅ |
| Recommended | ⭐⭐⭐ | ⭐⭐ |

---

## 🐍 Virtual Environment Details

### Folder structure
```
research-env/
├── Scripts/          # Windows executables
├── bin/              # Linux/Mac executables
├── Lib/              # Python packages
└── pyvenv.cfg
```

### Activate manually (optional)
```bash
# Windows
research-env\Scripts\activate.bat

# Linux/Mac
source research-env/bin/activate

# Then run Python
python main.py
```

### Deactivate
```bash
deactivate
```

### Delete environment
```bash
# Windows
rmdir /s research-env

# Linux/Mac
rm -rf research-env
```

---

## 🔧 Troubleshooting

### "ModuleNotFoundError" when running notebook
- Make sure `research-env/` folder exists
- Run `setup_env.bat` again
- Check kernel is set to `Python (research-env)`

### GDAL/geospatial library errors (Windows)
- These may fail on Windows - use Docker instead
- Or install system packages manually

### Port 8888 already in use
- Change port in run.py
- Or stop other Jupyter instances

---

**Happy coding! 🌊**
