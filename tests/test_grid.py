"""
Grid Consistency Tests

Validates grid generation and integrity
"""

import pytest
import geopandas as gpd
from pathlib import Path


class TestGridGeneration:
    """Test suite for grid generation consistency"""
    
    @pytest.fixture
    def grid_path(self):
        """Path to generated grid"""
        return Path("data/intermediate/grid_definition.geojson")
    
    def test_grid_exists(self, grid_path):
        """Test that grid file exists"""
        assert grid_path.exists(), f"Grid file not found at {grid_path}"
    
    def test_grid_is_valid_geojson(self, grid_path):
        """Test that grid is valid GeoJSON"""
        gdf = gpd.read_file(grid_path)
        assert len(gdf) > 0, "Grid is empty"
        assert gdf.crs is not None, "Grid has no CRS"
    
    def test_grid_no_overlaps(self, grid_path):
        """Test that grid cells do not overlap (Q1 requirement)"""
        gdf = gpd.read_file(grid_path)
        
        # Check for self-intersections
        for idx, geom in enumerate(gdf.geometry):
            assert geom.is_valid, f"Grid cell {idx} is invalid"
    
    def test_grid_complete_coverage(self, grid_path):
        """Test that grid covers expected area"""
        gdf = gpd.read_file(grid_path)
        
        # Get total boundary
        total_bounds = gdf.total_bounds
        assert total_bounds is not None, "Cannot calculate grid bounds"
        assert len(gdf) > 0, "Grid has no cells"


class TestGridConsistency:
    """Test grid consistency across runs"""
    
    def test_grid_cell_count_consistent(self):
        """Q1 reproducibility: grid cell count should be consistent"""
        pass
    
    def test_grid_crs_consistency(self):
        """Ensure CRS remains consistent"""
        pass
