"""
Pytest Configuration

Shared fixtures and configuration for test suite
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / 'src'))


@pytest.fixture(scope="session")
def project_root_path():
    """Get project root path"""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def data_path(project_root_path):
    """Get data directory path"""
    return project_root_path / 'data'


@pytest.fixture(scope="session")
def intermediate_data_path(data_path):
    """Get intermediate data directory path"""
    return data_path / 'intermediate'


@pytest.fixture(scope="session")
def results_path(project_root_path):
    """Get results directory path"""
    return project_root_path / 'results'
