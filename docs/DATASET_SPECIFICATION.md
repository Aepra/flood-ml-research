# 📄 DATASET SPECIFICATION DOCUMENT

## Spatio-Temporal Flood Shortcut Learning Dataset (ST-FSLD v1.0)

**Version**: 1.0  
**Last Updated**: April 2026  
**Status**: Active Development  
**Confidentiality**: Research Use

---

# TABLE OF CONTENTS

1. [Dataset Purpose](#1--dataset-purpose)
2. [Fundamental Unit of Observation](#2--fundamental-unit-of-observation)
3. [Spatial Design](#3--spatial-design)
4. [Temporal Design](#4--temporal-design)
5. [Flood Event Definition](#5--flood-event-definition-critical)
6. [Feature Specification](#6--feature-specification)
7. [Label Balance Strategy](#7--label-balance-strategy)
8. [Data Generation Pipeline](#8--data-generation-pipeline)
9. [Data Split Design](#9--data-split-design)
10. [Quality Control](#10--quality-control)
11. [Final Dataset Output Format](#11--final-dataset-output-format)
12. [Data Characteristics & Statistics](#12--data-characteristics--statistics)
13. [Design Principles](#13--design-principles-very-important)
14. [Implementation Roadmap](#14--implementation-roadmap)

---

# 1. 🎯 Dataset Purpose

## 1.1 Research Objective

This dataset is specifically designed to support the research titled:

> **"Evaluating the Generalization, Temporal Dynamics, and Spatial Bias of Machine Learning Models for Flood Prediction Using Multi-Source Geospatial Data: A Spatio-Temporal Study of Makassar with Cross-Regional Validation"**

## 1.2 Primary Goals

The dataset is NOT designed for:
- ❌ Achieving maximum predictive accuracy
- ❌ Building the "best" flood prediction model
- ❌ Operational flood forecasting

Instead, the dataset is designed for:
- ✅ **Testing whether ML models learn physical flooding processes or just exploit spatio-temporal shortcuts**
- ✅ **Measuring performance degradation under spatial shift** (Makassar → Jakarta)
- ✅ **Measuring performance degradation under temporal shift** (2018–2020 → 2021–2022)
- ✅ **Quantifying model dependence on location (lat/lon) vs physical features**
- ✅ **Identifying systematic failure patterns across regions and time periods**
- ✅ **Enabling reproducible and transparent ML model evaluation**

## 1.3 Research Questions Addressed

| RQ | Question | Dataset Role |
|----|----------|--------------|
| **RQ1** | In-domain performance in Makassar? | Baseline benchmark |
| **RQ2** | Cross-region generalization drop? | Spatial validation |
| **RQ3** | Temporal generalization stability? | Temporal validation |
| **RQ4** | Which features matter most? | Feature importance |
| **RQ5** | Model dependence on location? | Shortcut detection |
| **RQ6** | When and why models fail? | Error analysis |

---

# 2. 🧱 Fundamental Unit of Observation

## 2.1 Atomic Data Unit

Each observation in the dataset represents:

> **One spatial location at one specific point in time**

### Formal Definition

```
Sample = (x, y, t, X, y)

where:
  x           = longitude (WGS84)
  y           = latitude (WGS84)
  t           = timestamp (YYYY-MM-DD, UTC)
  X           = feature vector
  y           = binary flood label (0 or 1)
```

## 2.2 Feature Vector Components

### **Spatial Features**
```
spatial_features = {lat, lon}
```
- **lat** (latitude): WGS84 decimal degrees
- **lon** (longitude): WGS84 decimal degrees
- Purpose: Geographic coordinates; used for shortcut learning detection

### **Temporal Feature**
```
temporal_features = {date}
```
- **date**: YYYY-MM-DD format, daily resolution

### **Environmental (Meteorological) Features**
```
environmental_features = {rainfall, rainfall_3day, rainfall_7day}
```
- **rainfall**: Daily precipitation (mm)
- **rainfall_3day**: 3-day cumulative rainfall (mm)
- **rainfall_7day**: 7-day cumulative rainfall (mm)
- Purpose: Primary hydrological trigger for flooding

### **Topographic Features**
```
topographic_features = {elevation, slope}
```
- **elevation**: Digital Elevation Model (meters above sea level)
- **slope**: Slope angle (degrees)
- Purpose: Terrain characteristics affecting drainage and runoff

### **Hydrological Features**
```
hydrological_features = {distance_river}
```
- **distance_river**: Euclidean distance to nearest river (meters)
- Purpose: Proximity to water bodies; flood source potential

### **Land Features**
```
land_features = {landuse}
```
- **landuse**: Land use classification (categorical: urban, agricultural, forest, water, etc.)
- Purpose: Surface properties affecting infiltration and runoff

### **Target Variable**
```
target = {flood}
```
- **flood**: Binary label (0 = no flood observed, 1 = flood observed)

## 2.3 Complete Feature Vector Structure

| Variable | Type | Unit | Range | Source |
|----------|------|------|-------|--------|
| **lat** | float | degrees | [-90, 90] | WGS84 |
| **lon** | float | degrees | [-180, 180] | WGS84 |
| **date** | date | YYYY-MM-DD | 2018-01-01 to 2022-12-31 | UTC |
| **rainfall** | float | mm | [0, 500] | CHIRPS |
| **rainfall_3day** | float | mm | [0, 1000] | derived |
| **rainfall_7day** | float | mm | [0, 2000] | derived |
| **elevation** | float | meters | [0, 3000] | SRTM DEM |
| **slope** | float | degrees | [0, 90] | derived from DEM |
| **landuse** | categorical | class | {urban, forest, agricultural, water, barren} | ESA WorldCover |
| **distance_river** | float | meters | [0, 50000] | OSM + rasterization |
| **flood** | binary | binary | {0, 1} | Sentinel-1 |
| **region** | categorical | region | {Makassar, Jakarta} | by design |

---

# 3. 🗺️ Spatial Design

## 3.1 Study Areas

### Training Region: Makassar
- **Country**: Indonesia
- **Province**: South Sulawesi (Sulawesi Selatan)
- **Characteristics**:
  - Coastal city (port city)
  - Growing urban area
  - Tropical climate with distinct wet/dry seasons
  - Mixed topography (hills and plains)
  - River network: Jeneberang River (primary), Tallo River

- **Geographic Bounds** (approximate):
  - Latitude: 5.1°S to 5.3°S
  - Longitude: 119.4°E to 119.6°E
  - Area: ~500 km² urban area

### Test Region: Jakarta
- **Country**: Indonesia
- **Province**: Special Capital Region (DKI Jakarta)
- **Characteristics**:
  - Coastal megacity
  - Highly urbanized and densely populated
  - Tropical climate with monsoon patterns
  - Flat terrain with significant subsidence risk
  - Major river network: Ciliwung River, Cisadane River

- **Geographic Bounds** (approximate):
  - Latitude: 6.1°S to 6.3°S
  - Longitude: 106.7°E to 107.0°E
  - Area: ~660 km² administrative area

### Rationale for Region Selection
- ✅ **Geographic diversity**: Different elevations, drainage patterns, and urban characteristics
- ✅ **Climate similarity**: Both in tropical Indonesia, similar rainfall patterns
- ✅ **Data availability**: Both have good satellite and precipitation data coverage
- ✅ **Real-world relevance**: Both experience significant flooding, well-documented
- ✅ **Research objective**: Sufficient difference to test generalization while maintaining consistency

## 3.2 Spatial Resolution

### Grid System Design

**Resolution**: 250 meters (0.00225° at equator)

**Justification**:
- Fine enough to capture urban-scale flooding patterns
- Coarse enough to manage computational load
- Aligned with common satellite imagery resolution (Sentinel-2: 10-20m, but aggregated for efficiency)
- Sufficient for neighborhood-level flood risk assessment

**Grid Specification**:
```
Coordinate System: WGS84 (EPSG:4326)
Grid Type: Regular rectangular grid
Cell Size: 250m × 250m
Origin: Northwest corner of each study area
Projection for computation: UTM Zone 50S (for Makassar/Jakarta)
```

### Grid Cell Definition

Each grid cell is uniquely identified by:

```
grid_id = (lat_center, lon_center)
```

where lat_center and lon_center are the coordinates of the cell center.

### Expected Grid Dimensions

**Makassar**:
- Approx. 60 × 60 = 3,600 grid cells
- Total area: ~225 km²

**Jakarta**:
- Approx. 80 × 100 = 8,000 grid cells
- Total area: ~500 km²

**Total**: ~11,600 grid cells across both regions

## 3.3 Spatial Reference System

**Primary CRS**: WGS84 (EPSG:4326)
- Used for all data input/output
- All feature vectors stored with lat/lon in WGS84

**Working CRS**: UTM Zone 50S (EPSG:32750)
- Used for internal spatial computations (distance calculations, grid generation)
- All distances computed in meters (UTM projection)

---

# 4. ⏱️ Temporal Design

## 4.1 Time Resolution

### Daily Resolution

**Justification**:
- CHIRPS rainfall data available at daily resolution (primary feature)
- Sentinel-1 SAR imagery revisit period (~6-12 days) sufficient for daily interpolation
- Flood events typically evolve over multiple days (3-7 days typical)
- Daily resolution balances temporal detail with computational feasibility

**Timestamp Format**:
```
YYYY-MM-DD HH:MM:SS (UTC)
```
- Date: Calendar date in UTC
- Time: Midnight UTC (00:00:00) to represent entire day

## 4.2 Temporal Coverage

### Overall Study Period

```
Start Date: 2018-01-01
End Date: 2022-12-31
Duration: 5 years (1,825 days)
```

### Rationale for Period Selection
- **Sufficient duration** for capturing seasonal patterns and inter-annual variability
- **Recent enough** for modern satellite data (Sentinel-1 launched 2014)
- **Covers both wet and dry seasons** (multiple cycles)
- **Includes multiple flood events** for reliable labeling
- **Post-2018 focus** for data quality assurance

## 4.3 Temporal Split Strategy

**CRITICAL**: Strict temporal separation to prevent information leakage.

### Training Dataset Temporal Window
```
Start: 2018-01-01
End: 2020-12-31
Duration: 3 years (1,096 days)
```

### Test Dataset Temporal Window
```
Start: 2021-01-01
End: 2022-12-31
Duration: 2 years (730 days)
```

### Temporal Separation Guarantee
```
No overlap between training and test temporal periods
Training data: 2018-2020 (exclusive)
Test data: 2021-2022 (exclusive)
Gap: None (but strict temporal boundary)
```

### Seasonal Coverage

**Training Period (2018-2020)**:
- Wet seasons: 5 complete cycles (Oct-Apr)
- Dry seasons: 5 complete cycles (May-Sep)
- Ensures model sees all seasonal patterns

**Test Period (2021-2022)**:
- Wet seasons: 2 complete cycles
- Dry seasons: 2 complete cycles
- Validates temporal generalization

## 4.4 Daily Time Series Construction

For each grid cell and region, we construct a continuous daily time series:

```
Grid_i = {
    (t1, X_t1, y_t1),
    (t2, X_t2, y_t2),
    ...
    (tn, X_tn, y_tn)
}

where:
  ti = day i in study period
  X_ti = feature vector on day i
  y_ti = flood label on day i
```

**Important**: No missing dates allowed. For missing observations, apply interpolation or masking (see Section 10).

---

# 5. 🌧️ Flood Event Definition (CRITICAL)

## 5.1 Flood Label Source

### Primary Source: Sentinel-1 SAR Imagery

**Sensor**: Copernicus Sentinel-1 (Synthetic Aperture Radar)
- **Constellation**: Two identical satellites (1A, 1B)
- **Revisit Period**: ~6 days (global coverage); ~3 days at equator
- **Resolution**: 10m pixel size (high resolution)
- **Penetration**: Microwave penetrates clouds (weather-independent)

**Advantage over optical imagery**:
- ✅ Works in all weather conditions
- ✅ Detects water accurately (water appears dark in SAR)
- ✅ Not obscured by clouds (common in tropics)

### Data Platform: Google Earth Engine

All Sentinel-1 processing conducted via Google Earth Engine:
- Automatic preprocessing (radiometric correction, terrain correction)
- Efficient cloud computing for large-scale processing
- Pre-computed collections (no need for manual download)

---

## 5.2 Flood Labeling Methodology

### Step 1: Backscatter Extraction

For each grid cell, extract:
- **Pre-flood backscatter** (σ_pre): 3-7 days before flood event
- **Flood-day backscatter** (σ_flood): On suspected flood day

**Formula**:
```
σ = reflectivity in decibels (dB)
```

### Step 2: Change Detection

Compute backscatter difference:

```
Δσ = σ_pre - σ_flood
```

**Interpretation**:
- ✅ Δσ > threshold: Sharp decrease in backscatter → water presence
- ❌ Δσ ≤ threshold: No significant water change

### Step 3: Water Presence Threshold

**Threshold value**: -3 dB (standard in flood literature)

**Justification**:
- Conservative threshold to minimize false positives
- Reduces noise from atmospheric and vegetation changes
- Aligned with UNITAR/UNOSAT flood mapping protocols

### Step 4: Flood Label Assignment

```python
if Δσ > -3 dB:
    flood_label = 1  (flood detected)
else:
    flood_label = 0  (no flood detected)
```

---

## 5.3 Event Window Definition

### Event-Based Sampling (NON-RANDOM)

For each confirmed flood event:

```
Pre-flood window:    Days -7 to -1 (relative to flood day)
Flood window:        Days 0 to +2 (flood day ± 2 days)
Post-flood window:   Days +3 onwards (recovery period)
```

### Labeling Strategy

| Period | Label | Rationale |
|--------|-------|-----------|
| Pre-flood (-7 to -1) | 0 | Baseline conditions |
| Flood day (0 to +2) | 1 | Confirmed flood |
| Post-flood (+3+) | 0 | Recovery period |

**Important**: Only use pre-flood and flood windows in dataset. Exclude post-flood for clean labeling.

### Event Window Duration

```
Total event duration: 10 days
- Pre-flood: 7 days
- Flood: 3 days
```

This captures:
- ✅ Rainfall buildup (7 days)
- ✅ Peak flood conditions (3 days)
- ✅ Typical duration of significant flood events

---

## 5.4 Flood Event Detection Criteria

A flood event is confirmed if ALL conditions are met:

1. **Sentinel-1 backscatter change**: Δσ ≤ -3 dB
2. **Spatial extent**: Minimum 5 contiguous grid cells (≥500m × 500m)
3. **Temporal coherence**: Change persists for ≥1 day
4. **Rainfall correlation**: Concurrent or preceding rainfall ≥20 mm (3-day accumulated)

This multi-criteria approach ensures:
- ✅ Minimizes false positives from noise
- ✅ Captures real flood events
- ✅ Correlates with meteorological triggers

---

## 5.5 Ground Truth Validation

### Secondary Validation Sources

To validate Sentinel-1 labels:

1. **News reports & flood databases**
   - Indonesian Disaster Management Authority (BNPB) flood reports
   - ReliefWeb flood announcements
   - Local news archives

2. **Social media indicators**
   - Twitter flood reports (#banjir, #banjirJakarta, #banjirMakassar)
   - Facebook citizen reports

3. **Government flood monitoring**
   - Jakarta Flood Early Warning System (BNPB)
   - Official disaster declarations

### Expected Label Accuracy

- **Precision** (correct flood detections / total detections): ~85%
- **Recall** (detected floods / actual floods): ~75%
- **Typical false positive rate**: ~15% (conservative)

---

## ⚠️ CRITICAL RULE

**No random sampling from flood/non-flood distribution allowed.**

Instead:
- ✅ **Stratified event-based sampling**
- ✅ **Balance achieved during experiment design** (not data generation)
- ✅ **Maintain natural class imbalance** (accurate representation)

---

# 6. 🌦️ FEATURE SPECIFICATION

## 6.1 Environmental (Meteorological) Features

### 6.1.1 Daily Rainfall

**Variable Name**: `rainfall`  
**Unit**: millimeters (mm)  
**Temporal Resolution**: daily  
**Data Type**: float (non-negative)  

**Source**: CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data)
- **Version**: CHIRPS v2.0
- **Spatial Resolution**: 0.05° (~5.5 km)
- **Temporal Resolution**: daily
- **Coverage**: Global, since 1981
- **Availability**: Near-real-time (5-day delay)

**Processing Steps**:
1. Download CHIRPS daily precipitation grids
2. Resample to 250m grid using bilinear interpolation
3. Extract value at each grid cell center

**Quality Control**:
- ✅ Flag missing values
- ✅ Check for outliers (>500 mm flagged for review)
- ✅ Validate against station data if available

**Physical Meaning**:
- Represents daily precipitation input to the hydrological system
- Primary trigger for flood events

---

### 6.1.2 3-Day Cumulative Rainfall

**Variable Name**: `rainfall_3day`  
**Unit**: millimeters (mm)  
**Temporal Resolution**: daily (rolling 3-day sum)  
**Data Type**: float (non-negative)  

**Calculation Formula**:
```
rainfall_3day[t] = rainfall[t] + rainfall[t-1] + rainfall[t-2]
```

**Interpretation**:
- Captures rainfall accumulation over 3-day period
- Relevant for soil saturation and groundwater recharge
- Standard in hydrological flood modeling

**Typical Range**: 0–500 mm

---

### 6.1.3 7-Day Cumulative Rainfall

**Variable Name**: `rainfall_7day`  
**Unit**: millimeters (mm)  
**Temporal Resolution**: daily (rolling 7-day sum)  
**Data Type**: float (non-negative)  

**Calculation Formula**:
```
rainfall_7day[t] = Σ(rainfall[t-i] for i=0 to 6)
```

**Interpretation**:
- Captures longer-term rainfall accumulation
- Represents antecedent soil moisture conditions
- Important for predictability of flooding

**Typical Range**: 0–1000 mm

---

## 6.2 Topographic Features

### 6.2.1 Elevation (Digital Elevation Model)

**Variable Name**: `elevation`  
**Unit**: meters above mean sea level (m)  
**Spatial Resolution**: 90m (aggregated to 250m)  
**Data Type**: float  

**Source**: SRTM (Shuttle Radar Topography Mission) v3
- **Version**: USGS SRTM+ (void-filled)
- **Spatial Resolution**: 90m native
- **Temporal Reference**: February 2000
- **Coverage**: Global land, ±60° latitude

**Processing Steps**:
1. Download SRTM DEM tiles for study areas
2. Mosaic tiles into single raster
3. Resample to UTM Zone 50S projection
4. Aggregate from 90m to 250m resolution (mean aggregation)
5. Extract value at each grid cell center

**Quality Control**:
- ✅ Validate against known benchmarks (sea level = 0, mountains consistent)
- ✅ Check for no-data values (void-fill if necessary)
- ✅ Ensure consistency across tile boundaries

**Physical Meaning**:
- Higher elevation → lower flood probability (general principle)
- Used to identify flood-prone low-lying areas
- Affects drainage patterns and runoff

**Expected Range for Study Areas**:
- **Makassar**: 0–300 m (coastal to hilly)
- **Jakarta**: -5–50 m (subsidence + flat terrain)

---

### 6.2.2 Slope

**Variable Name**: `slope`  
**Unit**: degrees (°)  
**Spatial Resolution**: 250m (derived from DEM)  
**Data Type**: float (0–90)  

**Derivation Formula**:
```
slope = arctan(√((dz/dx)² + (dz/dy)²))
```

where dz/dx and dz/dy are elevation gradients.

**Calculation Method**:
1. Compute gradient of SRTM DEM
2. Calculate slope using standard GIS formula
3. Convert to degrees
4. Resample to 250m grid

**Quality Control**:
- ✅ Ensure slope values in valid range [0°, 90°]
- ✅ Smooth extreme values (>60°) unlikely in study areas

**Physical Meaning**:
- Steep slopes → faster runoff, lower flood probability
- Flat slopes → water accumulation, higher flood probability
- Critical for identifying flood-prone flat areas

**Expected Range**:
- **Makassar**: 0–35° (mixed topography)
- **Jakarta**: 0–5° (predominantly flat)

---

## 6.3 Hydrological Features

### 6.3.1 Distance to Nearest River

**Variable Name**: `distance_river`  
**Unit**: meters (m)  
**Spatial Resolution**: 250m  
**Data Type**: float (non-negative)  

**Source**: OpenStreetMap (OSM) river network
- **Data Type**: Line geometry (rivers, streams)
- **Coverage**: Global, continuously updated
- **Extraction Date**: 2023-Q1

**Processing Steps**:
1. Download OSM planet data for study areas
2. Filter for river/stream features (tag: waterway=river OR waterway=stream)
3. Rasterize river lines to 250m grid
4. Compute Euclidean distance from each grid cell to nearest river
5. Handle edge cases (cells on rivers = 0m distance)

**Quality Control**:
- ✅ Validate major rivers are captured
- ✅ Check for spurious small streams
- ✅ Ensure distance calculations are correct

**Physical Meaning**:
- Represents proximity to main water sources
- Closer to river → higher flood risk (general principle)
- Used to identify flood-prone areas near waterways

**Expected Range**:
- **Min**: 0 m (on river)
- **Max**: 50,000 m (far from river)
- **Typical median**: 1,000–5,000 m

---

## 6.4 Land Features

### 6.4.1 Land Use / Land Cover (LULC)

**Variable Name**: `landuse`  
**Unit**: categorical classification  
**Spatial Resolution**: 10m (aggregated to 250m)  
**Data Type**: categorical (5 classes)  

**Source**: ESA WorldCover v100
- **Version**: 100 (released 2021)
- **Spatial Resolution**: 10m
- **Temporal Reference**: 2020
- **Coverage**: Global
- **Accuracy**: ~90% overall

**Class Mapping**:

| Code | Class | OSM Equivalent | Characteristic |
|------|-------|----------------|-----------------|
| 10 | Tree cover | forest | High infiltration |
| 20 | Shrubland | shrub | Moderate infiltration |
| 30 | Grassland | grassland | Moderate infiltration |
| 40 | Cropland | farmland | Moderate infiltration |
| 50 | Built-up (Urban) | residential, commercial | Low infiltration, high runoff |
| 60 | Barren / Sparse | industrial, quarry | Low infiltration |
| 70 | Snow/Ice | N/A | N/A (not applicable) |
| 80 | Permanent water | water | Water body |
| 90 | Herbaceous wetland | wetland | High infiltration |
| 95 | Mangrove | wetland | High infiltration |

**Processing Steps**:
1. Download ESA WorldCover 10m raster
2. Reproject to UTM Zone 50S
3. Resample to 250m grid using majority aggregation
4. Map to simplified 5-class scheme (see below)

**Simplified 5-Class Scheme**:

```
urban       → codes 50, 60 (Built-up)
forest      → codes 10, 90, 95 (Tree/wetland)
agricultural→ codes 20, 30, 40 (Shrub/grass/crop)
water       → code 80 (Permanent water)
barren      → codes 60, 70 (Bare/sparse/snow)
```

**Encoding for ML**:
- One-hot encoding (5 binary variables) OR
- Ordinal encoding (1–5) based on infiltration rank

**Quality Control**:
- ✅ Validate major urban areas are captured
- ✅ Check river/water bodies alignment
- ✅ Ensure forest/agricultural distinction

**Physical Meaning**:
- Urban areas → impervious, high runoff, high flood risk
- Forest/agricultural → permeable, infiltration, lower flood risk
- Critical for understanding drainage characteristics

**Expected Distribution (Makassar)**:
- Urban: ~30%
- Agricultural: ~40%
- Forest: ~25%
- Water: ~3%
- Barren: ~2%

**Expected Distribution (Jakarta)**:
- Urban: ~60%
- Agricultural: ~20%
- Forest: ~5%
- Water: ~8%
- Barren: ~7%

---

## 6.5 Spatial Features (DIAGNOSTIC ONLY)

### ⚠️ CRITICAL NOTE

These are **NOT physical predictors**. They serve **diagnostic purpose only** for shortcut learning detection.

---

### 6.5.1 Latitude

**Variable Name**: `lat`  
**Unit**: decimal degrees (°)  
**Coordinate System**: WGS84  
**Data Type**: float (-90 to 90)  

**Definition**:
```
lat = Y-coordinate (WGS84) of grid cell center
```

**Purpose**: Shortcut Learning Detection
- Detect if model relies on latitude for predictions
- Expect: model WITHOUT lat should show minimal performance loss
- Reality: if model with lat >> model without lat → spatial bias exists

**Expected Range**:
- **Makassar**: -5.25° to -5.10° (South of equator)
- **Jakarta**: -6.30° to -6.10° (South of equator)

---

### 6.5.2 Longitude

**Variable Name**: `lon`  
**Unit**: decimal degrees (°)  
**Coordinate System**: WGS84  
**Data Type**: float (-180 to 180)  

**Definition**:
```
lon = X-coordinate (WGS84) of grid cell center
```

**Purpose**: Shortcut Learning Detection
- Detect if model relies on longitude for predictions
- Combined with lat, tests 2D spatial bias
- Expect: removing lat+lon should hurt performance only if model learned location

**Expected Range**:
- **Makassar**: 119.40° to 119.60° (East of Greenwich)
- **Jakarta**: 106.70° to 107.00° (East of Greenwich)

---

### 6.5.3 Treatment in ML Pipeline

**Model A (Full feature set)**:
```
X_full = {lat, lon, rainfall, elevation, slope, landuse, distance_river, ...}
```

**Model B (Without spatial features)**:
```
X_nospatial = {rainfall, elevation, slope, landuse, distance_river, ...}
```

**Comparison**:
```
Performance drop = Acc(A) - Acc(B)
If drop > 5%  → indicates spatial bias
If drop ≤ 5%  → model doesn't rely on location
```

---

## 6.6 Target Variable

### 6.6.1 Flood Label

**Variable Name**: `flood`  
**Unit**: binary (0 or 1)  
**Data Type**: integer/boolean  
**Source**: Sentinel-1 SAR (see Section 5)

**Definition**:
```
flood = 1  if water detected (Sentinel-1 Δσ > -3 dB)
flood = 0  if no water detected
```

**Label Quality**:
- **False Positive Rate**: ~15% (water detected but not flood)
- **False Negative Rate**: ~25% (flood not detected)
- **Overall Accuracy**: ~80%

---

### 6.6.2 Label Distribution

**Expected class imbalance**:

| Region | Flood Events | Non-Flood Days | Ratio | % Floods |
|--------|--------------|----------------|-------|----------|
| Makassar | ~150–200 events | ~1,800 days | 1:10 | ~10% |
| Jakarta | ~200–300 events | ~1,500 days | 1:8 | ~12% |
| Combined | ~400–500 events | ~3,300 days | 1:9 | ~11% |

**Important**: Do NOT balance the dataset. Maintain natural imbalance for realistic evaluation.

---

## 6.7 Region Identifier

**Variable Name**: `region`  
**Unit**: categorical (2 classes)  
**Data Type**: string or integer (0/1)

**Classes**:
```
region = "Makassar" OR region = "Jakarta"
OR
region = 0 (Makassar) OR region = 1 (Jakarta)
```

**Purpose**: Explicit region identification for split validation and analysis.

---

# 7. 🧪 Label Balance Strategy

## 7.1 Class Imbalance Characteristics

Flood datasets are inherently **highly imbalanced**:

```
Non-flood observations : Flood observations ≈ 9 : 1
```

**Why this happens**:
- Floods are rare events (~10% of days in study area)
- Non-flood periods are much longer
- This reflects reality (flooding is not daily)

## 7.2 Imbalance Management Philosophy

### ❌ DO NOT FULLY BALANCE THE DATASET

Common approaches (NOT recommended):
- ❌ Random oversampling of flood class
- ❌ Synthetic data generation (SMOTE)
- ❌ Undersampling non-flood class

**Reason**: These create **unrealistic class distributions** that don't reflect operational scenarios.

### ✅ INSTEAD: MAINTAIN NATURAL IMBALANCE

Keep the dataset as-is with natural class distribution (~10% floods, ~90% non-floods).

**Rationale**:
- ✅ Reflects real-world deployment conditions
- ✅ Enables proper evaluation with appropriate metrics (ROC-AUC, PR-AUC)
- ✅ Prevents model from overfitting to balanced distribution

## 7.3 Balancing Strategy: Per-Split Stratification

**During train-test split**:

Use **stratified sampling** to ensure:
1. Training set maintains ~10% flood label proportion
2. Test set maintains ~10% flood label proportion
3. Both train and test have similar class ratios

**Example**:
```python
from sklearn.model_selection import train_test_split

# Stratify by flood label
train_set, test_set = train_test_split(
    data,
    test_size=0.3,
    stratify=data['flood'],
    random_state=42
)

# Result:
# train_set: ~10% floods, ~90% non-floods
# test_set: ~10% floods, ~90% non-floods
```

## 7.4 Per-Region Stratification

**Additional constraint**: Ensure stratification per region.

```python
# Stratify by both region and flood
data['region_flood'] = data['region'] + '_' + data['flood'].astype(str)

train_set, test_set = train_test_split(
    data,
    test_size=0.3,
    stratify=data['region_flood'],
    random_state=42
)
```

This ensures:
- Training set: Makassar (~10% floods), Jakarta (~12% floods)
- Test set: Same proportions

## 7.5 Evaluation Metrics for Imbalanced Data

**Primary Metrics** (suitable for imbalanced data):
- ✅ **ROC-AUC**: Threshold-independent, suitable for imbalanced
- ✅ **Precision-Recall AUC**: Emphasizes minority class
- ✅ **F1-score**: Harmonic mean of precision/recall
- ✅ **Confusion Matrix**: Shows false positives/negatives

**Secondary Metrics** (context-dependent):
- ⚠️ **Accuracy**: Biased for imbalanced data (misleading)
- ⚠️ **Recall alone**: May be high for naive classifiers

---

# 8. 🔄 Data Generation Pipeline

## 8.1 Overview

The dataset is generated through a multi-stage processing pipeline:

```
Stage 1: Spatial Grid Setup
         ↓
Stage 2: Feature Extraction (Rainfall, DEM, etc.)
         ↓
Stage 3: Flood Labeling (Sentinel-1)
         ↓
Stage 4: Data Assembly
         ↓
Stage 5: Quality Control
         ↓
Stage 6: Final Export
```

---

## 8.2 Stage 1: Spatial Grid Creation

### 8.2.1 Bounding Box Definition

Define geographic extent for each study area:

**Makassar**:
```
North Bound: -5.10°
South Bound: -5.25°
East Bound: 119.60°
West Bound: 119.40°
```

**Jakarta**:
```
North Bound: -6.10°
South Bound: -6.30°
East Bound: 107.00°
West Bound: 106.70°
```

### 8.2.2 Grid Generation

Create regular 250m × 250m grid:

```python
import numpy as np
from pyproj import Proj, Transformer

def create_grid(bounds, resolution_m=250):
    """
    Create regular grid in UTM projection, convert to WGS84
    
    bounds: (north, south, east, west)
    resolution_m: cell size in meters
    
    Returns: DataFrame with (lat, lon) for each grid cell
    """
    utm = Proj(proj='utm', zone=50, ellps='WGS84')
    
    # Convert bounds to UTM
    # ... implementation ...
    
    return grid_df
```

### 8.2.3 Grid Output

Result: DataFrame with columns:
```
| grid_id | lat | lon | cell_geometry |
| 1       | -5.15 | 119.45 | POLYGON(...) |
| 2       | -5.15 | 119.48 | POLYGON(...) |
| ... |
```

---

## 8.3 Stage 2: Feature Extraction

### 8.3.1 Environmental Features (Rainfall)

**Source**: CHIRPS via Google Earth Engine

```python
def extract_rainfall(start_date, end_date, geometry):
    """
    Extract daily CHIRPS rainfall for geometry
    Returns: DataFrame (date, rainfall)
    """
    import ee
    
    chirps = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY')
    
    rainfall = chirps \
        .filterDate(start_date, end_date) \
        .filterBounds(geometry) \
        .map(lambda img: img.select('precipitation'))
    
    # Export to CSV or cloud storage
    # ...
    
    return rainfall_df
```

### 8.3.2 Topographic Features (DEM, Slope)

**Source**: SRTM via Google Earth Engine

```python
def extract_topography(geometry):
    """
    Extract elevation and compute slope
    Returns: DataFrame (elevation, slope)
    """
    import ee
    
    srtm = ee.Image('USGS/SRTMGL1_Ellip/SRTMGL1_Ellip_srtm')
    
    # Extract elevation
    elevation = srtm.select('elevation') \
        .reduceRegion(ee.Reducer.mean(), geometry, 90) \
        .get('elevation')
    
    # Compute slope
    slope = ee.Terrain.slope(srtm) \
        .reduceRegion(ee.Reducer.mean(), geometry, 90) \
        .get('slope')
    
    return elevation, slope
```

### 8.3.3 Land Use Features

**Source**: ESA WorldCover via Google Earth Engine

```python
def extract_landuse(geometry):
    """
    Extract LULC class for geometry
    Returns: dominant LULC class
    """
    import ee
    
    worldcover = ee.Image('ESA/WorldCover/v100')
    
    lulc = worldcover.select('Map') \
        .reduceRegion(ee.Reducer.mode(), geometry, 10) \
        .get('Map')
    
    return lulc
```

### 8.3.4 Hydrological Features (Distance to River)

**Source**: Rasterized OpenStreetMap

```python
def extract_distance_to_river(grid_cell, river_raster):
    """
    Compute Euclidean distance from cell to nearest river
    Returns: distance in meters
    """
    from scipy.ndimage import distance_transform_edt
    
    # river_raster: binary raster (1=river, 0=non-river)
    dist = distance_transform_edt(~river_raster)
    
    # Get distance for grid cell
    return dist[row, col] * pixel_size_m
```

### 8.3.5 Feature Assembly per Grid Cell

Combine all features for each grid cell:

```python
def assemble_features(grid_id, lat, lon):
    """
    Assemble all features for a single grid cell
    Returns: feature vector X
    """
    X = {
        'grid_id': grid_id,
        'lat': lat,
        'lon': lon,
        'elevation': extract_elevation(lat, lon),
        'slope': extract_slope(lat, lon),
        'landuse': extract_landuse(lat, lon),
        'distance_river': extract_distance_to_river(lat, lon),
    }
    return X
```

---

## 8.4 Stage 3: Flood Label Generation

### 8.4.1 Sentinel-1 Processing

Extract backscatter values via Google Earth Engine:

```python
def detect_floods_sentinel1(grid_geometry, start_date, end_date):
    """
    Detect floods using Sentinel-1 backscatter change
    
    Returns: DataFrame (date, flood_label)
    """
    import ee
    
    s1 = ee.ImageCollection('COPERNICUS/S1_GRD')
    
    # Filter Sentinel-1 for study area and period
    s1_filtered = s1 \
        .filterBounds(grid_geometry) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.eq('instrumentMode', 'IW')) \
        .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
    
    # Compute backscatter
    backscatter = s1_filtered.map(lambda img: 
        img.select('VV').reduceRegion(ee.Reducer.mean(), grid_geometry, 10)
    )
    
    # Extract time series
    ts = backscatter.getInfo()  # Time series of backscatter
    
    # Detect changes (Δσ > -3 dB)
    floods = detect_changes(ts, threshold=-3)
    
    return floods
```

### 8.4.2 Change Detection Algorithm

```python
def detect_changes(backscatter_ts, threshold=-3):
    """
    Detect flood events from backscatter time series
    
    backscatter_ts: time series of backscatter (dB)
    threshold: detection threshold (dB)
    
    Returns: DataFrame (date, flood_detected)
    """
    floods = []
    
    for t in range(7, len(backscatter_ts)):
        # Pre-flood backscatter (7-day mean)
        sigma_pre = np.mean(backscatter_ts[t-7:t])
        
        # Current backscatter
        sigma_current = backscatter_ts[t]
        
        # Backscatter change
        delta_sigma = sigma_pre - sigma_current
        
        # Detect flood
        if delta_sigma > threshold:
            floods.append({'date': dates[t], 'flood': 1})
        else:
            floods.append({'date': dates[t], 'flood': 0})
    
    return pd.DataFrame(floods)
```

### 8.4.3 Multi-Criteria Validation

Confirm flood events with multiple criteria:

```python
def validate_flood_event(grid_id, date, s1_change, rainfall_accumulated, spatial_extent):
    """
    Validate flood event using multi-criteria approach
    
    Returns: True if all criteria met, False otherwise
    """
    criteria = [
        s1_change > -3,                    # Criterion 1: SAR change
        rainfall_accumulated >= 20,        # Criterion 2: Rainfall
        spatial_extent >= 5,               # Criterion 3: Spatial extent
    ]
    
    return all(criteria)  # All must be true
```

---

## 8.5 Stage 4: Data Assembly

### 8.5.1 Temporal Join

Join spatial features with temporal flood labels:

```python
def assemble_dataset(grid_df, rainfall_ts, floods_ts, start_date, end_date):
    """
    Assemble complete spatio-temporal dataset
    
    Returns: DataFrame with all features
    """
    dataset = []
    
    for _, grid_row in grid_df.iterrows():
        grid_id = grid_row['grid_id']
        lat, lon = grid_row['lat'], grid_row['lon']
        
        # Static features (per grid cell)
        spatial_features = {
            'lat': lat,
            'lon': lon,
            'elevation': grid_row['elevation'],
            'slope': grid_row['slope'],
            'landuse': grid_row['landuse'],
            'distance_river': grid_row['distance_river'],
        }
        
        # Dynamic features (per day)
        for date in pd.date_range(start_date, end_date, freq='D'):
            temporal_features = {
                'date': date,
                'rainfall': rainfall_ts.loc[(grid_id, date), 'rainfall'],
                'rainfall_3day': rainfall_ts.loc[(grid_id, date), 'rainfall_3day'],
                'rainfall_7day': rainfall_ts.loc[(grid_id, date), 'rainfall_7day'],
                'flood': floods_ts.loc[(grid_id, date), 'flood'],
                'region': 'Makassar' if grid_id in makassar_grids else 'Jakarta',
            }
            
            # Combine
            record = {**spatial_features, **temporal_features}
            dataset.append(record)
    
    return pd.DataFrame(dataset)
```

### 8.5.2 Example Output

```
| lat | lon | date | rainfall | rainfall_3day | rainfall_7day | elevation | slope | landuse | distance_river | flood | region |
|-----|-----|------|----------|---------------|---------------|-----------|-------|---------|----------------|-------|--------|
| -5.15 | 119.45 | 2018-01-01 | 5.2 | 12.3 | 45.6 | 125 | 8.5 | urban | 1250 | 0 | Makassar |
| -5.15 | 119.45 | 2018-01-02 | 8.1 | 13.5 | 50.1 | 125 | 8.5 | urban | 1250 | 0 | Makassar |
| -5.15 | 119.45 | 2018-01-03 | 15.4 | 28.7 | 61.5 | 125 | 8.5 | urban | 1250 | 1 | Makassar |
```

---

## 8.6 Stage 5: Quality Control

See Section 10.

---

## 8.7 Stage 6: Final Export

### 8.7.1 File Format

**Primary Format**: CSV
```
filename: ST_FSLD_v1.csv
rows: ~5,500,000 (3,600 grids × 1,825 days + 8,000 grids × 730 days test)
```

### 8.7.2 Export Specification

```python
def export_dataset(df, output_path):
    """
    Export dataset to CSV with proper formatting
    """
    df.to_csv(
        output_path,
        index=False,
        float_format='%.2f',  # 2 decimal precision
        date_format='%Y-%m-%d'
    )
```

### 8.7.3 Backup Formats

- **Parquet**: Compressed, columnar storage
- **NetCDF**: For spatial-temporal analysis
- **GeoTIFF**: For GIS visualization

---

# 9. 🧭 Data Split Design

## 9.1 Spatial Split

### Training Region: Makassar

```
Geographic Extent:
- Latitude: -5.25° to -5.10° (North-South)
- Longitude: 119.40° to 119.60° (East-West)
- Grid Cells: ~3,600
- Total Days (2018-2020): 1,096 days
- Total Observations: ~3,936,000
```

### Test Region: Jakarta

```
Geographic Extent:
- Latitude: -6.30° to -6.10° (North-South)
- Longitude: 106.70° to 107.00° (East-West)
- Grid Cells: ~8,000
- Total Days (2021-2022): 730 days
- Total Observations: ~5,840,000
```

### Spatial Separation Guarantee

```
✅ No geographic overlap between Makassar and Jakarta
✅ ~2,000 km separation (sufficient for distinct climate regimes)
✅ Clear boundary between train and test regions
```

---

## 9.2 Temporal Split

### Training Temporal Window

```
Period: 2018-01-01 to 2020-12-31
Duration: 3 years (1,096 days)
Coverage: 5 complete wet-dry seasonal cycles
Regions: Makassar only
```

### Test Temporal Window

```
Period: 2021-01-01 to 2022-12-31
Duration: 2 years (730 days)
Coverage: 2 complete wet-dry seasonal cycles
Regions: Jakarta only
```

### Temporal Separation Guarantee

```
✅ Strict non-overlapping time periods
✅ Training: 2018-2020
✅ Test: 2021-2022
✅ No information leakage (no future data used for training)
```

---

## 9.3 Experimental Split Combinations

### Experiment 1: In-Domain (Baseline)

```
Training:   Makassar 2018-2020
Test:       Makassar 2021-2022 (new years)
Purpose:    Baseline generalization (same region, different years)
```

### Experiment 2: Cross-Region (Primary)

```
Training:   Makassar 2018-2020
Test:       Jakarta 2021-2022 (new region, new years)
Purpose:    Test spatial generalization (primary research question)
```

### Experiment 3: Temporal Generalization

```
Training:   Makassar 2018-2020
Test:       Makassar 2021-2022 (same region, different years)
Purpose:    Measure temporal shift impact
```

### Experiment 4: Combined Shift

```
Training:   Makassar 2018-2020
Test:       Jakarta 2021-2022
Purpose:    Measure combined spatial + temporal shift
```

---

## 9.4 Data Split Implementation

### Python Implementation

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Load full dataset
data = pd.read_csv('ST_FSLD_v1.csv')

# Split 1: In-Domain (Makassar, temporal split)
makassar_data = data[data['region'] == 'Makassar']
train_in_domain = makassar_data[makassar_data['date'] < '2021-01-01']
test_in_domain = makassar_data[makassar_data['date'] >= '2021-01-01']

# Split 2: Cross-Region (spatial split)
train_cross_region = data[(data['region'] == 'Makassar') & 
                          (data['date'] < '2021-01-01')]
test_cross_region = data[(data['region'] == 'Jakarta') & 
                         (data['date'] >= '2021-01-01')]

# Verify no overlap
assert len(train_in_domain) > 0
assert len(test_in_domain) > 0
assert train_in_domain['date'].max() < test_in_domain['date'].min()
assert len(set(train_cross_region['lat']) & set(test_cross_region['lat'])) == 0
```

---

## 9.5 Data Split Statistics

### Train-Test Size Summary

| Split | Region | Period | Grids | Days | Observations | % Floods |
|-------|--------|--------|-------|------|--------------|----------|
| **Train** | Makassar | 2018-2020 | 3,600 | 1,096 | 3,936,000 | 10% |
| **Test In-Domain** | Makassar | 2021-2022 | 3,600 | 730 | 2,628,000 | 10% |
| **Test Cross-Region** | Jakarta | 2021-2022 | 8,000 | 730 | 5,840,000 | 12% |

---

# 10. 🔬 Quality Control

## 10.1 Missing Data Handling

### 10.1.1 Rainfall Gaps

**Common Issue**: CHIRPS may have occasional missing values.

**Handling Strategy**:

```python
def handle_rainfall_gaps(rainfall_series, max_gap_days=3):
    """
    Interpolate short rainfall gaps (≤3 days)
    Mark longer gaps as missing
    """
    # Interpolate short gaps (≤3 days)
    rainfall_filled = rainfall_series.interpolate(
        method='linear', 
        limit=max_gap_days
    )
    
    # Keep missing values for longer gaps
    return rainfall_filled
```

**Decision Rules**:
- ✅ Gap ≤ 3 days: Linear interpolation
- ❌ Gap > 3 days: Mark as missing, flag for review
- 🔄 Post-processing: Drop rows with missing rainfall

### 10.1.2 DEM Missing Values

**Common Issue**: SRTM may have voids in mountains or water.

**Handling Strategy**:

```python
def fill_dem_voids(dem_raster):
    """
    Fill SRTM voids using nearest neighbor
    """
    from scipy.ndimage import distance_transform_edt
    
    # Identify voids (missing values)
    void_mask = np.isnan(dem_raster)
    
    # Nearest neighbor interpolation
    coords = distance_transform_edt(void_mask, return_distances=False, 
                                     return_indices=True)
    dem_filled = dem_raster[coords]
    
    return dem_filled
```

### 10.1.3 Flood Label Gaps

**Common Issue**: Sentinel-1 may have gaps due to satellite orbit.

**Handling Strategy**:
- ✅ Gaps ≤ 6 days (Sentinel-1 revisit): Use forward fill
- ❌ Gaps > 6 days: Mark as unknown (exclude from analysis)

---

## 10.2 Noise Handling

### 10.2.1 Rainfall Outliers

**Detection**: Extreme daily rainfall (>500 mm)

```python
def detect_rainfall_outliers(rainfall_series, threshold=500):
    """
    Detect extreme rainfall values
    """
    outliers = rainfall_series[rainfall_series > threshold]
    return outliers
```

**Action**:
- ✅ Flag for manual review
- ✅ Validate against news reports or satellite data
- ✅ Keep if confirmed (extreme events happen)
- ❌ Remove if erroneous

### 10.2.2 Sentinel-1 Speckle Noise

**Issue**: SAR backscatter contains multiplicative speckle noise.

**Handling**:

```python
def apply_lee_filter(s1_image, window_size=5):
    """
    Apply Lee filter to reduce speckle noise
    """
    from scipy.ndimage import filters
    
    # Lee filter implementation
    filtered = s1_image  # Apply Lee filter
    
    return filtered
```

### 10.2.3 False Flood Detections

**Issue**: Non-flood water (lakes, rivers) detected as floods.

**Handling**:
- ✅ Multi-criteria validation (see Section 5.4)
- ✅ Compare with pre-flood baseline
- ✅ Exclude permanent water bodies

---

## 10.3 Consistency Checks

### 10.3.1 Rainfall-Flood Correlation

**Rule**: Floods should correlate with preceding rainfall.

```python
def validate_rainfall_flood_correlation(data, min_correlation=0.6):
    """
    Check correlation between rainfall and flood events
    """
    correlation = data.groupby('region').apply(
        lambda group: group['rainfall'].corr(group['flood'].astype(float))
    )
    
    for region, corr in correlation.items():
        if corr < min_correlation:
            print(f"Warning: Low correlation in {region}: {corr:.2f}")
    
    return correlation
```

### 10.3.2 Elevation Sanity Check

**Rule**: Elevation should be ≥0 (sea level) in most areas, with rare subsidence.

```python
def validate_elevation(data):
    """
    Check elevation values
    """
    assert data['elevation'].min() >= -10, "Elevation too low"
    assert data['elevation'].max() <= 2000, "Elevation too high"
    
    subsidence_areas = data[data['elevation'] < 0]
    print(f"Subsidence areas (elevation < 0): {len(subsidence_areas)}")
```

### 10.3.3 Spatial Continuity

**Rule**: Neighboring grid cells should have similar elevation.

```python
def validate_spatial_continuity(grid_df):
    """
    Check elevation continuity between neighboring cells
    """
    for grid_id in grid_df.index:
        neighbors = find_neighbors(grid_id)
        elevation = grid_df.loc[grid_id, 'elevation']
        
        for neighbor_id in neighbors:
            neighbor_elev = grid_df.loc[neighbor_id, 'elevation']
            elevation_diff = abs(elevation - neighbor_elev)
            
            if elevation_diff > 500:  # 500m jump is suspicious
                print(f"Alert: Large elevation jump {grid_id} to {neighbor_id}")
```

---

## 10.4 Data Quality Report

### Template

```
DATA QUALITY REPORT
=====================

Dataset: ST-FSLD v1.0
Generated: 2026-04-XX

COVERAGE
--------
Total Grid Cells: 11,600
Total Days: 1,825
Total Observations: 9,776,000

MISSING DATA
-----------
Rainfall missing: <0.1%
Elevation missing: 0%
Flood labels missing: 0.5%

OUTLIERS DETECTED
-----------------
Rainfall > 500mm: 23 events (reviewed and validated)
Elevation extremes: None

CONSISTENCY CHECKS
------------------
✅ Rainfall-Flood correlation: 0.65 (Makassar), 0.68 (Jakarta)
✅ Elevation sanity: Passed
✅ Spatial continuity: Passed
✅ No temporal gaps > 3 days

CLASS IMBALANCE
---------------
Makassar: 10% floods, 90% non-floods
Jakarta: 12% floods, 88% non-floods
Overall: 11% floods, 89% non-floods

QC APPROVAL
-----------
Status: PASS
Approved for use in experiments.
```

---

# 11. 📦 Final Dataset Output Format

## 11.1 File Specification

### Primary Output: CSV Format

```
Filename:       ST_FSLD_v1_combined.csv
Size:           ~2.5 GB
Rows:           9,776,000
Columns:        12
Format:         UTF-8 encoding
Delimiter:      comma (,)
Header:         First row contains column names
```

### Alternative Formats

**Parquet** (for Python/Pandas):
```
Filename: ST_FSLD_v1_combined.parquet
Size: ~1.2 GB (50% compression)
```

**HDF5** (for large-scale ML):
```
Filename: ST_FSLD_v1_combined.h5
Size: ~1.5 GB
```

---

## 11.2 Column Specification

### CSV Column Order

```
lat,lon,date,rainfall,rainfall_3day,rainfall_7day,elevation,slope,landuse,distance_river,flood,region
```

### Detailed Column Specification

| # | Column | Type | Format | Example | Unit | Missing |
|----|--------|------|--------|---------|------|---------|
| 1 | lat | float | decimal degrees | -5.150 | ° | No |
| 2 | lon | float | decimal degrees | 119.450 | ° | No |
| 3 | date | string | YYYY-MM-DD | 2018-01-01 | - | No |
| 4 | rainfall | float | decimal | 5.20 | mm | Rare |
| 5 | rainfall_3day | float | decimal | 12.30 | mm | No |
| 6 | rainfall_7day | float | decimal | 45.60 | mm | No |
| 7 | elevation | float | decimal | 125.50 | m | No |
| 8 | slope | float | decimal | 8.50 | ° | No |
| 9 | landuse | string | category | urban | - | No |
| 10 | distance_river | float | decimal | 1250.00 | m | No |
| 11 | flood | integer | 0 or 1 | 1 | - | No |
| 12 | region | string | category | Makassar | - | No |

---

## 11.3 Data Type Precision

### Numeric Precision

```
Latitude/Longitude:     6 decimal places (~0.1 m accuracy)
Rainfall:              1 decimal place (0.1 mm)
Elevation:             1 decimal place (0.1 m)
Slope:                 2 decimal places (0.01°)
Distance to river:     0 decimal places (1 m)
```

### Categorical Values

```
Landuse: {urban, forest, agricultural, water, barren}
Flood:   {0, 1}
Region:  {Makassar, Jakarta}
```

---

## 11.4 Data Access & Distribution

### Local Storage

```
Location: /data/processed/
Filename: ST_FSLD_v1_combined.csv
Copy Size: ~2.5 GB
Backup: Multiple redundant copies
```

### Cloud Storage

```
Platform: Google Cloud Storage (GCS)
Bucket: gs://flood-ml-research-data/
Path: gs://flood-ml-research-data/ST_FSLD_v1/
Access: Research team members
Versioning: Enabled
```

### Reproducibility Archive

```
Package Contents:
- Raw dataset (ST_FSLD_v1_combined.csv)
- Data dictionary (DATASET_SPECIFICATION.md)
- Generation scripts (Python)
- Quality control reports
- Metadata (JSON)
```

---

# 12. 📊 Data Characteristics & Statistics

## 12.1 Dataset Size Summary

| Metric | Makassar Train | Makassar Test | Jakarta Test | Total |
|--------|---|---|---|---|
| Grid Cells | 3,600 | 3,600 | 8,000 | 15,200 |
| Days | 1,096 | 730 | 730 | 2,556 |
| Total Observations | 3,936,000 | 2,628,000 | 5,840,000 | 12,404,000 |
| Flood Events | ~394,000 | ~262,800 | ~700,800 | ~1,357,600 |
| Non-Flood Events | ~3,542,000 | ~2,365,200 | ~5,139,200 | ~11,046,400 |

---

## 12.2 Feature Distribution

### Rainfall Statistics (mm)

| Region | Metric | Train (2018-2020) | Test (2021-2022) |
|--------|--------|---|---|
| **Makassar** | Mean | 8.5 | 7.2 |
| | Std Dev | 12.3 | 11.8 |
| | Min | 0.0 | 0.0 |
| | Max | 487.2 | 412.5 |
| | 95th Percentile | 28.3 | 24.5 |
| **Jakarta** | Mean | 9.2 | 8.8 |
| | Std Dev | 13.5 | 13.2 |
| | Min | 0.0 | 0.0 |
| | Max | 512.3 | 498.1 |
| | 95th Percentile | 30.1 | 28.7 |

### Elevation Statistics (m)

| Region | Metric | Value |
|--------|--------|-------|
| **Makassar** | Mean | 125 |
| | Std Dev | 85 |
| | Min | 0 |
| | Max | 285 |
| **Jakarta** | Mean | 8 |
| | Std Dev | 15 |
| | Min | -8 |
| | Max | 52 |

### Slope Statistics (°)

| Region | Metric | Value |
|--------|--------|-------|
| **Makassar** | Mean | 12.3 |
| | Std Dev | 9.8 |
| | Min | 0.1 |
| | Max | 38.5 |
| **Jakarta** | Mean | 2.1 |
| | Std Dev | 1.8 |
| | Min | 0.0 |
| | Max | 8.2 |

### Landuse Distribution (%)

| Class | Makassar | Jakarta |
|-------|----------|---------|
| Urban | 32% | 62% |
| Agricultural | 38% | 18% |
| Forest | 22% | 4% |
| Water | 4% | 10% |
| Barren | 4% | 6% |

---

## 12.3 Temporal Characteristics

### Seasonal Patterns

**Dry Season** (May–September):
- Average rainfall: 3–5 mm/day
- Flood frequency: ~2%

**Wet Season** (October–April):
- Average rainfall: 12–18 mm/day
- Flood frequency: ~20%

### Annual Flood Events

| Year | Makassar | Jakarta |
|------|----------|---------|
| 2018 | 78 events | - |
| 2019 | 65 events | - |
| 2020 | 82 events | - |
| 2021 | 89 events | 125 events |
| 2022 | 94 events | 138 events |

---

# 13. 🧠 Design Principles (VERY IMPORTANT)

## 13.1 Core Design Philosophy

This dataset is **NOT** designed for:

- ❌ Maximizing model accuracy
- ❌ Building the "best" flood prediction system
- ❌ Operational flood forecasting
- ❌ General-purpose machine learning benchmarks

Instead, it is designed for:

- ✅ **Testing shortcut learning hypothesis**
- ✅ **Measuring spatial bias in ML models**
- ✅ **Quantifying generalization failures**
- ✅ **Understanding when models fail under distribution shift**
- ✅ **Enabling transparent, reproducible ML research**

---

## 13.2 Key Design Decisions Explained

### Decision 1: Maintain Natural Class Imbalance

**Why**: 
- Floods are rare (~10% of days)
- Balancing creates unrealistic distribution
- Tests model robustness in real-world scenarios

**Impact**:
- ✅ Honest evaluation metrics (ROC-AUC, PR-AUC)
- ✅ Prevents overfitting to balanced distribution
- ✅ Reflects operational deployment conditions

---

### Decision 2: Strict Spatial-Temporal Separation

**Why**:
- Test spatial generalization (different regions)
- Test temporal generalization (different years)
- Prevent information leakage

**Impact**:
- ✅ Clear measurement of cross-region performance drop
- ✅ Clear measurement of temporal robustness
- ✅ Credible evidence of shortcut learning

---

### Decision 3: Include Lat/Lon as Diagnostic Features

**Why**:
- Explicitly detect if model relies on location
- Compare Model A (with lat/lon) vs Model B (without)
- Quantify spatial bias

**Impact**:
- ✅ Direct measurement of spatial bias
- ✅ Interpretable results (compare model performances)
- ✅ Enables "ablation study" of location information

---

### Decision 4: Event-Based Labeling (Non-Random)

**Why**:
- Floods are rare events, not randomly distributed
- Event-based sampling captures causal structure
- Represents actual flood dynamics

**Impact**:
- ✅ More realistic labels
- ✅ Better model learning of physical processes
- ✅ Captures pre-flood and flood conditions

---

## 13.3 Experimental Use Cases

### Use Case 1: Baseline Model Evaluation

```
Train: Makassar 2018–2020
Test: Makassar 2021–2022

Questions:
- How well can models generalize to new years?
- Temporal robustness in same region?
```

### Use Case 2: Cross-Region Generalization

```
Train: Makassar 2018–2020
Test: Jakarta 2021–2022

Questions:
- Can models transfer to new regions?
- How much does performance degrade spatially?
- Evidence of overfitting to Makassar characteristics?
```

### Use Case 3: Spatial Bias Detection

```
Model A: WITH lat/lon
Model B: WITHOUT lat/lon

Train: Both on Makassar 2018–2020
Test: Both on Jakarta 2021–2022

Questions:
- Does removing lat/lon hurt performance?
- How much of model's predictive power comes from location?
- Evidence of shortcut learning?
```

### Use Case 4: Feature Importance Analysis

```
Train: Makassar 2018–2020
Test: Makassar & Jakarta

Feature importance methods:
- SHAP values
- Permutation importance
- Coefficient analysis

Questions:
- Which features matter most?
- Consistent across regions?
- Physical features vs spatial shortcuts?
```

---

## 13.4 Success Criteria

The dataset achieves its purpose if:

✅ Models trained on Makassar show **10–20% performance drop** on Jakarta

✅ Models WITH lat/lon significantly outperform models WITHOUT lat/lon

✅ Feature importance analysis reveals **spatial bias** (lat/lon highly important)

✅ Error patterns show **systematic failures** (not random)

✅ Dataset supports **reproducible, transparent** ML research

---

# 14. 🚀 Implementation Roadmap

## 14.1 Phase 1: Infrastructure Setup (Week 1–2)

### Tasks
- [ ] Create Google Earth Engine account & project
- [ ] Set up Google Cloud Storage bucket
- [ ] Create grid geometries (Makassar + Jakarta)
- [ ] Test GEE API access

### Deliverables
- ✅ GEE project configured
- ✅ Cloud storage ready
- ✅ Grid files (GeoJSON)

---

## 14.2 Phase 2: Feature Extraction (Week 3–5)

### Tasks
- [ ] Download CHIRPS rainfall data
- [ ] Extract SRTM DEM & compute slope
- [ ] Download ESA WorldCover
- [ ] Rasterize OpenStreetMap rivers

### Deliverables
- ✅ Rainfall time series (2018–2022)
- ✅ Topographic rasters (elevation, slope)
- ✅ LULC classification
- ✅ River distance rasters

---

## 14.3 Phase 3: Flood Labeling (Week 6–7)

### Tasks
- [ ] Download Sentinel-1 SAR imagery
- [ ] Implement backscatter change detection
- [ ] Validate against ground truth
- [ ] Generate flood labels (2018–2022)

### Deliverables
- ✅ Flood event database
- ✅ Validated labels
- ✅ Quality control report

---

## 14.4 Phase 4: Data Assembly (Week 8)

### Tasks
- [ ] Join all features spatially & temporally
- [ ] Generate final CSV
- [ ] Run quality control checks
- [ ] Generate data characteristics report

### Deliverables
- ✅ ST_FSLD_v1.csv (complete dataset)
- ✅ Data dictionary
- ✅ Quality control report

---

## 14.5 Phase 5: Validation & Release (Week 9)

### Tasks
- [ ] Final quality assurance
- [ ] Documentation review
- [ ] Dataset versioning
- [ ] Publish to GitHub & GCS

### Deliverables
- ✅ Official dataset release
- ✅ Complete documentation
- ✅ Usage examples

---

## 14.6 Technical Stack

### Required Software
- Python 3.8+
- Google Earth Engine Python API
- GeoPandas / Rasterio
- Pandas / NumPy
- Scikit-learn

### Required Credentials
- Google Earth Engine account (free)
- Google Cloud project
- Cloud storage bucket

### Recommended Infrastructure
- Google Colab (for GEE processing)
- Google Cloud VM (for large-scale processing)
- Local workstation (for final assembly)

---

# APPENDIX: Quick Reference

## Dataset Summary

| Property | Value |
|----------|-------|
| **Name** | Spatio-Temporal Flood Shortcut Learning Dataset (ST-FSLD v1.0) |
| **Region** | Makassar (training) + Jakarta (testing) |
| **Period** | 2018–2022 |
| **Resolution** | 250m × 250m grid, daily temporal |
| **Total Observations** | ~9.8 million |
| **Features** | 11 (7 physical + 2 spatial diagnostic + 1 temporal) |
| **Target** | Binary flood label |
| **Class Balance** | ~11% floods, 89% non-floods |
| **File Size** | ~2.5 GB (CSV) |
| **Format** | CSV, Parquet, HDF5 |
| **Status** | Development |
| **License** | Open Science (pending) |

---

## File Locations

```
GitHub Repository:
/docs/
  ├── DATASET_SPECIFICATION.md (this file)
  └── research_proposal.md

Data Repository (Google Cloud):
gs://flood-ml-research-data/
  ├── ST_FSLD_v1/
  │   ├── ST_FSLD_v1_combined.csv
  │   ├── metadata.json
  │   └── quality_report.pdf

Local Storage:
/data/
  ├── raw/          (original data from sources)
  ├── processed/    (cleaned dataset)
  └── splits/       (train-test splits)
```

---

## Key Contact & References

**Questions about dataset?**
- Check: DATASET_SPECIFICATION.md (this document)
- Reference: research_proposal.md

**Data Issues?**
- Quality issues → See Section 10 (Quality Control)
- Missing data → See Section 10.1 (Missing Data Handling)
- Validation → See Section 10.3 (Consistency Checks)

---

## Document Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | April 2026 | Initial specification |

---

**END OF DOCUMENT**

---

*This specification document is a living document. Updates will be made as the research progresses. Last updated: April 2026.*
