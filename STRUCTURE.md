# Project Structure & Organization

Complete guide to the directory hierarchy, data flow, and workflow for the **Spatio-Temporal Flood Shortcut Learning (ST-FSLD v1.0)** research project.

**Last Updated:** April 2026 | **Version:** 1.0-diagnostic-framework

---

## 📊 Project Hierarchy Diagram

```
flood-ml-research/
│
├── 📄 Root Documentation
│   ├── README.md                  # Project overview & quick start
│   ├── STRUCTURE.md              # This file - directory guide
│   ├── main.py                   # Entry point for pipeline
│   └── requirements.txt           # Python dependencies
│
├── 📁 docs/ - Research Documentation
│   ├── research_proposal.md       # Full research methodology (16 sections)
│   └── DATASET_SPECIFICATION.md   # Technical dataset specification (14 sections)
│
├── 📁 data/ - Data Storage (Multi-Stage)
│   ├── raw/                       # Original data from sources
│   ├── processed/                 # Cleaned, aligned, normalized data
│   └── external/                  # Reference & auxiliary data
│
├── 📁 src/ - Source Code (Reusable Modules)
│   ├── data/                      # Data loading & preprocessing
│   ├── features/                  # Feature engineering & derivation
│   ├── models/                    # Model training & evaluation
│   └── visualization/             # Plotting & analysis figures
│
├── 📁 models/ - Model Artifacts
│   ├── random_forest/             # RF model checkpoints
│   └── xgboost/                   # XGBoost model checkpoints
│
├── 📁 notebooks/ - Jupyter Analysis
│   ├── 01_data_exploration.ipynb         # EDA & data inspection
│   ├── 02_feature_engineering.ipynb      # Feature derivation
│   ├── 03_model_training.ipynb           # Model fitting
│   ├── 04_shortcut_analysis.ipynb        # Shortcut detection
│   └── 05_failure_modes.ipynb            # Failure categorization
│
└── 📁 results/ - Output & Analysis
    ├── metrics/                   # Quantitative results (CSV/JSON)
    │   ├── in_domain_baseline.csv
    │   ├── spatial_shift_test.csv
    │   ├── temporal_shift_test.csv
    │   ├── feature_importance.csv
    │   └── failure_modes.csv
    │
    └── figures/                   # Publication-quality plots
        ├── shortcut_learning_score.png
        ├── performance_degradation.png
        ├── feature_dependency.png
        ├── physical_consistency.png
        └── failure_mode_distribution.png
```

---

## 🗂️ Detailed Directory Descriptions

### 📁 **root/** — Project Root

| File | Purpose |
|------|---------|
| `README.md` | Project overview, installation, quick start, research questions |
| `STRUCTURE.md` | This file - directory & workflow documentation |
| `main.py` | Main entry point for running full pipeline |
| `requirements.txt` | Python package dependencies (pip install -r requirements.txt) |
| `.gitignore` | Git ignore patterns (data/, models/, results/, __pycache__/) |
| `.git/` | Version control history |

---

### 📁 **docs/** — Research Documentation

Research and technical documentation for the project.

```
docs/
├── research_proposal.md
│   ├── 1. Research Positioning      # Shortcut learning context
│   ├── 2. Problem Statement         # Literature gap
│   ├── 3. Research Objectives       # Main + 6 specific
│   ├── 4. Research Questions        # RQ1-RQ6
│   ├── 5. Hypotheses                # H1-H6
│   ├── 6. Dataset Design            # Spatio-temporal unit definition
│   ├── 7. Data Sources              # CHIRPS, SRTM, ESA, OSM, Sentinel-1
│   ├── 8. Methodology Pipeline      # 6 steps (collect → evaluate)
│   ├── 9. Experimental Design       # 6 experiments
│   ├── 10. Shortcut Learning Score  # S = (AUC_in - AUC_shift) / AUC_in
│   ├── 11. Failure Mode Taxonomy    # 4 failure types
│   ├── 12. Analysis Framework       # 3 layers (behavioral → dependency → mechanisms)
│   ├── 13. Expected Findings        # Hypothesized outcomes
│   ├── 14. Contributions            # 4 research contributions
│   ├── 15. Risks & Mitigation       # Potential challenges
│   └── 16. Core Insight             # Diagnostic reframing
│
└── DATASET_SPECIFICATION.md
    ├── 1. Dataset Purpose              # Diagnostic research, not operational
    ├── 2. Fundamental Unit              # (lat, lon, date) → feature vector
    ├── 3. Spatial Design                # 250m grid, Makassar/Jakarta, WGS84
    ├── 4. Temporal Design               # Daily, 2018-2022, strict splits
    ├── 5. Flood Event Definition        # Sentinel-1 SAR, -3dB threshold
    ├── 6. Feature Specification         # 11 features detailed
    ├── 7. Label Balance Strategy        # Natural ~11% / 89%, no balancing
    ├── 8. Data Generation Pipeline      # 6 stages (grid → export)
    ├── 9. Data Split Design             # Spatial + temporal
    ├── 10. Quality Control              # Missing data, noise filtering
    ├── 11. Output Format                # CSV schema
    ├── 12. Characteristics & Stats      # Distributions
    ├── 13. Design Principles            # Why not balance, etc.
    └── 14. Implementation Roadmap       # 5 phases
```

