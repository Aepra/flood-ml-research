# A Diagnostic Framework for Quantifying Spatio-Temporal Shortcut Learning in Machine Learning-Based Flood Prediction Under Cross-Regional and Temporal Distribution Shifts

---

## 1. Research Positioning

Flood prediction using machine learning has achieved high predictive performance in recent studies. However, high in-domain accuracy does not necessarily indicate that models learn physically meaningful hydrological processes.

Instead, models may rely on **spatio-temporal shortcut mechanisms**, such as:
- geographic encoding (lat/lon memorization)
- regional rainfall co-occurrence patterns
- temporal seasonality leakage

A key limitation in current literature is the absence of a **quantitative framework** to measure shortcut learning under spatial and temporal distribution shifts.

---

## 2. Problem Statement

There is no standardized metric or framework to quantify the extent to which machine learning flood prediction models rely on spatio-temporal shortcuts rather than physically consistent hydrological relationships.

This leads to an open question:

> Do flood prediction models generalize hydrologically, or do they fail under distribution shift due to shortcut learning?

---

## 3. Research Objectives

### Main Objective

To develop a diagnostic framework for quantifying spatio-temporal shortcut learning in flood prediction models under distribution shift.

### Specific Objectives

- Quantify shortcut learning behavior in in-domain and shifted settings  
- Measure performance degradation under spatial shift (Makassar → Jakarta)  
- Measure performance degradation under temporal shift (2018–2020 → 2021–2022)  
- Evaluate dependence on spatial proxy features (lat/lon)  
- Assess physical consistency of model predictions  
- Identify structured failure modes under distribution shift  

---

## 4. Research Questions

### RQ1 — In-Domain Shortcut Dependency  
Do models already rely on spatio-temporal shortcuts even within the training region?

### RQ2 — Spatial Generalization Failure  
How significantly does model performance degrade under cross-regional shift?

### RQ3 — Temporal Generalization Failure  
Do models rely on temporal correlations that fail across years?

### RQ4 — Feature Shortcut Dominance  
To what extent do spatial features (lat/lon) dominate predictive signals?

### RQ5 — Physical Consistency Violation  
Do model predictions violate expected hydrological relationships?

### RQ6 — Failure Mode Structure  
What structured failure patterns emerge under distribution shift?

---

## 5. Hypotheses

- H1: Models exhibit shortcut learning even in in-domain evaluation  
- H2: Spatial shift leads to significant performance degradation  
- H3: Temporal shift exposes reliance on seasonal correlations  
- H4: Spatial features (lat/lon) dominate model predictions  
- H5: Models violate expected hydrological monotonicity relationships  
- H6: Failure modes are structured rather than random  

---

## 6. Dataset Design

### 6.1 Spatio-Temporal Unit

Each sample represents a spatial location at a specific time:

```
(lat, lon, date) → feature vector → flood label
```

---

### 6.2 Features

**Environmental**
- rainfall
- rainfall_3day
- rainfall_7day

**Topographic**
- elevation
- slope

**Land**
- landuse

**Hydrological**
- distance_river

**Spatial (diagnostic only)**
- lat
- lon

---

### 6.3 Target Variable

- flood = 1 (flood event)
- flood = 0 (non-flood)

---

### 6.4 Dataset Structure

| lat | lon | date | rainfall | rainfall_3day | rainfall_7day | elevation | slope | landuse | distance_river | flood | region |

Primary key:

```
(lat, lon, date)
```

---

### 6.5 Temporal Sampling Strategy

- Event-based sampling using flood occurrences  
- Pre-flood window (3–7 days before event)  
- Flood event day labeled as positive class  

---

### 6.6 Temporal Coverage

- 2018 – 2020: Training set  
- 2021 – 2022: Testing set  

---

## 7. Data Sources

- Rainfall: CHIRPS / NASA  
- Elevation: SRTM (DEM)  
- Land use: ESA WorldCover  
- River network: OpenStreetMap  
- Flood labels: Sentinel-1 SAR (Google Earth Engine)  

---

## 8. Methodology Pipeline

### Step 1 — Data Collection  
Collect multi-source geospatial datasets.

### Step 2 — Flood Label Generation  
- Use Sentinel-1 SAR imagery  
- Detect water extent changes between pre-event and flood periods  
- Generate binary flood labels  

### Step 3 — Preprocessing  
- Spatial alignment  
- Missing value handling  
- Normalization  

### Step 4 — Feature Engineering  
- Rainfall aggregation (3-day, 7-day)  
- Slope computation from DEM  
- Distance to river calculation  
- Land use encoding  

### Step 5 — Model Training  
- Random Forest  
- XGBoost  

