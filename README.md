# QGIS + Jupyter Integration (Windows, QGIS 3.36.2)

This repository shows how to run **QGIS inside Jupyter notebooks** using a Conda environment.  
It allows you to interactively run QGIS Python API (`PyQGIS`) for geospatial workflows.

⚠️ **Important**: You must use the same Python version that ships with your QGIS install.  
For QGIS 3.36.2, this is **Python 3.12**.

---

## Requirements
- Windows OS
- QGIS 3.36.2 (from [QGIS.org](https://qgis.org/))
- Miniconda/Anaconda

---

## Setup

1. Create and activate the environment:
   ```bash
   conda env create -f environment.yml
   conda activate qgis-jupyter