---

### 📁 **data/** — Data Storage (Multi-Stage Pipeline)

Hierarchical data management following preprocessing stages.

```
data/
│
├── raw/
│   ├── CHIRPS/
│   │   └── *.tif                    # Daily rainfall GeoTIFF files
│   │                                # Region: Makassar + Jakarta
│   │                                # Period: 2018-2022
│   │                                # Resolution: 0.05° (~5.5 km)
│   │
│   ├── SRTM_DEM/
│   │   └── *.tif                    # Digital Elevation Model
│   │                                # Resolution: 30m
│   │                                # Coverage: Study areas
│   │
│   ├── ESA_WorldCover/
│   │   └── *.tif                    # Land use classification
│   │                                # Resolution: 10m
│   │                                # Classes: 11 land cover types
│   │
│   ├── OpenStreetMap/
│   │   └── rivers.shp               # River network vector data
│   │                                # Format: Shapefile (shp/shx/dbf)
│   │
│   └── Sentinel1/
│       └── *.xml                    # SAR backscatter measurements
│                                    # Acquisition: VV + VH polarization
│                                    # Resolution: 10m
│
├── processed/
│   ├── makassar_train_2018_2020.csv
│   │   ├── 1.8M observations       # Grid cells × days
│   │   ├── Features: 11 columns    # (rainfall, elevation, slope, etc.)
│   │   ├── Target: flood           # Binary (0/1)
│   │   └── Size: ~450 MB
│   │
│   ├── jakarta_test_2021_2022.csv
│   │   ├── 1.6M observations
│   │   ├── Same schema as training
│   │   └── Size: ~400 MB
│   │
│   ├── feature_matrix_scaled.csv    # Normalized features for modeling
│   │   ├── (lat, lon, date) + 11 features
│   │   └── Size: ~550 MB
│   │
│   ├── train_split.csv              # Training set with indices
│   ├── test_split.csv               # Testing set with indices
│   │
│   └── metadata.json                # Dataset metadata
│       ├── grid_info (3600 Makassar cells, 8000 Jakarta cells)
│       ├── feature_stats (mean, std, min, max per feature)
│       └── temporal_coverage (date ranges)
│
└── external/
    ├── grid_definition.shp          # 250m grid cell geometries
    │                                # CRS: WGS84 + UTM 50S
    │
    ├── reference_boundaries/
    │   ├── makassar_boundary.shp    # Administrative boundary
    │   └── jakarta_boundary.shp
    │
    └── lookups/
        ├── landuse_classification.csv  # Land use class codes
        └── region_centroids.csv        # Geographic reference points
```

---

### 📁 **src/** — Source Code (Reusable Modules)

Core logic organized into functional modules.