### Step 6 — Diagnostic Evaluation  
Instead of only predictive accuracy, evaluate:

- in-domain performance  
- spatial shift performance  
- temporal shift performance  
- feature dependency (ablation)  
- physical consistency checks  

---

## 9. Experimental Design: Multi-Layer Evidence Framework

We construct a **multi-layer diagnostic framework** combining observational, shift-based, interventional, and counterfactual evidence to detect spatio-temporal shortcut learning.

---

### LAYER 1 — Observational Baseline

#### Experiment 1.1 — In-Domain Baseline  
Train and test within Makassar (2018–2020 → 2021–2022)
- **Purpose:** Establish baseline performance ceiling
- **Output:** AUC, F1, confusion matrix

#### Experiment 1.2 — Sub-Region Holdout  
Train on Makassar subregion → test on held-out subregion
- **Purpose:** Internal spatial validation (short-range shift)
- **Output:** Performance within-region vs across-region

---

### LAYER 2 — Natural Distribution Shift

#### Experiment 2.1 — Spatial Shift Test  
Train on Makassar → test on Jakarta
- **Purpose:** Detect geographic memorization under cross-regional shift
- **Expected:** Large AUC drop if model learns lat/lon encoding

#### Experiment 2.2 — Temporal Shift Test  
Train 2018–2020 → test 2021–2022
- **Purpose:** Detect seasonal shortcuts under temporal distribution shift
- **Expected:** AUC drop if model exploits seasonal correlations

#### Experiment 2.3 — Distance-Based Split  
Train on near-region cells → test on far-region cells
- **Purpose:** Quantify performance degradation as function of geographic distance
- **Output:** AUC vs distance curve

---

### LAYER 3 — Intervention Experiments (Q1-Critical)

#### Experiment 3.1 — Spatial Perturbation Test  
Add controlled noise to geographic coordinates.

| Noise Level | Magnitude | Purpose |
|-------------|-----------|---------|
| Small | ±100m | Minimal geographic shift |
| Medium | ±1km | Local neighborhood change |
| Large | ±5km | Regional scale shift |

**Procedure:**
1. Perturb lat/lon: `(lat', lon') = (lat + ε, lon + ε)`
2. Keep all other features fixed
3. Measure AUC degradation

**Expected:** If model relies on coordinate memorization, even small perturbations cause large accuracy drops.

---

#### Experiment 3.2 — Spatial Shuffle Test (Region Break)  
Shuffle grid cells within meaningful geospatial contexts.

**Procedure:**
1. **Shuffle A:** Swap coordinates within Makassar (preserve physical features)
2. **Shuffle B:** Swap coordinates between similar elevation zones (preserve physical similarity)
3. **Shuffle C:** Random global shuffle (destroy all spatial structure)

**Expected:** 
- Shuffle A: Moderate drop (location encoding violated)
- Shuffle B: Small drop (physical similarity preserved)
- Shuffle C: Severe drop (all spatial structure lost)

---

#### Experiment 3.3 — Feature Intervention Dose Test  
Systematically vary feature combinations.

| Configuration | Features Included | Purpose |
|---------------|------------------|---------|
| Full | All 11 features | Baseline |
| No-Spatial | Remove lat/lon | Isolate physical features |
| Spatial-Only | Only lat/lon | Pure geographic encoding |
| No-Physical | Remove rainfall, elevation, river dist | Spatial + land use only |
| Rainfall-Only | Only rainfall | Single dominant physical feature |

**Expected:** Measure feature importance via AUC difference between configurations.

---

#### Experiment 3.4 — Counterfactual Flood Test  
Generate synthetic samples with modified environmental features.

**Procedure:**

For each real flood event (lat, lon, date):

1. Create synthetic non-flood by perturbing:
   - Rainfall: reduce by 50%
   - Elevation: increase by 100m
   - River distance: increase by 1km

2. Create synthetic flood by perturbing non-flood:
   - Rainfall: increase by 50%
   - Elevation: decrease by 100m
   - River distance: decrease by 1km

3. Measure model's prediction change

**Expected:** If model understands physical relationships, counterfactual perturbations should align with expected flood probability change.

---

### LAYER 4 — Counterfactual Logic Tests

#### Experiment 4.1 — Monotonicity Test  
Verify whether model predictions follow expected hydrological laws.

**Physical Rules (Must Hold):**
- Rainfall ↑ → Flood probability ↑
- Elevation ↑ → Flood probability ↓
- River distance ↑ → Flood probability ↓
- Slope ↑ → Flood probability ↓ (water drains faster)

**Procedure:**
1. For each sample, vary one feature incrementally
2. Record prediction response
3. Compute violation rate: % predictions violating monotonicity

