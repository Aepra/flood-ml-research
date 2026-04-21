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

**Itu saja!** ✨ Menu interaktif akan muncul, pilih apa yang mau dijalankan.

---

## 📋 Menu Interaktif Pilihan

```
1️⃣  Start container & buka Jupyter Lab
2️⃣  Jalankan notebook (.ipynb)
3️⃣  Jalankan Python script (.py)
4️⃣  Stop container
5️⃣  Keluar
```

### Contoh:
- **Pilih 1** → Docker start + Jupyter Lab link
- **Pilih 2** → Pilih notebook → auto execute
- **Pilih 3** → Pilih script → auto execute

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
