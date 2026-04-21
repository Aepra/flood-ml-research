# Data Pipeline Documentation

## Pipeline Flow

```
RAW DATA (data/raw/)
    ├── CHIRPS rainfall data
    ├── DEM (Digital Elevation Model)
    └── OSM (OpenStreetMap) data
           ↓
PREPROCESSING (src/data/preprocessing.py)
    ├── Clean raw data
    ├── Validate CRS (EPSG:4326)
    ├── Handle missing values
    └── Data quality checks
           ↓
INTERMEDIATE (data/intermediate/)
    ├── Grid definition (grid_definition.geojson)
    ├── Aligned geometries
    └── Temporary processing outputs
           ↓
FEATURE ENGINEERING (src/features/)
    ├── Extract features from raw data
    ├── Spatial joins to grid
    └── Temporal aggregations
           ↓
PROCESSED DATA (data/processed/)
    ├── Final feature datasets
    ├── Normalized values
    └── Ready for modeling
           ↓
MODEL TRAINING (src/models/)
    └── Training and prediction
           ↓
RESULTS (results/)
    ├── figures/ - Generated visualizations
    ├── metrics/ - Performance metrics
    └── logs/ - Execution logs
```

## Key Requirements (Q1)

### CRS Consistency
- All spatial data must use **EPSG:4326** (WGS84)
- Validate CRS at each pipeline stage
- Document any transformations

### Data Quality Checks
- No missing geometries
- No invalid geometries  
- Completeness >= 90%
- Bounds validation

### Grid Reproducibility
- Grid generation must be deterministic
- Cell count must remain consistent across runs
- Grid cells must not overlap

## Data Directories

### data/raw/
Original, unmodified data sources. Never modify these files.

### data/intermediate/
Temporary outputs from pipeline stages:
- Grid definitions
- Spatial joins
- Alignment results

**Note:** These are outputs of your pipeline, not external data.

### data/processed/
Final datasets ready for analysis and modeling.
Output from complete preprocessing pipeline.

### data/external/
Reference data only (e.g., boundary definitions from GADM).
Minimal, read-only data.

## Running the Pipeline

```bash
# Generate grid
python -m notebooks.00_grid_generation

# Process boundaries
python -m notebooks.00a_boundary_q1

# Preprocess data
python src/data/preprocessing.py

# Run tests
pytest tests/
```

## Validation

Always run tests after data processing:

```bash
pytest tests/test_grid.py -v
pytest tests/test_crs.py -v  
pytest tests/test_data_quality.py -v
```