```
src/
│
├── data/
│   ├── __init__.py
│   ├── load.py
│   │   ├── load_chirps_rainfall()
│   │   ├── load_srtm_dem()
│   │   ├── load_esaworldcover()
│   │   ├── load_openstreetmap()
│   │   └── load_sentinel1_labels()
│   │
│   ├── preprocess.py
│   │   ├── align_spatial_grids()
│   │   ├── resample_to_250m()
│   │   ├── handle_missing_values()
│   │   ├── normalize_features()
│   │   └── create_temporal_windows()
│   │
│   ├── validation.py
│   │   ├── check_data_completeness()
│   │   ├── validate_crs_consistency()
│   │   ├── detect_outliers()
│   │   └── quality_report()
│   │
│   └── split.py
│       ├── spatial_train_test_split()    # Makassar/Jakarta split
│       ├── temporal_train_test_split()   # 2018-2020 / 2021-2022
│       └── stratified_split()
│
├── features/
│   ├── __init__.py
│   ├── engineering.py
│   │   ├── compute_slope()              # From DEM (degrees)
│   │   ├── distance_to_river()          # From OSM (meters)
│   │   ├── aggregate_rainfall()         # 3-day, 7-day windows (mm)
│   │   ├── encode_landuse()             # One-hot or ordinal
│   │   └── derive_interaction_features()
│   │
│   ├── scaling.py
│   │   ├── standard_scaler()
│   │   ├── robust_scaler()
│   │   └── min_max_scaler()
│   │
│   └── importance.py
│       ├── shap_importance()            # SHAP values for interpretability
│       ├── permutation_importance()     # Feature shuffling analysis
│       └── ablation_study()             # Remove features iteratively
│
├── models/
│   ├── __init__.py
│   ├── train.py
│   │   ├── train_random_forest()        # RandomForestClassifier
│   │   ├── train_xgboost()              # XGBoost classifier
│   │   ├── hyperparameter_tuning()      # GridSearchCV / RandomizedSearch
│   │   └── cross_validation()
│   │
│   ├── evaluate.py
│   │   ├── compute_auc_roc()            # Primary metric (AUC)
│   │   ├── compute_auc_pr()             # Precision-Recall
│   │   ├── compute_f1_score()           # F1 for imbalanced data
│   │   ├── compute_confusion_matrix()
│   │   └── classification_report()
│   │
│   ├── experiments.py
│   │   ├── experiment_1_1_in_domain()      # In-domain baseline
│   │   ├── experiment_1_2_subregion()      # Sub-region holdout
│   │   ├── experiment_2_1_spatial_shift()  # Spatial shift (Makassar → Jakarta)
│   │   ├── experiment_2_2_temporal_shift() # Temporal shift (2018-20 → 2021-22)
│   │   ├── experiment_2_3_distance_split() # Distance-based split
│   │   ├── experiment_3_1_perturbation()   # Spatial perturbation (noise injection)
│   │   ├── experiment_3_2_spatial_shuffle()# Spatial shuffle (region break)
│   │   ├── experiment_3_3_feature_dose()   # Feature intervention dose test
│   │   ├── experiment_3_4_counterfactual() # Counterfactual flood test
│   │   ├── experiment_4_1_monotonicity()   # Monotonicity test (physical laws)
│   │   └── experiment_4_2_consistency()    # Causal consistency score
│   │
│   └── diagnostics.py
│       ├── shortcut_learning_score()    # S = (AUC_in - AUC_shift) / AUC_in
│       ├── analyze_failure_modes()      # Categorize errors
│       └── physical_consistency_check()
│
└── visualization/
    ├── __init__.py
    ├── plots.py
    │   ├── plot_auc_curves()             # ROC & PR curves
    │   ├── plot_shortcut_score()         # S score visualization
    │   ├── plot_feature_importance()     # SHAP, permutation importance
    │   ├── plot_failure_distribution()   # Error mode breakdown
    │   └── plot_spatial_patterns()       # Map-based visualizations
    │
    ├── diagnostics.py
    │   ├── plot_performance_degradation() # Compare shift results
    │   ├── plot_physical_consistency()     # Rainfall vs flood relationship
    │   └── plot_lat_lon_dependence()      # Spatial memorization evidence
    │
    └── report.py
        ├── generate_summary_table()      # Metrics comparison table
        └── create_summary_figure()       # Multi-panel figure
```

---

### 📁 **models/** — Model Artifacts & Checkpoints

Trained model storage organized by algorithm.

```
models/
│
├── random_forest/
│   ├── experiment_1_in_domain.pkl              # Makassar train/test
│   ├── experiment_2_spatial_shift.pkl          # Makassar → Jakarta
│   ├── experiment_3_temporal_shift.pkl         # 2018-20 → 2021-22
│   ├── hyperparameters.json                    # Best parameters
│   │   ├── n_estimators: 100
│   │   ├── max_depth: 20
│   │   ├── min_samples_split: 10
│   │   └── random_state: 42
│   │
│   └── feature_names.json                      # Feature order & names
│
└── xgboost/
    ├── experiment_1_in_domain.pkl
    ├── experiment_2_spatial_shift.pkl
    ├── experiment_3_temporal_shift.pkl
    ├── hyperparameters.json
    │   ├── n_estimators: 100
    │   ├── max_depth: 7
    │   ├── learning_rate: 0.1
    │   └── subsample: 0.8
    │
    └── feature_names.json
```

