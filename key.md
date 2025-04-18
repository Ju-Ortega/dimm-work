# DIMM-WORK Repository Structure

This repository is organized following best practices for data science and research projects, with emphasis on Physics-Informed Neural Networks (PINNs) and differential equation modeling.

## Directory Structure

### `data/`
Stores all data used in the project. This folder contains only data files, not code.

### `doc/`
Contains all project documentation:
- `latex/apuntes/`: LaTeX documents with theoretical notes and concepts about PINNs, eikonal equations, etc.
- `latex/manuscrito/`: Drafts and versions of manuscripts for potential publications.
- `meetings/`: Notes and minutes from meetings with collaborators and advisors.
- `papers/`: Relevant scientific articles for reference.

### `notebooks/`
Jupyter notebooks in logical sequence for analysis:
- `01_data_exploration.ipynb`: Initial data exploration.
- `02_model_development.ipynb`: Model development and testing.
- `03_result_analysis.ipynb`: Results analysis and evaluation.

### `src/`
Source code organized into Python modules:
- `data/`: Modules for loading, processing, and preparing data.
  - `__init__.py`: Defines the module as importable.
  - `data_utils.py`: Utility functions for data processing.

- `models/`: Neural network model implementations.
  - `__init__.py`: Defines the module as importable.
  - `theta_pinn.py`: Implementation of the Θ-PINN model for eikonal equations.

- `training/`: Code for training and evaluating models.
  - `__init__.py`: Defines the module as importable.
  - `trainer.py`: Classes and functions for model training.

- `visualization/`: Tools for visualizing data and results.
  - `__init__.py`: Defines the module as importable.
  - `plotting.py`: Functions for generating plots and visualizations.

- `__init__.py`: Root file that allows importing the complete module.

### `tests/`
Unit tests to verify code functionality:
- `__init__.py`: Defines the module as importable.
- `test_data.py`: Tests for data processing functionalities.
- `test_models.py`: Tests for implemented models.

### Root directory files
- `.gitignore`: Specifies files and directories ignored by version control.
- `LICENSE`: MIT license defining the terms of code usage.
- `README.md`: General project description, installation, and usage instructions.
- `requirements.txt`: List of dependencies required to run the code.
- `setup.py`: Script to install the package in development mode.

## Recommended Workflow

1. Place raw data in `data/`
2. Develop and test functionalities in notebooks within `notebooks/`
3. Implement reusable functions in the appropriate modules within `src/`
4. Write tests in `tests/` to verify correct functionality
5. Document theoretical concepts in `doc/latex/apuntes/`
6. Record progress and decisions in `doc/meetings/`
7. Prepare manuscripts for publication in `doc/latex/manuscrito/`

## Import Structure

When working with the code, use imports like:

```python
# Import specific modules
from src.models.theta_pinn import ThetaPINN
from src.data.data_utils import load_data

# Or import the package and use dot notation
import src
model = src.models.theta_pinn.ThetaPINN()