**Expected:** Low violation rate (< 10%) indicates physical consistency.

---

#### Experiment 4.2 — Causal Consistency Score  
Quantify model compliance with physical causal relationships.

$$C = \frac{\text{# predictions consistent with physical laws}}{\text{# total predictions}} \times 100\%$$

**Procedure:**
1. For each sample: apply counterfactual perturbation
2. Compute expected direction of prediction change (from physics)
3. Compare with actual model prediction change
4. Aggregate consistency rate

**Interpretation:**
- C = 100%: Perfect physical alignment
- C = 50%: Random with respect to physics
- C < 50%: Anti-aligned with physics (shortcut learning evidence)

---

## Summary: Four-Layer Diagnostic Framework

```
LAYER 1 — OBSERVATIONAL
├─ In-domain baseline (AUC_in)
└─ Sub-region holdout

LAYER 2 — NATURAL SHIFT
├─ Spatial shift: Makassar → Jakarta (AUC_spatial)
├─ Temporal shift: 2018–2020 → 2021–2022 (AUC_temporal)
└─ Distance-based split (AUC vs distance)

LAYER 3 — INTERVENTIONS (Q1-CRITICAL)
├─ Spatial perturbation (noise injection)
├─ Spatial shuffle (region break test)
├─ Feature intervention (dose test)
└─ Counterfactual generation (synthetic samples)

LAYER 4 — COUNTERFACTUAL LOGIC
├─ Monotonicity test (law violations)
└─ Causal consistency score (C metric)
```

---

## Shortcut Learning Detection via Multi-Layer Evidence

**Primary Detection Logic:**

```
IF (AUC_spatial << AUC_in) AND
   (AUC_shift_perturbation << AUC_baseline) AND
   (Causal_Consistency_Score < 50%) AND
   (Feature_Importance(lat/lon) > Feature_Importance(rainfall))
THEN model exhibits strong spatial shortcut learning
```

**Evidence Strength Ranking:**
1. **Strongest:** Counterfactual logic + monotonicity violation
2. **Strong:** Spatial perturbation + feature intervention
3. **Moderate:** Spatial shift + distance-based split
4. **Baseline:** In-domain vs shift comparison

---

## 10. Shortcut Learning Quantification

### Shortcut Learning Score

```
S = (AUC_in-domain - AUC_shift) / AUC_in-domain
```

---

### Decomposed Form

```
S = S_spatial + S_temporal + S_feature
```

Where:
- S_spatial = degradation under regional shift  
- S_temporal = degradation under temporal shift  
- S_feature = degradation after removing spatial features  

---

## 11. Failure Mode Taxonomy

| Type | Definition | Signature |
|------|------------|----------|
| Spatial Memorization Failure | Over-reliance on geographic coordinates | High lat/lon importance + spatial shift drop |
| Temporal Shortcut Failure | Dependence on seasonal patterns | Performance drop across years |
| Hydrological Inconsistency Failure | Violates physical relationships | Rainfall ↑ but flood ↓ |
| Feature Proxy Dominance | Non-physical features dominate prediction | Lat/lon > rainfall importance |

---

## 12. Analysis Framework

The analysis is structured into three layers:

### Layer 1 — Behavioral Shift
Performance degradation under spatial and temporal shifts.

### Layer 2 — Shortcut Dependency
Feature attribution analysis (SHAP + ablation).

### Layer 3 — Structural Failure Mechanisms
Categorization of failure modes into interpretable types.

---

## 13. Expected Findings

- Evidence of spatio-temporal shortcut learning in in-domain models  
- Significant performance degradation under distribution shift  
- Strong dependence on spatial proxy variables (lat/lon)  
- Violations of hydrological consistency  
- Structured failure patterns under shift conditions  

---

## 14. Contributions

- A quantitative framework for diagnosing shortcut learning in geospatial ML systems  
- A cross-regional and temporal evaluation protocol for flood prediction models  
- A failure mode taxonomy for machine learning in hydrological applications  
- Empirical evidence that flood prediction models rely on non-physical correlations under distribution shift  

---

## 15. Risks and Mitigation

### Risks
- Noise in Sentinel-1 flood labeling  
- Class imbalance in flood events  
- Missing or inconsistent geospatial data  

### Mitigation
- Multi-source validation  
- Balanced sampling strategies  
- Noise filtering in SAR-based labeling  

---

## 16. Core Insight

This research reframes flood prediction from a purely predictive task into a **diagnostic framework for understanding model behavior under distribution shift**, aiming to determine whether machine learning systems learn physical processes or spatio-temporal shortcuts.

---

## Final Note

The key challenge is not building a predictive model, but rigorously quantifying what the model actually learns under distribution shift.
