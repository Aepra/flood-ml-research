# Testing Guide

## Overview

The test suite ensures data quality, consistency, and reproducibility for Q1 submission.

## Test Structure

```
tests/
├── __init__.py
├── conftest.py          # Pytest configuration and shared fixtures
├── test_grid.py         # Grid generation consistency tests
├── test_crs.py          # CRS validation tests
└── test_data_quality.py # Data completeness and integrity tests
```

## Running Tests

### Run all tests
```bash
pytest tests/ -v
```

### Run specific test file
```bash
pytest tests/test_grid.py -v
pytest tests/test_crs.py -v
pytest tests/test_data_quality.py -v
```

### Run specific test class
```bash
pytest tests/test_grid.py::TestGridGeneration -v
```

### Run with coverage
```bash
pytest tests/ --cov=src --cov-report=html
```

## Test Categories

### 1. Grid Consistency (test_grid.py)
- ✓ Grid file exists and is valid GeoJSON
- ✓ No overlapping cells
- ✓ Complete area coverage
- ✓ Reproducible cell count

**Why it matters for Q1:** Ensures grid generation is reliable and reproducible

### 2. CRS Validation (test_crs.py)
- ✓ CRS is defined
- ✓ CRS is valid (EPSG-based)
- ✓ All data uses consistent CRS
- ✓ Transformations are accurate

**Why it matters for Q1:** Spatial accuracy depends on consistent CRS

### 3. Data Quality (test_data_quality.py)
- ✓ No missing geometries
- ✓ No invalid geometries
- ✓ Reasonable bounds
- ✓ >= 90% data completeness

**Why it matters for Q1:** Ensures data quality for reliable analysis

## Adding New Tests

1. Create test file in `tests/` directory
2. Follow naming convention: `test_*.py`
3. Use pytest fixtures from `conftest.py`
4. Document test purpose with docstrings

Example:
```python
def test_my_feature(intermediate_data_path):
    """Test description"""
    assert True
```

## Continuous Integration

Tests should be run:
- Before committing code
- Before pushing to repository
- As part of CI/CD pipeline

```bash
# Pre-commit hook example
#!/bin/bash
pytest tests/ || exit 1
```