---

### 📁 **notebooks/** — Jupyter Analysis & Exploration

Interactive notebooks for development & visualization.

```
notebooks/
│
├── 01_data_exploration.ipynb
│   ├── Load raw data from multiple sources
│   ├── Inspect spatial coverage & temporal ranges
│   ├── Visualize geographic distributions
│   ├── Check for missing data & outliers
│   └── Output: EDA summary & diagnostic plots
│
├── 02_feature_engineering.ipynb
│   ├── Derive topographic features (slope, aspect)
│   ├── Calculate hydrological features (distance to river)
│   ├── Aggregate rainfall (moving windows)
│   ├── Encode categorical features (land use)
│   └── Output: Feature matrix CSV files
│
├── 03_model_training.ipynb
│   ├── Prepare train/test splits
│   ├── Train Random Forest & XGBoost
│   ├── Perform hyperparameter tuning
│   ├── Evaluate baseline performance
│   └── Output: Trained model pickles
│
├── 04_shortcut_analysis.ipynb
│   ├── Compute Shortcut Learning Score (S)
│   ├── Run SHAP feature importance analysis
│   ├── Ablation study (remove lat/lon)
│   ├── Compare in-domain vs shift performance
│   └── Output: Feature importance plots & metrics
│
└── 05_failure_modes.ipynb
    ├── Categorize prediction errors
    ├── Identify spatial vs temporal failure patterns
    ├── Check physical consistency violations
    ├── Visualize failure distributions
    └── Output: Failure mode summary & plots
```

---

### 📁 **results/** — Output & Analysis Results

Quantitative metrics and publication-quality figures.

