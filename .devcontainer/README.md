# 🌊 Flood ML Research - VS Code Setup

## ⚡ Super Simple Setup (2 steps)

### Step 1: Install VS Code Extension

Open VS Code, go to Extensions, search for:
```
Dev Containers
```

Install: **"Dev Containers"** by Microsoft (ms-vscode-remote.remote-containers)

### Step 2: Open Project in VS Code

```bash
git clone https://github.com/Aepra/flood-ml-research.git
cd flood-ml-research

code .
```

**VS Code will ask:** "Reopen in Dev Container?"

**Click:** "Reopen in Container"

---

## ⏳ Wait (First Time Only)

- 🔄 Building container... (~3-5 minutes)
- 📥 Installing Python packages... (~5 minutes)
- ✅ Done!

**Next time:** ~10 seconds (container already built)

---

## 🎯 Run Your Notebook

1. **Open** `notebooks/` folder in Explorer
2. **Click** on any `.ipynb` file
3. **Select Kernel:**
   - Press `Ctrl+Shift+P`
   - Type `Python: Select Interpreter`
   - Choose `Python (from container)` 
4. **Click** ▶️ Run Cell (or Run All)

**All modules available!** ✅

---

## 🔍 How to Know It's Working

Look at **bottom-left corner** of VS Code:

```
><><  (green icon)
Dev Container: Flood ML Research
```

If you see that = ✅ **Container is connected!**

---

## 📝 Edit & Run Code

Everything works like normal VS Code:

- ✅ Edit notebooks
- ✅ Edit Python files
- ✅ Run cells
- ✅ See outputs in notebook
- ✅ Intellisense works
- ✅ Debugger works
- ✅ Git integration works

---

## 🛑 Stop Container

**Option A:** Close VS Code

**Option B:** Run in terminal:
```bash
docker-compose down
```

Your data/notebooks are **NOT deleted** - they're on your computer!

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| **"Dev Containers not found"** | Install extension (see Step 1) |
| **"Reopen in Container" not appearing** | Restart VS Code |
| **Kernel not showing Python option** | Wait for container to fully load (check bottom-left) |
| **Module errors** | Container still building, wait 1-2 more minutes |
| **Port 8888 in use** | Edit `docker-compose.yml`, change 8888 → 8889 |

---

## 💡 Pro Tips

### Run Jupyter Lab (if you want)
```bash
# In VS Code terminal (inside container):
jupyter lab --ip=0.0.0.0 --port=8888
```

Open browser → `http://localhost:8888`

### Access Terminal in Container
```
Ctrl+Shift+`  (backtick)
```

Now you have bash terminal **inside the container**!

### Install New Packages
```bash
pip install package-name
```

(In container terminal - it saves automatically)

---

## ✅ That's All You Need!

1. ✅ Install VS Code + Dev Containers extension
2. ✅ `code .` to open project
3. ✅ Reopen in container
4. ✅ Open notebook
5. ✅ Select kernel
6. ✅ Run!

---

**No Docker commands needed. No manual setup. Just VS Code as usual!** 🎉

---

See also: [README.md](../README.md) for other options
