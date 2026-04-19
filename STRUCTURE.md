# 📋 Struktur Project: Flood ML Research

## 🎯 Project Overview
Penelitian tentang **generalisasi dan bias spasial** model machine learning untuk prediksi banjir menggunakan data geospasial.

**Focus Area**: Makassar (training) → Jakarta (testing cross-region validation)

---

## 📂 Struktur Direktori dan File

### 📁 `data/` - Data Storage
Penyimpanan data dalam berbagai tahap pemrosesan.

```
data/
├── raw/              # Data mentah dari berbagai sumber
│                     # - CHIRPS (rainfall)
│                     # - SRTM (elevation/DEM)
│                     # - ESA WorldCover (land use)
│                     # - OpenStreetMap (river data)
│
├── processed/        # Data yang sudah dibersihkan & siap untuk modeling
│                     # - Cleaned datasets
│                     # - Normalized features
│                     # - Train-test splits
│
└── external/         # Data eksternal tambahan
                      # - Reference data
                      # - Auxiliary information
```

**Purpose**: Memisahkan data dalam berbagai tahap memudahkan tracking dan reproducibility.

---

### 📁 `src/` - Source Code (Core Logic)
Kode utama project yang dapat digunakan kembali (reusable).

```
src/
├── data/             # Data loading & processing pipelines
│                     # - load_raw_data()
│                     # - preprocess()
│                     # - handle_missing_values()
│
├── features/         # Feature engineering
│                     # - calculate_slope()
│                     # - compute_distance_to_river()
│                     # - aggregate_rainfall()
│                     # - encode_landuse()
│
├── models/           # Model definitions & training
│                     # - RandomForest implementation
│                     # - XGBoost implementation
│                     # - Model training logic
│
└── visualization/    # Plotting & visual analysis
                      # - plot_performance()
                      # - plot_feature_importance()
                      # - plot_error_distribution()
                      # - plot_flood_risk_maps()
```

**Purpose**: Modularisasi kode untuk maintainability dan reusability.

---

### 📁 `models/` - Model Artifacts
Penyimpanan model yang sudah dilatih dan artifacts.

```
models/
├── baseline/         # Model in-domain (trained on Makassar)
├── generalization/   # Model untuk OOD testing (trained on Makassar, test Jakarta)
├── spatial_bias/     # Model untuk spatial bias testing
│                     # - Model dengan lat/lon
│                     # - Model tanpa lat/lon
└── checkpoints/      # Training checkpoints & intermediate states
```

**Purpose**: Memudahkan loading model untuk inference dan analisis tanpa perlu retrain.

---

### 📁 `notebooks/` - Jupyter Notebooks
Notebooks untuk eksplorasi, eksperimen, dan dokumentasi interaktif.

**Typical contents:**
- `01_eda.ipynb` - Exploratory Data Analysis
- `02_preprocessing.ipynb` - Data preprocessing steps
- `03_feature_engineering.ipynb` - Feature creation & analysis
- `04_baseline_model.ipynb` - Baseline model training
- `05_generalization_test.ipynb` - Cross-region testing
- `06_spatial_bias_analysis.ipynb` - Spatial bias experiments
- `07_error_analysis.ipynb` - Detailed error investigation

---

### 📁 `results/` - Experiment Results
Output dari eksperimen dan analisis.

```
results/
├── figures/          # Visualisasi hasil
│                     # - Performance plots
│                     # - Feature importance charts
│                     # - Confusion matrices
│                     # - Flood risk maps
│
└── metrics/          # Performance metrics & statistics
                      # - accuracy, precision, recall, F1
                      # - ROC-AUC scores
                      # - Cross-region performance drops
                      # - Spatial error distributions
```

**Purpose**: Dokumentasi hasil eksperimen untuk referensi dan publikasi.

---

### 📁 `docs/` - Documentation
Dokumentasi penelitian dan teknis.

