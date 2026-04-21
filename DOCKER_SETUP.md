# Docker Setup Guide

## 🚀 **SUPER QUICK START** (1 Perintah!)

### Di Komputer Lain:

```bash
git clone https://github.com/YOUR_USERNAME/flood-ml-research.git
cd flood-ml-research

# Windows
run.bat

# Linux/Mac
./run.sh
```

**Itu saja!** ✨ Menu interaktif akan muncul dengan opsi pilihan.

---

## 🎯 **RECOMMENDED: VS Code + Remote Container**

1️⃣ Install VS Code extension: **"Remote - Containers"** (ms-vscode-remote.remote-containers)

2️⃣ Jalankan:
```bash
run.bat
```

3️⃣ Pilih **Opsi 1**: "Buka VS Code + Remote Container + Jupyter kernel"

4️⃣ VS Code akan auto-open dengan:
- ✅ Python kernel dari container
- ✅ Semua module terinstall
- ✅ Siap edit & run notebook

5️⃣ Buka notebook → pilih kernel (Ctrl+Shift+P) → langsung jalankan!

---

## 📋 Menu Interaktif Pilihan

```
1️⃣  Buka VS Code + Remote Container + Jupyter kernel  ← RECOMMENDED!
2️⃣  Start container & buka Jupyter Lab (Browser)
3️⃣  Jalankan notebook
4️⃣  Jalankan Python script
5️⃣  Stop container
6️⃣  Keluar
```

---

## **Opsi 1: VS Code (RECOMMENDED) ✅**

### Setup (sekali saja):
1. Install VS Code
2. Install extension: **"Remote - Containers"** (ID: ms-vscode-remote.remote-containers)

### Jalankan:
```bash
run.bat
→ Pilih 1
→ VS Code otomatis buka
```

### Kernel di VS Code:
```
Ctrl+Shift+P → "Jupyter: Select Kernel"
→ Pilih "Python 3.11.X (container)"
→ Kernel dari container sudah ready!
```

### Keuntungan:
- ✅ Edit + Run di VS Code
- ✅ Kernel dari container (semua module ada)
- ✅ Intellisense bekerja
- ✅ Debug support
- ✅ Git integration

---

## **Opsi 2: Jupyter Lab (Browser)**

```bash
run.bat
→ Pilih 2
→ Copy URL & buka di browser
```

Keuntungan:
- ✅ Tidak perlu install VS Code extension
- ✅ Simple & reliable
- ✅ Jupyter Lab UI yang familiar

---

## 🔧 Manual Commands (Optional)

Jika ingin manual control:

```bash
# Start container only
docker-compose up -d

# Stop container
docker-compose down

# Access container bash
docker-compose exec flood-ml bash

# Run specific notebook
docker-compose exec flood-ml jupyter nbconvert --to notebook --execute notebooks/00a_grid_generation.ipynb

# Run specific script
docker-compose exec flood-ml python src/main.py
```

---

## 📂 Output Files

- Notebook hasil execute tersimpan di: `notebooks/outputs/`
- Results tersimpan di: `results/`
- Models tersimpan di: `models/`

---

## ✅ Prerequisites

- Docker Desktop installed
- Git installed
- ~5GB disk space (untuk docker image + data)

---

## ⚠️ Troubleshooting

| Error | Solusi |
|-------|--------|
| Port 8888 used | Edit docker-compose.yml port |
| Permission denied | `chmod +x run.sh` (Linux/Mac) |
| Docker not found | Install Docker Desktop |
| Build error | Pastikan internet stabil, coba ulang |

---

**Happy researching! 🌊**
