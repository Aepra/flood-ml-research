# A Diagnostic Framework for Quantifying Spatio-Temporal Shortcut Learning in Machine Learning-Based Flood Prediction Under Cross-Regional and Temporal Distribution Shifts

**Status:** 🚧 In Development | **Target:** Q1 Conference/Journal

---

## 📋 Quick Navigation

- **[Research Proposal](docs/research_proposal.md)** — Full research methodology & framework
- **[Dataset Specification](docs/DATASET_SPECIFICATION.md)** — Technical dataset details (ST-FSLD v1.0)
- **[Project Structure](STRUCTURE.md)** — Directory organization & workflows
- **[Data Sources](docs/research_proposal.md#7-data-sources)** — CHIRPS, SRTM, ESA WorldCover, OpenStreetMap, Sentinel-1

---

## 🎯 Research Overview

### The Core Question

> **Do machine learning flood prediction models learn physical hydrological processes, or do they rely on spatio-temporal shortcuts such as location memorization and seasonal patterns?**

This is not a predictive modeling study. It is a **diagnostic framework** to quantify shortcut learning under distribution shift.

---

## 🔬 Research Framework

### Problem Statement

High in-domain accuracy in flood prediction models does not guarantee that models learn physically meaningful processes. Models may instead rely on:

- **Geographic encoding** (lat/lon memorization)
- **Regional rainfall patterns** (co-occurrence shortcuts)
- **Temporal seasonality** (time-based leakage)

**Literature gap:** No standardized quantitative framework exists to measure shortcut learning in geospatial ML.

---

## 🎓 Research Objectives

### Main Objective
To develop a diagnostic framework for quantifying spatio-temporal shortcut learning in flood prediction models under distribution shift.

### Specific Objectives
1. Quantify shortcut learning in in-domain and shifted settings
2. Measure degradation under spatial shift (Makassar → Jakarta)
3. Measure degradation under temporal shift (2018–2020 → 2021–2022)
4. Evaluate dependence on spatial proxy features (lat/lon)
5. Assess physical consistency of model predictions
6. Identify structured failure modes under distribution shift

---

## ❓ Research Questions

| # | Question | Focus |
|---|----------|-------|
| RQ1 | Do models rely on shortcuts even in-domain? | Baseline dependency |
| RQ2 | How much does spatial shift degrade performance? | Cross-regional generalization |
| RQ3 | Do models fail under temporal shift? | Temporal generalization |
| RQ4 | Do lat/lon dominate predictions? | Feature shortcut dominance |
| RQ5 | Do predictions violate hydrological relationships? | Physical consistency |
| RQ6 | Are failure patterns structured? | Failure mode taxonomy |

---

## 📊 Study Design

### Geographic Setup

| Region | Role | Coverage | Period |
|--------|------|----------|--------|
| **Makassar** | Training | 3,600 grid cells (250m × 250m) | 2018–2020 |
| **Jakarta** | Testing | 8,000 grid cells (250m × 250m) | 2021–2022 |

- **Coordinate system:** WGS84 + UTM 50S
- **Temporal resolution:** Daily observations
- **Total dataset:** ~9.8 million observations (~2.5 GB CSV)

---

## 🗂️ Dataset: ST-FSLD v1.0

**Spatio-Temporal Flood Shortcut Learning Dataset**

### Features (11 total)

**Environmental (from CHIRPS)**
- `rainfall` — Daily rainfall (mm)
- `rainfall_3day` — 3-day cumulative rainfall
- `rainfall_7day` — 7-day cumulative rainfall

**Topographic (from SRTM DEM)**
- `elevation` — Digital elevation model (m)
- `slope` — Terrain slope (degrees)

**Hydrological (from OpenStreetMap)**
- `distance_river` — Distance to nearest river (m)

**Land (from ESA WorldCover)**
- `landuse` — Land use classification

**Spatial (Diagnostic Features)**
- `lat` — Latitude (WGS84)
- `lon` — Longitude (WGS84)

### Target Variable

- `flood = 1` → Flood event (detected via Sentinel-1 SAR)
- `flood = 0` → Non-flood event
- **Class distribution:** ~11% floods, 89% non-floods (natural, unbalanced)

### Data Split Strategy

| Split Type | Train | Test |
|-----------|-------|------|
| **Spatial** | Makassar | Jakarta |
| **Temporal** | 2018–2020 | 2021–2022 |
| **Primary Key** | (lat, lon, date) | — |

**Why no balancing?** Class imbalance reflects real-world flood rarity. Balancing introduces artificial shortcuts.

---

## 🔧 Methodology

### Data Pipeline (6 Steps)

1. **Data Collection** — Multi-source geospatial datasets
2. **Flood Label Generation** — Sentinel-1 SAR backscatter analysis
3. **Preprocessing** — Spatial alignment, missing value handling, normalization
4. **Feature Engineering** — Rainfall aggregation, slope computation, distance calculation
5. **Model Training** — Random Forest, XGBoost
6. **Diagnostic Evaluation** — In-domain, spatial shift, temporal shift, feature ablation, physical consistency

---

## 🧪 Experimental Design: 4-Layer Evidence Framework

### LAYER 1 — Observational Baseline

| Experiment | Train | Test | Purpose |
|-----------|-------|------|---------|
| **1.1 In-Domain** | Makassar 2018–2020 | Makassar 2021–2022 | Establish baseline AUC ceiling |
| **1.2 Sub-Region Holdout** | Makassar 80% | Makassar 20% | Internal spatial validation |

### LAYER 2 — Natural Distribution Shift

| Experiment | Train | Test | Purpose |
|-----------|-------|------|---------|
| **2.1 Spatial Shift** | Makassar 2018–2020 | Jakarta 2021–2022 | Detect geographic memorization |
| **2.2 Temporal Shift** | Makassar 2018–2020 | Makassar 2021–2022 | Detect seasonal shortcuts |
| **2.3 Distance-Based Split** | Near cells | Far cells | Quantify AUC vs geographic distance |

### LAYER 3 — Intervention Experiments (Q1-Critical)

| Experiment | Method | Purpose |
|-----------|--------|---------|
| **3.1 Spatial Perturbation** | Add noise ±100m, ±1km, ±5km to lat/lon | Test sensitivity to coordinate shifts |
| **3.2 Spatial Shuffle** | Swap grid cells within/across regions | Isolate location encoding vs physics |
| **3.3 Feature Dose Test** | Full → No-Spatial → Spatial-Only → No-Physical | Measure feature importance via dose response |
| **3.4 Counterfactual Test** | Generate synthetic samples with modified features | Test model understanding of physical relationships |

### LAYER 4 — Counterfactual Logic Tests

| Experiment | Method | Purpose |
|-----------|--------|---------|
| **4.1 Monotonicity Test** | Verify physical laws (rainfall↑→flood↑, etc.) | Check % violations of hydrological rules |
| **4.2 Causal Consistency Score** | C = % predictions consistent with physics | Q1-key metric: C=100% (perfect) vs C<50% (shortcut) |

---

## 📐 Shortcut Learning Quantification

### Shortcut Learning Score

$$S = \frac{\text{AUC}_{\text{in-domain}} - \text{AUC}_{\text{shift}}}{\text{AUC}_{\text{in-domain}}}$$

### Decomposed Form

$$S = S_{\text{spatial}} + S_{\text{temporal}} + S_{\text{feature}}$$

- $S_{\text{spatial}}$ = degradation under regional shift
- $S_{\text{temporal}}$ = degradation under temporal shift
- $S_{\text{feature}}$ = degradation after removing spatial features

**Interpretation:**
- $S = 0$ → No shortcut learning
- $S > 0.3$ → Evidence of significant shortcut dependence
- $S > 0.5$ → Model relies predominantly on shortcuts

---

## 🚨 Failure Mode Taxonomy

| Type | Definition | Detection Signature |
|------|-----------|-------------------|
| **Spatial Memorization** | Over-reliance on lat/lon | High feature importance + spatial shift drop |
| **Temporal Shortcut** | Dependence on seasonal patterns | Performance drop across years |
| **Hydrological Inconsistency** | Violates physical relationships | Rainfall ↑ but flood ↓ |
| **Feature Proxy Dominance** | Non-physical features outweigh physical ones | lat/lon importance > rainfall importance |

---

## 🔍 Analysis Framework (3 Layers)

### Layer 1: Behavioral Shift
- Quantify performance degradation under spatial and temporal shifts
- Compare: in-domain AUC vs spatial shift AUC vs temporal shift AUC

### Layer 2: Shortcut Dependency
- SHAP-based feature importance analysis
- Ablation study (model with/without lat/lon)
- Measure importance gap between spatial and physical features

### Layer 3: Structural Failure Mechanisms
- Categorize prediction errors into failure modes
- Quantify frequency of each failure type
- Assess whether failures are random or structured

---

## 📈 Expected Findings

- ✓ Models exhibit spatio-temporal shortcut learning even in-domain
- ✓ Significant performance degradation under distribution shift
- ✓ Strong dependence on spatial proxy variables (lat/lon)
- ✓ Violations of expected hydrological consistency
- ✓ Structured failure patterns (not random errors)

---

## 🎁 Research Contributions

1. **Quantitative Framework** — First standardized metric for diagnosing shortcut learning in geospatial ML
2. **Evaluation Protocol** — Cross-regional and cross-temporal evaluation methodology
3. **Taxonomy** — Structured failure mode categorization for hydrological ML systems
4. **Empirical Evidence** — Demonstration that flood models rely on non-physical correlations under shift

---

## 📂 Project Structure

```
flood-ml-research/
├── README.md                          # This file
├── STRUCTURE.md                       # Detailed directory structure & workflows
├── main.py                            # Entry point
├── requirements.txt                   # Dependencies
│
├── docs/
│   ├── research_proposal.md          # Full research methodology
│   └── DATASET_SPECIFICATION.md      # Comprehensive dataset technical specs
│
├── data/
│   ├── raw/                          # Original data files
│   ├── processed/                    # Cleaned & preprocessed data
│   └── external/                     # External datasets (CHIRPS, SRTM, etc.)
│
├── src/
│   ├── data/                         # Data loading & preprocessing
│   ├── features/                     # Feature engineering
│   ├── models/                       # Model training & evaluation
│   └── visualization/                # Analysis plots & figures
│
├── models/                           # Trained model artifacts
│   ├── random_forest/
│   └── xgboost/
│
├── notebooks/                        # Jupyter notebooks for exploration
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_shortcut_analysis.ipynb
│   └── 05_failure_modes.ipynb
│
└── results/
    ├── metrics/                      # Quantitative results (CSV/JSON)
    │   ├── in_domain_baseline.csv
    │   ├── spatial_shift_test.csv
    │   ├── temporal_shift_test.csv
    │   ├── feature_importance.csv
    │   └── failure_modes.csv
    └── figures/                      # Publication-quality plots
        ├── shortcut_learning_score.png
        ├── performance_degradation.png
        ├── feature_dependency.png
        ├── physical_consistency.png
        └── failure_mode_distribution.png
```

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/your-repo/flood-ml-research.git
cd flood-ml-research

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Full Pipeline

```bash
# Data processing
python src/data/preprocess.py

# Feature engineering
python src/features/engineer.py

# Model training & evaluation (all 6 experiments)
python src/models/train.py --experiment all

# Generate diagnostic analysis
python src/models/evaluate.py --analysis shortcut_learning
```

### Run Individual Experiment

```bash
# In-domain baseline
python src/models/train.py --experiment 1

# Spatial shift test
python src/models/train.py --experiment 2

# Temporal shift test
python src/models/train.py --experiment 3

# Feature dependency (SHAP + ablation)
python src/models/train.py --experiment 4

# Physical consistency checks
python src/models/train.py --experiment 5

# Failure mode analysis
python src/models/train.py --experiment 6
```

---

## 📊 Workflow Phases

### Phase 1: Data Preparation ⏳
- Collect multi-source geospatial data
- Generate Sentinel-1 SAR-based flood labels
- Preprocess & align spatial datasets
- **Output:** Preprocessed dataset in `data/processed/`

### Phase 2: Feature Engineering ⏳
- Aggregate rainfall (3-day, 7-day windows)
- Compute topographic features (slope from DEM)
- Calculate hydrological features (distance to river)
- Encode land use classifications
- **Output:** Feature matrix in `data/processed/`

### Phase 3: Model Training ⏳
- Train Random Forest & XGBoost models
- Perform hyperparameter tuning
- Save trained models to `models/`
- **Output:** Model artifacts & training logs

### Phase 4: Diagnostic Evaluation ⏳
- Run 6 experiments (in-domain, spatial shift, temporal shift, ablation, consistency, failure modes)
- Compute Shortcut Learning Score (S)
- Generate feature importance (SHAP)
- Categorize failure modes
- **Output:** Metrics in `results/metrics/`

### Phase 5: Analysis & Visualization ✅
- Create publication-quality figures
- Generate summary statistics
- Write results & interpretation
- **Output:** Figures in `results/figures/`, manuscript draft

---

## ⚠️ Risks & Mitigation

### Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Noisy Sentinel-1 labels | Biased model training | Multi-source validation, manual verification |
| Class imbalance | Training instability | Use stratified sampling, focus on AUC metrics |
| Missing spatial data | Incomplete feature matrix | Interpolation, gap filling, exclude problematic cells |
| Computational complexity | Long pipeline runtime | Distributed processing, cloud computing |

---

## 🔗 Resources & References

### Data Sources
- **Rainfall:** [CHIRPS - Climate Hazards Group](https://www.chc.ucsb.edu/data/chirps) (NASA)
- **Elevation:** [SRTM DEM - USGS](https://earthexplorer.usgs.gov/) (30m resolution)
- **Land Use:** [ESA WorldCover](https://worldcover.org/) (10m resolution)
- **Rivers:** [OpenStreetMap](https://www.openstreetmap.org/) (vector network)
- **Flood Labels:** [Sentinel-1 SAR](https://sentinel.esa.int/web/sentinel/missions/sentinel-1) (Google Earth Engine)

### Key References

**Shortcut Learning in ML:**
- Geirhos et al. (2020) "Shortcut Learning in Deep Neural Networks"
- Jacobsen et al. (2019) "Excessive Invariance Hurts Interpretability"

**Geospatial ML & Distribution Shift:**
- Tuia et al. (2021) "Closing the Loop: A Review of Domain Adaptation"
- Robinson et al. (2019) "Spatial Data Augmentation for Deep Learning"

**Flood Prediction & SAR:**
- Martinis et al. (2018) "Flood Mapping from Synthetic Aperture Radar"
- Uddin et al. (2019) "Flood Risk Assessment Using SAR and Multispectral"

---

## 📝 Important Notes

### Design Philosophy

1. **Diagnostic, Not Operational** — This framework is for research understanding, not operational flood early warning
2. **Class Imbalance by Design** — Natural ~11% flood rate; no artificial balancing to avoid shortcuts
3. **Strict Temporal Split** — No data leakage; 2018–2020 training, 2021–2022 testing
4. **Spatial Features Are Intentional** — lat/lon included to detect memorization, not to improve predictions
5. **Multiple Distribution Shifts** — Tests both spatial AND temporal generalization

### Why NOT to Balance Classes

Balancing (50/50 flood/non-flood) would:
- Artificially inflate minority class representation
- Allow models to use spurious correlations
- Mask real generalization failures
- Obscure shortcut learning

We keep natural ~11% balance to force models to learn real patterns.

---

## 👥 Contributing

### For Researchers/Contributors

1. Read [research_proposal.md](docs/research_proposal.md) for full methodology
2. Read [DATASET_SPECIFICATION.md](docs/DATASET_SPECIFICATION.md) for data details
3. Check [STRUCTURE.md](STRUCTURE.md) for workflow
4. Follow code in `src/` directory for implementation

### For Reviewers/Evaluators

- **Quick overview:** This README (3 min read)
- **Detailed framework:** [research_proposal.md](docs/research_proposal.md) (15 min read)
- **Technical specs:** [DATASET_SPECIFICATION.md](docs/DATASET_SPECIFICATION.md) (20 min read)
- **Results:** See `results/metrics/` and `results/figures/`

---

## 📜 License

CC BY-SA 4.0 — Attribution required for academic use

---

## 📧 Contact & Citation

**Lead Researcher:** [Your Name]  
**Email:** [your.email@institution.edu]  
**Affiliation:** [Your Institution]

**Cite this project:**

```bibtex
@misc{flood_ml_shortcut_2026,
  author = {Your Name},
  title = {A Diagnostic Framework for Quantifying Spatio-Temporal Shortcut Learning 
           in Machine Learning-Based Flood Prediction},
  year = {2026},
  url = {https://github.com/your-repo/flood-ml-research}
}
```

---

## 🎯 Core Insight

> The hardest part of this research is not building a flood prediction model, but **rigorously quantifying what the model actually learns under distribution shift**.

This framework operationalizes that challenge into a standardized diagnostic protocol.

---

**Last updated:** April 2026 | **Version:** 1.0-diagnostic-framework
# 🌊 Flood Prediction ML Research

**Evaluating the Generalization, Temporal Dynamics, and Spatial Bias of Machine Learning Models for Flood Prediction Using Multi-Source Geospatial Data**

---

## 📌 Quick Links

- 📋 **Full Research Proposal**: [`docs/research_proposal.md`](docs/research_proposal.md)
- 📊 **Dataset Specification**: [`docs/DATASET_SPECIFICATION.md`](docs/DATASET_SPECIFICATION.md)
- 📁 **Project Structure**: [`STRUCTURE.md`](STRUCTURE.md)

---

## 🎯 Project Overview

This is a **research-driven project** (not an operational flood forecasting system) focused on a critical question:

> **Do machine learning models truly learn the physical processes of flooding, or do they rely on spatio-temporal shortcuts such as location and seasonal patterns?**

Unlike conventional flood prediction systems that optimize for accuracy, this study explicitly evaluates:
- ✅ **Spatial generalization** (Makassar → Jakarta)
- ✅ **Temporal robustness** (2018–2020 → 2021–2022)
- ✅ **Spatial bias detection** (reliance on coordinates)
- ✅ **Feature importance analysis** (physical vs spatial factors)
- ✅ **Failure patterns** (systematic errors under distribution shift)

---

## 🔬 Research Motivation

**Problem**: Most flood prediction models:
- ❌ Perform well locally but fail in new regions
- ❌ Overfit to spatial patterns (e.g., geographic coordinates)
- ❌ Don't generalize across time (different years or seasons)
- ❌ Lack transparency about what they actually learn

**Solution**: This project uses a **spatio-temporal experimental framework** to rigorously evaluate:
- Whether models learn physical flood processes
- How much models rely on "shortcuts" (location, time patterns)
- How performance degrades under spatial and temporal shifts

---

## 🌍 Study Areas

### Training Region: Makassar, Indonesia
- **Location**: South Sulawesi Province
- **Characteristics**: Coastal city, growing urban area, mixed topography
- **Data Period**: 2018–2020 (3 years)
- **Grid Cells**: ~3,600 (250m × 250m resolution)

### Test Region: Jakarta, Indonesia
- **Location**: DKI Jakarta (capital)
- **Characteristics**: Coastal megacity, highly urbanized, flat terrain
- **Data Period**: 2021–2022 (2 years)
- **Grid Cells**: ~8,000 (250m × 250m resolution)

**Rationale**: Different topography, urban patterns, and drainage systems enable testing of cross-region generalization while maintaining climate similarity (tropical Indonesia).

---

## 📊 Dataset: ST-FSLD v1.0

**Spatio-Temporal Flood Shortcut Learning Dataset**

### Key Characteristics

| Aspect | Value |
|--------|-------|
| **Spatial Resolution** | 250m × 250m grid |
| **Temporal Resolution** | Daily (2018–2022) |
| **Total Observations** | ~9.8 million |
| **Total Grid Cells** | ~11,600 |
| **Total Days** | 1,825 |
| **Class Balance** | ~11% floods, 89% non-floods |
| **File Size** | ~2.5 GB (CSV) |

### Data Structure

Each row represents:
```
(location, time) → feature vector X → flood label y
```

**Dataset Schema**:
```
lat, lon, date, rainfall, rainfall_3day, rainfall_7day, 
elevation, slope, landuse, distance_river, flood, region
```

**Example Rows**:

| lat | lon | date | rainfall | elevation | slope | landuse | distance_river | flood | region |
|-----|-----|------|----------|-----------|-------|---------|----------------|-------|--------|
| -5.15 | 119.45 | 2018-01-01 | 5.2 | 125 | 8.5 | urban | 1250 | 0 | Makassar |
| -5.15 | 119.45 | 2018-01-03 | 15.4 | 125 | 8.5 | urban | 1250 | 1 | Makassar |
| -6.21 | 106.85 | 2021-02-15 | 22.1 | 8 | 2.1 | urban | 450 | 1 | Jakarta |

### Feature Description

#### Environmental Features
- **rainfall** (mm): Daily precipitation from CHIRPS
- **rainfall_3day** (mm): 3-day cumulative rainfall
- **rainfall_7day** (mm): 7-day cumulative rainfall

#### Topographic Features
- **elevation** (m): Height above sea level (SRTM DEM)
- **slope** (°): Terrain slope (derived from DEM)

#### Hydrological Features
- **distance_river** (m): Euclidean distance to nearest river (OSM)

#### Land Features
- **landuse** (category): LULC classification (ESA WorldCover)
  - `urban`, `forest`, `agricultural`, `water`, `barren`

#### Diagnostic Features (for shortcut learning detection)
- **lat** (°): Latitude (WGS84)
- **lon** (°): Longitude (WGS84)
- ⚠️ **NOTE**: Used to detect if model relies on location rather than physical features

#### Target Variable
- **flood** (binary): 0 = no flood, 1 = flood detected
- **region** (categorical): `Makassar` or `Jakarta`

---

## 🌊 Flood Labeling Strategy

### Detection Method: Sentinel-1 SAR

Flood labels derived from **Sentinel-1 Synthetic Aperture Radar** using:

1. **Backscatter Change Detection**
   - Compare pre-flood (7-day mean) vs flood-day backscatter
   - Threshold: Δσ > -3 dB

2. **Multi-Criteria Validation**
   - Sentinel-1 backscatter change ✓
   - Preceding rainfall ≥ 20 mm ✓
   - Spatial extent ≥ 5 grid cells ✓

3. **Event-Based Sampling** (Non-random)
   - Pre-flood window: 7 days before event
   - Flood window: 3 days during event
   - Captures precursor signals

### Label Quality

- **Precision**: ~85% (correct detections / all detections)
- **Recall**: ~75% (detected floods / actual floods)
- **Validated Against**: News reports, government disaster declarations, social media

---

## 🧪 Experimental Design

### Experiment 1: Baseline (In-Domain)
```
Train: Makassar 2018–2020
Test:  Makassar 2021–2022
Goal:  Temporal generalization in same region
```

### Experiment 2: Cross-Region Generalization ⭐ PRIMARY
```
Train: Makassar 2018–2020
Test:  Jakarta 2021–2022
Goal:  Spatial generalization (main research question)
```

### Experiment 3: Spatial Bias Detection (Core)
```
Model A: WITH lat/lon features
Model B: WITHOUT lat/lon features

Train: Both on Makassar 2018–2020
Test:  Both on Jakarta 2021–2022

Goal:  Measure dependence on location
If Acc(A) >> Acc(B) → spatial bias confirmed
```

### Experiment 4: Feature Importance
```
Methods: SHAP, permutation importance, coefficient analysis
Goal:    Which features matter? Consistent across regions?
```

### Experiment 5: Error Analysis
```
Analyze: False positives, false negatives, spatial error distribution
Goal:    Identify systematic failure patterns
```

---

## 📈 Expected Outputs

### Technical Deliverables
- ✅ ST-FSLD v1.0 dataset (spatio-temporal, multi-region)
- ✅ ML models (Random Forest, XGBoost)
- ✅ Complete reproducible pipeline
- ✅ Open-source code & dataset

### Scientific Findings
- ✅ Quantified spatial generalization gap
- ✅ Evidence of spatial bias (or lack thereof)
- ✅ Feature importance insights
- ✅ Failure pattern analysis
- ✅ Recommendations for robust deployment

### Visualizations
- ✅ Flood risk maps
- ✅ Performance comparison charts
- ✅ Feature importance plots
- ✅ Error distribution maps
- ✅ Cross-region comparison

---

## 🚀 Project Structure

```
flood-ml-research/
├── docs/
│   ├── research_proposal.md              # Detailed research plan
│   ├── DATASET_SPECIFICATION.md          # Complete dataset spec
│   └── STRUCTURE.md                      # Project organization
├── data/
│   ├── raw/                              # Original data from sources
│   ├── processed/                        # Cleaned & ready for ML
│   └── external/                         # Reference data
├── src/
│   ├── data/                             # Data loading & preprocessing
│   ├── features/                         # Feature engineering
│   ├── models/                           # Model definitions
│   └── visualization/                    # Plotting & analysis
├── notebooks/
│   ├── 01_eda.ipynb                      # Exploratory data analysis
│   ├── 02_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_baseline_model.ipynb
│   ├── 05_generalization_test.ipynb      # Cross-region testing
│   ├── 06_spatial_bias_analysis.ipynb    # Core experiment
│   └── 07_error_analysis.ipynb
├── models/                               # Trained model artifacts
├── results/
│   ├── figures/                          # Output visualizations
│   └── metrics/                          # Performance results
├── main.py                               # Entry point
├── requirements.txt                      # Python dependencies
├── README.md                             # This file
└── STRUCTURE.md                          # Detailed structure guide
```

For detailed structure, see [`STRUCTURE.md`](STRUCTURE.md).

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip / conda
- Git

### Quick Start

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/flood-ml-research.git
cd flood-ml-research

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run baseline pipeline
python main.py
```

### Dependencies

See [`requirements.txt`](requirements.txt):
```
pandas, numpy, scikit-learn
xgboost, geopandas, rasterio
matplotlib, seaborn
jupyter, jupyter-lab
```

---

## 🔄 Workflow

### Phase 1: Data Collection & Preprocessing
1. Download geospatial data (CHIRPS, SRTM, ESA WorldCover, OSM)
2. Create spatial grid (Makassar + Jakarta)
3. Extract features & generate flood labels (Sentinel-1)
4. Assemble final dataset

**Status**: 🚧 In progress

### Phase 2: Exploratory Analysis
1. Dataset statistics & distributions
2. Seasonal patterns & flood frequency
3. Feature correlations
4. Class imbalance analysis

**Status**: 📋 Planned

### Phase 3: Modeling & Experiments
1. Train baseline models (Random Forest, XGBoost)
2. Run 7 experiments (see research proposal)
3. Analyze results & failure patterns
4. Detect spatial bias

**Status**: 📋 Planned

### Phase 4: Analysis & Interpretation
1. Feature importance analysis (SHAP)
2. Cross-region performance comparison
3. Error distribution analysis
4. Generate visualizations

**Status**: 📋 Planned

### Phase 5: Documentation & Publication
1. Write methodology section
2. Draft results & discussion
3. Submit to Q1 journal
4. Open-source release

**Status**: 📋 Planned

---

## 🎓 Core Research Questions

| RQ | Question | Dataset Support |
|----|---------| -- |
| **RQ1** | How well do models predict floods in-domain? | Baseline experiment |
| **RQ2** | How much does performance drop cross-region? | Primary experiment |
| **RQ3** | How stable are models across years? | Temporal validation |
| **RQ4** | Which features matter most? | Feature importance |
| **RQ5** | Do models rely on location? ⭐ CORE | Spatial bias detection |
| **RQ6** | What are systematic failure patterns? | Error analysis |

---

## 📚 References & Data Sources

### Geospatial Data Sources

| Data | Source | Website |
|------|--------|---------|
| **Rainfall** | CHIRPS v2.0 | https://www.chc.ucsb.edu/data/chirps |
| **Elevation** | SRTM DEM | https://lpdaac.usgs.gov/products/srtmgl1v003/ |
| **Land Use** | ESA WorldCover | https://www.esa-worldcover.org/ |
| **Rivers** | OpenStreetMap | https://www.openstreetmap.org/ |
| **Flood Labels** | Sentinel-1 SAR | https://sentinel.esa.int/ |

### Processing Platform

- **Google Earth Engine**: Cloud-based geospatial analysis
  - https://earthengine.google.com/
  - Free for research

### Related Literature

- Recent papers on flood prediction with ML
- Shortcut learning & distribution shift in ML
- Interpretability of geospatial models

---

## ⚠️ Important Notes

### Dataset Design Philosophy

This dataset is **NOT** designed for:
- ❌ Maximizing prediction accuracy
- ❌ Operational flood forecasting
- ❌ General-purpose ML benchmarks

Instead, it's designed for:
- ✅ Testing shortcut learning hypothesis
- ✅ Measuring spatial/temporal generalization
- ✅ Enabling reproducible ML research

### Class Imbalance

- Natural imbalance: ~11% floods, 89% non-floods
- **NOT balanced intentionally** (reflects reality)
- Evaluation metrics: ROC-AUC, PR-AUC (suitable for imbalance)

### Spatial Bias Testing

To detect spatial bias, compare:
- **Model A** (WITH lat/lon) vs **Model B** (WITHOUT lat/lon)
- If A significantly outperforms B → model relies on location
- Diagnostic feature, not predictor for production

---

## 🤝 Contributing

### How to Contribute

1. Fork repository
2. Create feature branch (`git checkout -b feature/xyz`)
3. Make changes & add tests
4. Commit with clear messages
5. Push & create Pull Request

### Guidelines

- Follow Python PEP 8 style guide
- Add docstrings to functions
- Include unit tests for new features
- Update documentation

---

## 📄 License

This project is licensed under **MIT License** (subject to finalization).

Dataset: Open access for research purposes (licensing pending).

---

## 👤 Author & Contact

**Author**: [Your Name]  
**Institution**: [Your University]  
**Email**: [your.email@example.com]

**Questions?** Please open an issue or check:
- [`docs/research_proposal.md`](docs/research_proposal.md) - Full research details
- [`docs/DATASET_SPECIFICATION.md`](docs/DATASET_SPECIFICATION.md) - Dataset technical spec
- [`STRUCTURE.md`](STRUCTURE.md) - Project organization

---

## 📖 Getting Started

### For New Contributors
1. Read [`STRUCTURE.md`](STRUCTURE.md) to understand project layout
2. Check [`docs/research_proposal.md`](docs/research_proposal.md) for research context
3. Review [`docs/DATASET_SPECIFICATION.md`](docs/DATASET_SPECIFICATION.md) for dataset details
4. Start with notebooks in `/notebooks/` folder

### For Reviewers/Evaluators
1. Start with this README (overview)
2. Read [`docs/research_proposal.md`](docs/research_proposal.md) (research design)
3. Review [`docs/DATASET_SPECIFICATION.md`](docs/DATASET_SPECIFICATION.md) (dataset validation)
4. Check `/results/` for outputs and visualizations

---

## 🔗 Useful Links

- 📋 Research Proposal: [`docs/research_proposal.md`](docs/research_proposal.md)
- 📊 Dataset Specification: [`docs/DATASET_SPECIFICATION.md`](docs/DATASET_SPECIFICATION.md)
- 🗺️ Project Structure: [`STRUCTURE.md`](STRUCTURE.md)
- 🚀 Notebooks: [`notebooks/`](notebooks/)
- 📈 Results: [`results/`](results/)

---

**Last Updated**: April 2026  
**Status**: 🚧 In Development  
**Next Milestone**: Complete Phase 1 (Data Collection)

---

## Dataset Design

This project uses a **spatio-temporal dataset**, where each row represents:

> A specific location at a specific time

---

### Dataset Construction Details

- Spatial resolution: 1 km × 1 km grid  
- Temporal resolution: daily observations  
- Each grid cell represents a spatial unit observed at a specific date  
- Features are extracted based on geographic location  
- Flood labels are assigned using Sentinel-1 detection  

### Dataset Structure

Each row represents a specific geographic location observed at a given date.

| lat | lon | date | rainfall (mm) | rainfall_3day (mm) | rainfall_7day (mm) | elevation (m) | slope (°) | landuse | distance_river (m) | flood | region |
|-----|-----|------|---------------|--------------------|--------------------|----------------|------------|----------|---------------------|--------|--------|
| -5.1477 | 119.4327 | 2020-01-15 | 45.2 | 120.5 | 210.3 | 12 | 1.8 | urban | 350 | 1 | Makassar |
| -5.1501 | 119.4350 | 2020-01-16 | 10.3 | 60.2 | 150.8 | 15 | 2.1 | urban | 420 | 0 | Makassar |
| -6.2088 | 106.8456 | 2021-02-10 | 80.5 | 200.1 | 350.7 | 8 | 0.9 | urban | 150 | 1 | Jakarta |

**Column Description:**

- `lat`, `lon`: Geographic coordinates  
- `date`: Observation date (YYYY-MM-DD)  
- `rainfall`: Daily rainfall  
- `rainfall_3day`, `rainfall_7day`: Accumulated rainfall over past days  
- `elevation`: Height above sea level  
- `slope`: Terrain slope  
- `landuse`: Land cover category  
- `distance_river`: Distance to nearest river  
- `flood`: Binary label (1 = flood, 0 = no flood)  
- `region`: Study area identifier  

---

## Flood Labeling Strategy (Critical)

Flood labeling is based on **spatio-temporal flood events**, not single-day observations.

### Key Principles

- Flood events may span **multiple consecutive days**  
- All affected grid cells during an event are labeled `flood = 1`  
- Non-flood conditions are labeled `flood = 0`  

### Event-Based Temporal Window

Each flood sample includes:

- Pre-flood window: **3–7 days before flood event**  
- Flood window: duration of observed flooding  

This allows the model to learn **precursor signals**, not just flood occurrence.

### Flood Detection Method

Flood labels are derived from **Sentinel-1 SAR imagery** using:

- Water detection via backscatter thresholding  
- Temporal comparison (before vs during flood)  

---

## Feature Description

### Environmental Features
- `rainfall`: daily rainfall  
- `rainfall_3day`: 3-day accumulated rainfall  
- `rainfall_7day`: 7-day accumulated rainfall  

### Topographic Features
- `elevation`: height above sea level (DEM)  
- `slope`: terrain slope  

### Land Features
- `landuse`: land cover classification  

### Hydrological Features
- `distance_river`: distance to nearest river  

### Spatial Features
- `lat`, `lon`: geographic coordinates (used for bias analysis)  

---

## Data Sources

- Rainfall: CHIRPS / NASA  
- Elevation: SRTM (DEM)  
- Land Use: ESA WorldCover  
- River Data: OpenStreetMap  
- Flood Detection: Sentinel-1 (Google Earth Engine)  

---

## Temporal Design

- Time range: 2018 – 2022  

### Data Split
- Train: 2018–2020  
- Test: 2021–2022  

---

## Data Considerations (Critical for Validity)

Special attention is given to potential risks:

- Spatial leakage due to geographic coordinates (lat/lon)  
- Temporal leakage from overlapping rainfall aggregation  
- Distribution shift across regions and time  

---

## Research Challenges

- Flood events are **spatially heterogeneous**  
- Flood duration varies across locations  
- Labels derived from SAR imagery may contain noise  
- Strong **distribution shift** between regions  
- Temporal patterns differ across years  

---

## Research Hypotheses

We hypothesize that:

- Models will perform well in-domain but degrade significantly out-of-domain  
- Models using geographic coordinates will outperform others but exhibit spatial bias  
- Rainfall features will dominate predictions, but may not generalize across regions 

---

## Evaluation Criteria

Model performance is assessed not only by predictive accuracy, but by:

- Generalization gap (in-domain vs out-of-domain performance)
- Stability across temporal splits
- Consistency of feature importance across regions
- Sensitivity to removal of spatial coordinates

A model is considered reliable if it maintains performance and interpretability under these conditions.

---

## Methodology

To address the research questions and validate the hypotheses, this study employs a structured experimental pipeline for developing and evaluating a spatio-temporal flood prediction framework using multi-source geospatial data.

### 1. Data Collection

Multi-source geospatial datasets are collected to capture the environmental, topographic, and hydrological factors influencing flood occurrence.

**Data sources include:**
- Rainfall data (CHIRPS / NASA)  
- Elevation data (SRTM DEM)  
- Land use / land cover (ESA WorldCover)  
- River networks (OpenStreetMap)  
- Satellite imagery (Sentinel-1 SAR)  

**Objective:**
To construct a consistent and spatially aligned dataset that integrates multiple data sources across both space and time.

---

### 2. Flood Label Generation

Flood labels are generated using **Sentinel-1 SAR imagery**, which enables water detection regardless of cloud conditions.

**Method:**
- Backscatter thresholding to detect water surfaces  
- Temporal comparison (before vs during flood events)  
- Identification of flood-affected areas  

**Label definition:**
- `flood = 1` → water detected (flood condition)  
- `flood = 0` → no water detected  

**Event-based approach:**
- Flood events may span multiple consecutive days  
- All affected grid cells during the event are labeled as flood  
- Pre-flood conditions are captured using rainfall accumulation features  

This event-based labeling strategy enables the model to learn temporal flood dynamics rather than relying on single-day observations.

---

### 3. Preprocessing

Raw geospatial data is cleaned and aligned to ensure consistency.

**Steps:**
- Handling missing values  
- Spatial resampling to a common resolution (e.g., 1 km grid)  
- Coordinate system standardization  
- Temporal alignment across datasets  

**Objective:**
To produce a clean, consistent, and spatially aligned dataset suitable for downstream modeling.

---

### 4. Feature Engineering

Relevant features are derived to capture the physical processes of flooding.

**Temporal features:**
- Daily rainfall  
- 3-day accumulated rainfall  
- 7-day accumulated rainfall  

**Topographic features:**
- Elevation (from DEM)  
- Slope (derived from DEM)  

**Hydrological features:**
- Distance to nearest river  

**Land features:**
- Land use encoding  

**Spatial features:**
- Latitude and longitude (used specifically for spatial bias analysis)

**Objective:**
To construct informative features that reflect both environmental conditions and flood-generating processes.

---

### 5. Modeling

Machine learning models are trained using tabular geospatial features.

**Models used:**
- Random Forest  
- XGBoost  

**Rationale:**
- Robust for tabular data  
- Capable of modeling non-linear relationships  
- Provide feature importance for interpretability  

**Objective:**
To learn predictive relationships between geospatial features and flood occurrence.

---

### 6. Evaluation

Model performance is evaluated not only in terms of predictive accuracy, but also in terms of generalization and robustness.

**Metrics:**
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  
- Confusion Matrix  

**Evaluation scenarios:**
- In-domain (train and test on the same region)  
- Cross-region (train on Makassar, test on Jakarta)  
- Temporal generalization (train on earlier years, test on later years)  

**Additional analysis:**
- Feature importance comparison  
- Spatial bias testing (with vs without coordinates)  
- Error analysis (false positives and false negatives)  
- Sensitivity to data variation  

**Objective:**
To assess model performance, generalization capability, and robustness under varying spatial and temporal conditions.

---

## Experimental Design

### 1. Baseline Performance (In-Domain)
- Train and test on Makassar  
- Establish baseline model performance  

### 2. Cross-Region Generalization
- Train on Makassar  
- Test on Jakarta  
- Measure performance degradation  

### 3. Temporal Generalization
- Train on 2018–2020  
- Test on 2021–2022  
- Evaluate robustness over time  

### 4. Feature Importance Analysis
- Analyze dominant features  
- Compare importance across regions  

### 5. Spatial Bias Test (Core Experiment)
- Model A: with lat/lon  
- Model B: without lat/lon  
- Evaluate dependence on spatial coordinates  

### 6. Error Analysis
- Analyze false positives and false negatives  
- Identify spatial distribution of errors  

### 7. Sensitivity Analysis
- Reduce training data size  
- Introduce noise  
- Evaluate robustness under data variation  
---
## Project Structure

```text
flood-ml-research/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── visualization/
│
├── models/
│   ├── baseline/
│   ├── generalization/
│   └── spatial_bias/
│
├── notebooks/
├── results/
│   ├── figures/
│   └── metrics/
│
├── docs/
│   └── research_proposal.md
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

git clone https://github.com/Aepra/flood-ml-research.git  
cd flood-ml-research  
pip install -r requirements.txt  

---

## Usage

python main.py  

---
## Reproducibility

All experiments are designed to be reproducible:

- Fixed random seeds for model training  
- Consistent preprocessing pipeline  
- Structured experiment tracking via notebooks and scripts  

Results can be reproduced from raw data using the provided pipeline.

## Final Note

The hardest part of this research is not building the model, but:

- Interpreting results  
- Understanding model behavior  
- Drawing meaningful conclusions  