```
results/
│
├── metrics/
│   ├── 01_in_domain_baseline.csv
│   │   ├── Model, AUC_ROC, AUC_PR, F1, Accuracy
│   │   └── For: Random Forest, XGBoost
│   │
│   ├── 02_sub_region_holdout.csv
│   │   ├── Train region vs test region performance
│   │   └── Short-range spatial validation
│   │
│   ├── 03_spatial_shift_test.csv
│   │   ├── Train: Makassar | Test: Jakarta
│   │   ├── AUC degradation (S_spatial)
│   │   └── Evidence of geographic memorization
│   │
│   ├── 04_temporal_shift_test.csv
│   │   ├── Train: 2018-2020 | Test: 2021-2022
│   │   ├── AUC degradation (S_temporal)
│   │   └── Evidence of seasonal shortcuts
│   │
│   ├── 05_distance_based_split.csv
│   │   ├── AUC vs geographic distance
│   │   └── Quantify distance-dependent generalization failure
│   │
│   ├── 06_perturbation_sensitivity.csv
│   │   ├── Noise level (±100m, ±1km, ±5km)
│   │   ├── AUC degradation per noise level
│   │   └── Evidence of coordinate memorization
│   │
│   ├── 07_spatial_shuffle_test.csv
│   │   ├── Shuffle A, B, C configurations
│   │   ├── AUC drop per shuffle type
│   │   └── Distinguish location encoding vs physical learning
│   │
│   ├── 08_feature_intervention_dose.csv
│   │   ├── Configuration, AUC, Feature_set
│   │   ├── Full | No-Spatial | Spatial-Only | No-Physical | Rainfall-Only
│   │   └── Measure feature importance via dose response
│   │
│   ├── 09_counterfactual_test.csv
│   │   ├── Sample_ID, Original_Prediction, Counterfactual_Prediction, Direction_Match
│   │   └── Evidence of physical understanding
│   │
│   ├── 10_monotonicity_violations.csv
│   │   ├── Physical_Rule, Violation_Count, Violation_Rate
│   │   ├── Rainfall↑→Flood↑, Elevation↑→Flood↓, etc.
│   │   └── % violations of physical laws
│   │
│   ├── 11_causal_consistency.json
│   │   ├── Causal_Consistency_Score (C metric)
│   │   ├── C = 100%: perfect alignment
│   │   ├── C = 50%: random
│   │   └── C < 50%: anti-aligned (shortcut learning)
│   │
│   ├── feature_importance.csv
│   │   ├── Feature, Importance_SHAP, Importance_Permutation
│   │   └── Comparison: spatial vs physical features
│   │
│   └── failure_modes.csv
│       ├── Failure_Type, Count, Percentage
│       ├── Spatial Memorization | Temporal Shortcut | 
│       │   Hydrological Inconsistency | Feature Proxy Dominance
│       └── Structured error categorization
│
└── figures/
    ├── 01_in_domain_baseline.png
    │   ├── ROC & PR curves for in-domain test
    │   └── AUC baseline reference
    │
    ├── 02_spatial_shift_degradation.png
    │   ├── AUC comparison: in-domain vs spatial shift
    │   └── Evidence of geographic memorization
    │
    ├── 03_temporal_shift_degradation.png
    │   ├── AUC comparison: 2018-20 train vs 2021-22 test
    │   └── Evidence of seasonal shortcuts
    │
    ├── 04_distance_based_performance.png
    │   ├── Line plot: AUC vs geographic distance
    │   └── Quantify distance-dependent generalization failure
    │
    ├── 05_perturbation_sensitivity.png
    │   ├── Bar chart: AUC drop vs noise magnitude
    │   ├── ±100m, ±1km, ±5km noise levels
    │   └── Evidence of coordinate memorization
    │
    ├── 06_spatial_shuffle_comparison.png
    │   ├── Bar chart: Shuffle A vs B vs C AUC drops
    │   └── Distinguish location encoding vs physical learning
    │
    ├── 07_feature_dose_response.png
    │   ├── Line plot: AUC vs configuration
    │   ├── Full → No-Spatial → Spatial-Only → No-Physical
    │   └── Feature importance dose-response curve
    │
    ├── 08_counterfactual_alignment.png
    │   ├── Scatter: Original vs Counterfactual predictions
    │   ├── Direction alignment rate
    │   └── Evidence of physical understanding
    │
    ├── 09_monotonicity_violations.png
    │   ├── Heatmap: Violation rates per physical rule
    │   ├── Rainfall↑, Elevation↑, Distance↑, Slope↑
    │   └── Physical law compliance scorecard
    │
    ├── 10_causal_consistency_score.png
    │   ├── Gauge chart: C = causal consistency score (0-100%)
    │   ├── C=100% (perfect) vs C=50% (random) vs C<50% (anti-aligned)
    │   └── Q1-key metric for shortcut learning detection
    │
    ├── 11_feature_importance_ranking.png
    │   ├── SHAP importance plot: Feature rankings
    │   ├── Highlight: lat/lon vs rainfall importance
    │   └── Evidence of spatial proxy dominance
    │
    ├── 12_layer_evidence_synthesis.png
    │   ├── Multi-panel figure combining all 4 layers
    │   ├── L1 (baseline) → L2 (shift) → L3 (intervention) → L4 (logic)
    │   └── Comprehensive shortcut learning diagnosis
    │
    └── 13_failure_mode_distribution.png
        ├── Pie chart: Proportions of 4 failure types
        └── Breakdown: Spatial vs temporal vs physics violations
```

---

## 🔄 Data Flow Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     DATA FLOW: RAW → PROCESSED → MODELING                │
└─────────────────────────────────────────────────────────────────────────┘

STAGE 1: COLLECTION
  ↓
  [CHIRPS]  [SRTM]  [ESA WorldCover]  [OpenStreetMap]  [Sentinel-1]
  (rainfall) (DEM)  (land use)        (rivers)        (flood labels)
  ↓
  data/raw/

STAGE 2: PREPROCESSING
  ↓
  [Spatial Alignment] → [Resample to 250m] → [Fill Missing Values]
  ↓
  data/processed/raw_aligned.csv

STAGE 3: FEATURE ENGINEERING
  ↓
  [Compute Slope] [Distance to River] [Aggregate Rainfall] [Encode Landuse]
  ↓
  data/processed/feature_matrix.csv (11 features)

STAGE 4: DATA SPLIT
  ↓
  ┌─────────────────┬──────────────────┐
  │ Experiment 1    │ Experiment 2     │
  │ (In-Domain)     │ (Spatial Shift)  │
  │                 │                  │
  │ Train: Makassar │ Train: Makassar  │
  │ Test: Makassar  │ Test: Jakarta    │
  │ 2018-20 / 21-22 │ 2018-20 / 21-22  │
  └─────────────────┴──────────────────┘
  ↓
  data/processed/{train|test}_splits.csv

