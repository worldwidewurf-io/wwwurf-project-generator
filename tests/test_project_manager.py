"""Tests for the ProjectManager class."""
import os
import shutil
from pathlib import Path

import pytest

from wwwurf_project_generator.project_manager import ProjectManager


@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for testing."""
    yield tmp_path
    # Cleanup after tests
    if tmp_path.exists():
        shutil.rmtree(tmp_path)


def test_project_creation(temp_dir):
    """Test basic project creation."""
    os.chdir(temp_dir)
    manager = ProjectManager("test-project", ["core"])

    assert manager.create_project()

    # Check basic structure
    project_dir = temp_dir / "test-project"
    assert project_dir.exists()
    assert (project_dir / "pyproject.toml").exists()
    assert (project_dir / "README.md").exists()
    assert (project_dir / ".gitignore").exists()
    assert (project_dir / "packages" / "core").exists()


def test_package_creation(temp_dir):
    """Test adding a new package to an existing project."""
    os.chdir(temp_dir)

    # First create a project
    manager = ProjectManager("test-project", ["core"])
    manager.create_project()

    # Then add a new package
    os.chdir(temp_dir / "test-project")
    manager = ProjectManager()
    assert manager.create_package("new-package")

    # Check package structure
    package_dir = temp_dir / "test-project" / "packages" / "new-package"
    assert package_dir.exists()
    assert (package_dir / "pyproject.toml").exists()
    assert (package_dir / "README.md").exists()
    assert (package_dir / "new-package" / "__init__.py").exists()
    assert (package_dir / "new-package" / "main.py").exists()


def test_invalid_package_creation(temp_dir):
    """Test creating a package in an invalid directory."""
    os.chdir(temp_dir)
    manager = ProjectManager()
    assert not manager.create_package("new-package")


def test_duplicate_package_creation(temp_dir):
    """Test creating a package that already exists."""
    os.chdir(temp_dir)

    # Create initial project
    manager = ProjectManager("test-project", ["core"])
    manager.create_project()

    # Try to create core package again
    os.chdir(temp_dir / "test-project")
    manager = ProjectManager()
    assert not manager.create_package("core")
