# 📊 DATASET SPECIFICATION (FINAL Q1-READY)
## Spatio-Temporal Flood Shortcut Learning Dataset (ST-FSLD v1.0)

**Version:** 1.0 – Final  
**Last Updated:** April 2026  
**Purpose:** Diagnostic dataset for shortcut learning analysis under spatio-temporal distribution shift in flood prediction

---

# 1. Dataset Purpose

This dataset is designed for **diagnosing shortcut learning behavior** in machine learning models applied to flood prediction, rather than operational flood forecasting.

The primary goal is to evaluate:
- Model behavior under spatial distribution shift
- Model behavior under temporal distribution shift
- Dependency on non-physical proxy features (e.g., coordinates)
- Physical consistency of learned representations

---

# 2. Fundamental Unit of Observation

Each sample represents a spatio-temporal observation:


(lat, lon, date) → feature vector → flood label


Where:
- Spatial unit: 250m × 250m grid cell
- Temporal unit: daily timestamp
- Label: binary flood occurrence

---

# 3. Spatial Design

## 3.1 Study Regions
- Makassar (training region)
- Jakarta (test region)

## 3.2 Grid System
- Resolution: 250 meters × 250 meters
- Grid type: regular spatial tessellation
- CRS: EPSG:4326 (WGS84) for storage
- Processing CRS: EPSG:32750 (UTM Zone 50S)

## 3.3 Spatial Coverage
Each grid cell is uniquely identified by:

grid_id = (lat_index, lon_index)


---

# 4. Temporal Design

- Temporal resolution: daily
- Time range: 2018–2022
- Training period: 2018–2020
- Testing period: 2021–2022

## Temporal Constraint
No temporal leakage is allowed:
- Future data cannot appear in training set
- Strict chronological split enforced

---

# 5. Flood Event Definition (Label Construction)

Flood labels are derived from Sentinel-1 SAR imagery using backscatter change detection:

## Rule:

Flood = 1 if backscatter_drop ≤ -3 dB
Flood = 0 otherwise


## Source:
- Sentinel-1 SAR (VV & VH polarization)
- Pre/post-event comparison

---

# 6. Feature Specification (INPUT VARIABLES)

Each sample contains **11 engineered features**:

---

## 6.1 Spatial Features

| Feature | Type | Unit | Description |
|--------|------|------|-------------|
| lat | float | degrees | Latitude of grid center |
| lon | float | degrees | Longitude of grid center |

---

## 6.2 Hydrological Features

| Feature | Type | Unit | Description |
|--------|------|------|-------------|
| rainfall_1d | float | mm | Daily rainfall |
| rainfall_3d | float | mm | 3-day cumulative rainfall |
| rainfall_7d | float | mm | 7-day cumulative rainfall |

Source: CHIRPS precipitation dataset

---

## 6.3 Topographic Features

| Feature | Type | Unit | Description |
|--------|------|------|-------------|
| elevation | float | meters | Digital Elevation Model (SRTM) |
| slope | float | degrees | Terrain slope derived from DEM |

---

## 6.4 Hydrological Distance Features

| Feature | Type | Unit | Description |
|--------|------|------|-------------|
| distance_to_river | float | meters | Euclidean distance to nearest river |

Source: OpenStreetMap river network

---

## 6.5 Land Use Features

| Feature | Type | Unit | Description |
|--------|------|------|-------------|
| landuse_type | categorical | class id | ESA WorldCover land classification |

Encoded as:
- One-hot encoding OR ordinal encoding (experiment-dependent)

---

## 6.6 Interaction Features

| Feature | Type | Unit | Description |
|--------|------|------|-------------|
| elevation_rainfall_interaction | float | derived | nonlinear interaction term |
| slope_rainfall_interaction | float | derived | terrain-rainfall coupling |

---

# 7. Target Variable

| Variable | Type | Values | Description |
|----------|------|--------|-------------|
| flood | binary | {0,1} | Flood occurrence label |

Distribution:
- Naturally imbalanced (~11% flood, ~89% non-flood)
- No artificial balancing applied

---

# 8. Data Generation Pipeline

## Step 1: Data Collection
- CHIRPS (rainfall)
- SRTM (elevation)
- ESA WorldCover (land use)
- OpenStreetMap (river network)
- Sentinel-1 (flood labels)

---

## Step 2: Spatial Alignment
- Reprojection to common CRS
- Alignment to 250m grid

---

## Step 3: Feature Extraction
- Raster → vector conversion
- Spatial joins for land use
- Distance computation for rivers

---

## Step 4: Temporal Aggregation
- Rolling rainfall windows (1d, 3d, 7d)

---

## Step 5: Dataset Construction
Final structured table:


(lat, lon, date, features[11], flood)


---

# 9. Data Splitting Strategy

## 9.1 Spatial Split
- Train: Makassar
- Test: Jakarta

Purpose:
- Evaluate spatial generalization
- Detect geographic memorization

---

## 9.2 Temporal Split
- Train: 2018–2020
- Test: 2021–2022

Purpose:
- Evaluate temporal generalization
- Detect seasonal shortcuts

---

## 9.3 Combined Constraints
- No overlap in spatial regions (for spatial shift experiments)
- No overlap in time (for temporal shift experiments)

---

# 10. Quality Control Procedures

## 10.1 Missing Data Handling
- Interpolation for rainfall gaps
- Masking for invalid raster values

## 10.2 Outlier Detection
- Z-score filtering for extreme rainfall values
- Terrain consistency checks

## 10.3 CRS Validation
- All spatial inputs validated to ensure CRS consistency

---

# 11. Output Format

Final dataset stored as CSV:


columns:
lat, lon, date,
rainfall_1d,
rainfall_3d,
rainfall_7d,
elevation,
slope,
distance_to_river,
landuse_type,
elevation_rainfall_interaction,
slope_rainfall_interaction,
flood


---

# 12. Dataset Characteristics

| Property | Value |
|----------|-------|
| Spatial resolution | 250m |
| Temporal resolution | Daily |
| Regions | 2 (Makassar, Jakarta) |
| Time range | 2018–2022 |
| Features | 11 |
| Label type | Binary |
| Imbalance ratio | ~11:89 |

---

# 13. Design Principles

## 13.1 No Artificial Balancing
The dataset preserves natural class imbalance to reflect real-world conditions.

## 13.2 No Feature Leakage
Temporal and spatial separation strictly enforced.

## 13.3 Diagnostic-Oriented Design
The dataset is explicitly designed to:
- expose shortcut learning
- stress-test generalization
- evaluate causal consistency

---

# 14. Implementation Roadmap

## Phase 1: Raw Data Ingestion
- Download all geospatial datasets
- Standardize CRS

## Phase 2: Grid Construction
- Build 250m spatial grid
- Assign grid IDs

## Phase 3: Feature Engineering
- Extract hydrological and topographic features

## Phase 4: Label Generation
- Process Sentinel-1 SAR flood detection

## Phase 5: Dataset Assembly
- Merge all features into unified table
- Generate train/test splits

---

# END OF DOCUMENT