STAGE 5: MODELING
  ↓
  [Random Forest] [XGBoost]
  ↓
  models/{random_forest|xgboost}/{experiment}.pkl

STAGE 6: EVALUATION & DIAGNOSTICS
  ↓
  [Experiment 1-3: Performance Metrics]
  [Experiment 4: Feature Importance (SHAP, Ablation)]
  [Experiment 5: Physical Consistency Checks]
  [Experiment 6: Failure Mode Categorization]
  ↓
  [Compute Shortcut Learning Score: S = (AUC_in - AUC_shift) / AUC_in]
  ↓
  results/metrics/ + results/figures/
```

---

## 🧪 Experiments Workflow (Q1-Level: 4-Layer Framework)

### LAYER 1 — OBSERVATIONAL BASELINE

```
EXPERIMENT 1.1: IN-DOMAIN BASELINE
├── Train: Makassar 2018-2020
├── Test: Makassar 2021-2022
├── Purpose: Establish baseline performance ceiling
└── Output: in_domain_baseline.csv (AUC, F1, confusion matrix)

EXPERIMENT 1.2: SUB-REGION HOLDOUT
├── Train: Makassar subregion (80%)
├── Test: Makassar subregion (20%)
├── Purpose: Internal spatial validation (short-range shift)
└── Output: sub_region_holdout.csv
```

---

### LAYER 2 — NATURAL DISTRIBUTION SHIFT

```
EXPERIMENT 2.1: SPATIAL SHIFT TEST
├── Train: Makassar 2018-2020
├── Test: Jakarta 2021-2022
├── Purpose: Detect geographic memorization (cross-regional)
├── Expected: Large AUC drop if model learns lat/lon encoding
└── Output: spatial_shift_test.csv

EXPERIMENT 2.2: TEMPORAL SHIFT TEST
├── Train: Makassar 2018-2020
├── Test: Makassar 2021-2022
├── Purpose: Detect seasonal shortcuts (temporal distribution shift)
├── Expected: AUC drop if model exploits seasonal correlations
└── Output: temporal_shift_test.csv

EXPERIMENT 2.3: DISTANCE-BASED SPLIT
├── Train: Near-region cells (distance < 5km)
├── Test: Far-region cells (distance > 10km)
├── Purpose: Quantify AUC degradation as function of geographic distance
└── Output: distance_based_split.csv (AUC vs distance curve)
```

---

### LAYER 3 — INTERVENTION EXPERIMENTS (Q1-CRITICAL)

```
EXPERIMENT 3.1: SPATIAL PERTURBATION TEST
├── Procedure: Add controlled noise to lat/lon
│   ├── Small noise: ±100m
│   ├── Medium noise: ±1km
│   └── Large noise: ±5km
├── Purpose: Test sensitivity to geographic coordinate shifts
├── Expected: AUC degradation proportional to noise magnitude
└── Output: perturbation_sensitivity.csv

EXPERIMENT 3.2: SPATIAL SHUFFLE TEST (REGION BREAK)
├── Shuffle A: Swap coordinates within Makassar (preserve physical)
├── Shuffle B: Swap coordinates within elevation zones (preserve physics)
├── Shuffle C: Random global shuffle (destroy spatial structure)
├── Purpose: Isolate geographic memorization vs physical learning
└── Output: spatial_shuffle_test.csv

EXPERIMENT 3.3: FEATURE INTERVENTION DOSE TEST
├── Configuration 1: Full (all 11 features)
├── Configuration 2: No-Spatial (remove lat/lon)
├── Configuration 3: Spatial-Only (only lat/lon)
├── Configuration 4: No-Physical (remove rainfall, elevation, river_dist)
├── Configuration 5: Rainfall-Only (only rainfall feature)
├── Purpose: Measure feature importance via AUC difference
└── Output: feature_intervention_dose.csv

