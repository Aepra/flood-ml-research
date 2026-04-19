# Flood Prediction using Machine Learning and Geospatial Data

## Overview

This repository contains a research-driven project focused on evaluating the **generalization**, **temporal robustness**, and **spatial bias** of machine learning models for flood prediction using multi-source geospatial data.

Unlike conventional flood prediction systems that focus solely on maximizing predictive accuracy, this study aims to answer a more fundamental question:

> Do machine learning models truly learn the physical processes of flooding, or do they rely on spatio-temporal shortcuts such as location and seasonal patterns?

---

## Research Motivation

Most flood prediction models are evaluated within a single region and time period, resulting in models that:

- Perform well locally but fail in new regions  
- Overfit to spatial patterns (e.g., coordinates)  
- Fail to generalize across time (different years)  

This project addresses these limitations by explicitly evaluating:

- Cross-region generalization (Makassar → Jakarta)  
- Cross-year generalization (2018–2020 → 2021–2022)  
- Model interpretability and feature importance  
- Spatial bias and reliance on geographic coordinates  
- Failure modes and robustness  

---
## Problem Statement

Despite the increasing use of machine learning for flood prediction, it remains unclear whether these models:

- Learn physically meaningful relationships between environmental variables  
- Or rely on spatio-temporal shortcuts such as geographic location and seasonal patterns  

This lack of understanding raises concerns about the reliability and generalizability of such models in real-world deployment.

---



## Core Contribution

This research contributes by:

- Providing empirical evidence of **spatial bias** in geospatial machine learning models  
- Evaluating model generalization across both **space and time**  
- Demonstrating the limitations of conventional flood prediction approaches  
- Proposing a **spatio-temporal experimental framework** for evaluating model behavior  

---

## Study Areas

- **Training Region:** Makassar, Indonesia  
- **Testing Region:** Jakarta, Indonesia  

---

### Rationale for Region Selection

Makassar and Jakarta are selected because:

- Both are flood-prone urban areas  
- They exhibit different topographic and hydrological characteristics  
- Data availability is relatively consistent across both regions  

This enables controlled evaluation of spatial generalization under realistic conditions.

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