```
docs/
├── research_proposal.md    # Detailed research plan
│                           # - Research questions
│                           # - Hypotheses
│                           # - Experimental design
│                           # - Methodology
│
└── [future]
    ├── METHODOLOGY.md      # Detailed technical methodology
    ├── RESULTS.md          # Results summary
    └── FINDINGS.md         # Key findings & insights
```

---

### 📄 Root Level Files

#### `main.py`
**Entry point** untuk menjalankan pipeline project.

Typical structure:
```python
if __name__ == "__main__":
    # 1. Load data
    # 2. Preprocess
    # 3. Feature engineering
    # 4. Train baseline model
    # 5. Run experiments
    # 6. Generate results
```

#### `README.md`
Overview project dengan:
- Deskripsi umum
- Setup instructions
- Usage guide
- Dependencies
- Study areas

#### `requirements.txt`
Python dependencies:
- `pandas`, `numpy` - Data manipulation
- `scikit-learn` - ML models & evaluation
- `xgboost` - Gradient boosting
- `geopandas`, `rasterio` - Geospatial processing
- `matplotlib` - Visualization

#### `.gitignore` & `.git/`
Git configuration untuk version control.

---

## 🔄 Data Flow Pipeline

```
raw data (CHIRPS, SRTM, ESA, OSM)
         ↓
     [src/data]  ← load & clean
         ↓
   data/processed
         ↓
  [src/features] ← feature engineering
         ↓
  feature vectors
         ↓
   [src/models]  ← training & evaluation
         ↓
  models/ (artifacts)
         ↓
 [src/visualization] + results/
         ↓
  figures & metrics
```

---

## 🧪 Experiment Structure

### 1. **Baseline Performance** (in-domain)
- Train: Makassar
- Test: Makassar
- Location: `notebooks/04_baseline_model.ipynb`
- Output: `results/metrics/baseline_performance.json`

### 2. **Generalization Test** (out-of-domain)
- Train: Makassar
- Test: Jakarta
- Location: `notebooks/05_generalization_test.ipynb`
- Output: `results/metrics/ood_performance.json`

### 3. **Spatial Bias Test** (critical experiment)
- Model A: with lat/lon
- Model B: without lat/lon
- Location: `notebooks/06_spatial_bias_analysis.ipynb`
- Output: `results/metrics/spatial_bias_results.json`

### 4. **Error Analysis**
- False Positive / False Negative patterns
- Spatial error distribution
- Location: `notebooks/07_error_analysis.ipynb`
- Output: `results/figures/error_distribution_map.png`

---

## 🛠️ Common Workflows

### Running the Full Pipeline
```bash
python main.py
```

### Running Individual Experiments
```bash
jupyter notebook notebooks/05_generalization_test.ipynb
```

### Adding New Features
1. Add code to `src/features/`
2. Test in `notebooks/03_feature_engineering.ipynb`
3. Integrate into `main.py`

### Adding New Model
1. Define in `src/models/`
2. Test in `notebooks/04_baseline_model.ipynb`
3. Compare performance with existing models

---

## 📊 Output Locations

| Output Type | Location | Example |
|---|---|---|
| Model artifacts | `models/` | `baseline_rf_makassar.pkl` |
| Performance metrics | `results/metrics/` | `accuracy_ood.json` |
| Visualizations | `results/figures/` | `feature_importance.png` |
| Analysis notebooks | `notebooks/` | `06_spatial_bias_analysis.ipynb` |
| Raw data | `data/raw/` | `makassar_rainfall.tif` |
| Processed data | `data/processed/` | `dataset_train.csv` |

---

## 🎓 Key Research Focus Areas

1. **Generalization** - Performance in-domain vs out-of-domain
2. **Spatial Bias** - Model dependence on location vs physical features
3. **Feature Importance** - Which features actually matter
4. **Error Analysis** - When and why models fail
5. **Robustness** - Sensitivity to data variations

---

## 📝 Notes

- Follow consistent naming conventions for models and datasets
- Document all preprocessing steps for reproducibility
- Store large files (.tif, .pkl) appropriately; use `.gitignore` to exclude them
- Results should be reproducible from raw data
- Update documentation as project evolves
