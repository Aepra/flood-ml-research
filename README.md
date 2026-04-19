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

## Dataset Design

This project uses a **spatio-temporal dataset**, where each row represents:

> A specific location at a specific time

---

### Dataset Structure

| lat | lon | date | rainfall | rainfall_3day | rainfall_7day | elevation | slope | landuse | distance_river | flood | region |
|-----|-----|------|----------|----------------|----------------|-----------|--------|----------|----------------|--------|--------|

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

- Time range: **2018 – 2022**

### Data Split

- Train: 2018–2020  
- Test: 2021–2022  

---

## Research Challenges

- Flood events are **spatially heterogeneous**  
- Flood duration varies across locations  
- Labels derived from SAR imagery may contain noise  
- Strong **distribution shift** between regions  
- Temporal patterns differ across years  

---

## Project Structure

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

---

## Methodology

1. Data Collection  
2. Flood Label Generation  
3. Preprocessing  
4. Feature Engineering  
5. Modeling (Random Forest, XGBoost)  
6. Evaluation  

---

## Experimental Design

- Baseline (in-domain)  
- Cross-region generalization  
- Temporal generalization  
- Feature importance analysis  
- Spatial bias test  
- Error analysis  
- Sensitivity analysis  

---

## Installation

git clone https://github.com/Aepra/flood-ml-research.git  
cd flood-ml-research  
pip install -r requirements.txt  

---

## Usage

python main.py  

---

## Final Note

The hardest part of this research is not building the model, but:

- Interpreting results  
- Understanding model behavior  
- Drawing meaningful conclusions  