EXPERIMENT 3.4: COUNTERFACTUAL FLOOD TEST
├── Procedure: Generate synthetic samples with modified features
│   ├── Counterfactual non-flood: reduce rainfall 50%, increase elevation
│   └── Counterfactual flood: increase rainfall 50%, decrease elevation
├── Purpose: Test model understanding of physical relationships
├── Expected: Predictions should align with counterfactual changes
└── Output: counterfactual_test.csv
```

---

### LAYER 4 — COUNTERFACTUAL LOGIC TESTS

```
EXPERIMENT 4.1: MONOTONICITY TEST
├── Physical Rules Expected:
│   ├── Rainfall ↑ → Flood probability ↑
│   ├── Elevation ↑ → Flood probability ↓
│   ├── River distance ↑ → Flood probability ↓
│   └── Slope ↑ → Flood probability ↓
├── Procedure: Vary each feature incrementally, record prediction response
├── Metric: Violation rate (% predictions violating physical laws)
├── Expected: Low violation rate (< 10%)
└── Output: monotonicity_violations.csv

EXPERIMENT 4.2: CAUSAL CONSISTENCY SCORE
├── Formula: C = (# consistent predictions / # total predictions) × 100%
├── Procedure:
│   ├── Apply counterfactual perturbation to sample
│   ├── Compute expected direction from physics
│   ├── Compare with actual model prediction change
│   └── Aggregate consistency rate
├── Interpretation:
│   ├── C = 100%: Perfect physical alignment
│   ├── C = 50%: Random wrt physics
│   └── C < 50%: Anti-aligned (shortcut learning evidence)
└── Output: causal_consistency.json
```

---

## 📋 Common Workflows

### Workflow 1: Run Full Pipeline

```bash
# 1. Activate environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run data processing
python src/data/load.py
python src/data/preprocess.py
python src/features/engineering.py

# 4. Run all experiments
python src/models/train.py --experiment all
python src/models/evaluate.py --analysis all

# 5. View results
ls results/metrics/
ls results/figures/
```

### Workflow 2: Run Single Experiment

```bash
# Example: Spatial Shift Test (Experiment 2)
python src/models/train.py --experiment 2 --model xgboost

# Output: results/metrics/spatial_shift_test.csv
```

### Workflow 3: Feature Importance Analysis

```bash
python src/features/importance.py --method shap
python src/features/importance.py --method permutation
python src/models/diagnostics.py --ablation lat_lon

# Output: results/figures/feature_dependency.png
```

### Workflow 4: Generate Diagnostic Report

```bash
python src/models/diagnostics.py --compute_shortcut_score
python src/models/diagnostics.py --failure_modes
python src/visualization/report.py --generate_summary

# Output: Comprehensive summary table & figure
```

---

## 📊 Key Output Locations

| Output Type | Location | Format | Purpose |
|-------------|----------|--------|---------|
| **Metrics** | `results/metrics/` | CSV/JSON | Quantitative evaluation |
| **Figures** | `results/figures/` | PNG | Visualization & publication |
| **Models** | `models/` | PKL | Model inference & re-use |
| **Datasets** | `data/processed/` | CSV | Training & testing |
| **Logs** | (console) | TXT | Debugging & tracking |

---

## 🔐 Version Control

```
.git/              # Git repository
.gitignore         # Ignore patterns:
                   # - data/ (large files)
                   # - models/ (artifacts)
                   # - results/ (outputs)
                   # - .ipynb_checkpoints/
```

**Push to GitHub:**
```bash
git add README.md STRUCTURE.md docs/
git commit -m "Update documentation & project structure"
git push origin main
```

---

## 📝 File Naming Conventions

**Data files:**
- `{region}_{purpose}_{date_range}.csv`
- Example: `makassar_train_2018_2020.csv`

**Model files:**
- `experiment_{number}_{model_type}.pkl`
- Example: `experiment_2_xgboost.pkl`

**Results files:**
- `{experiment_name}_{metric_type}.csv`
- Example: `spatial_shift_test_metrics.csv`

**Figure files:**
- `{number:02d}_{description}.png`
- Example: `03_feature_dependency.png`

---

## 🎯 Summary: Directory Purposes

| Directory | Contains | Why |
|-----------|----------|-----|
| `docs/` | Research proposal & specs | Reference & methodology |
| `data/` | Raw → processed data | Reproducible preprocessing |
| `src/` | Reusable code modules | Clean, maintainable code |
| `models/` | Trained model artifacts | Production & inference |
| `notebooks/` | Interactive analysis | Exploratory work & visualization |
| `results/` | Metrics & figures | Publication outputs |

---

**Project Status:** 🚧 In Development  
**Target:** Q1 Journal/Conference Submission  
**Research Focus:** Diagnosing shortcut learning under distribution shift
