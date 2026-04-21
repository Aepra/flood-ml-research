# 🌊 Flood ML Research - Quick Start Guide

## ⚡ SIMPLEST SETUP (Recommended)

### Step 1: Clone Project
```bash
git clone https://github.com/Aepra/flood-ml-research.git
cd flood-ml-research
```

### Step 2: Run ONE Command
```bash
# Windows
docker-compose up

# Linux/Mac
docker-compose up
```

**That's it!** ✅

Wait for:
```
flood-ml  | http://127.0.0.1:8888/lab?token=xxxxx
```

### Step 3: Open Jupyter Lab
Copy the URL above and paste in browser. Done! 🎉

---

## 📋 What Happens Automatically

When you run `docker-compose up`:

1. ✅ Downloads Python 3.11 image (~500MB, first time only)
2. ✅ Installs ALL packages from `requirements.txt` automatically
3. ✅ Setup geospatial libraries (GDAL, Proj, etc)
4. ✅ Starts Jupyter Lab on port 8888
5. ✅ Mounts your data/notebooks folders
6. ✅ **Everything ready to use!**

---

## 🚀 Run Your Notebooks

1. Open Jupyter Lab (link from step 2)
2. Navigate to `notebooks/`
3. Open any `.ipynb` file
4. **Kernel is already set** - just click Run!
5. All modules available ✅

---

## 📁 Files Your Computer Saves

```
flood-ml-research/
├── data/              ← Your data (persistent)
├── results/           ← Your results (persistent)
├── notebooks/         ← Your notebooks (persistent)
└── models/            ← Your models (persistent)
```

**Everything else in Docker container** - won't clutter your computer!

---

## 🛑 Stop Jupyter

Press `Ctrl+C` in terminal

Or run:
```bash
docker-compose down
```

---

## ⚠️ If Port 8888 is Busy

Edit `docker-compose.yml`, change:
```yaml
ports:
  - "8889:8888"  # Use port 8889 instead
```

Then access: `http://localhost:8889`

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Docker not installed | Download Docker Desktop from docker.com |
| Permission denied | Run as Admin (Windows) or use `sudo` (Linux/Mac) |
| Slow first time | Normal! Download + setup takes 5-10 min |
| Module not found | Restart container: `docker-compose down` then `docker-compose up` |
| Can't open http://localhost:8888 | Check token in terminal output |

---

## ✅ Prerequisites

- Docker Desktop installed (free)
- Git installed
- ~2GB free disk space

---

**That's all you need! No complex setup, no virtual environments, no remote containers.**

**Clone → docker-compose up → Done!** 🎉

---

## 📚 Advanced Options (Optional)

If you want more control, see [ADVANCED.md](ADVANCED.md)

---

Made with ❤️ for reproducible research
