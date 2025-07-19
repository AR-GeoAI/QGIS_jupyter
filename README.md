<<<<<<< HEAD
# QGIS + Jupyter Integration (Windows, QGIS 3.36.2)

This repository shows how to run **QGIS inside Jupyter notebooks** using a Conda environment.  
It allows you to interactively use the QGIS Python API (**PyQGIS**) for geospatial workflows in an interactive data science environment.

---

## ⚠️ Important Note on Python Versions

QGIS ships with its own embedded Python version.  
To make this work, you must use the **same Python version that your QGIS installation uses**.  

- For **QGIS 3.36.2**, the bundled Python is **3.12**.  
- If you are on a different QGIS version, adjust the Python version in your `environment.yml` and update the QGIS paths in `setup/qgis_init.py`.

---

## Requirements

- Windows OS  
- [QGIS 3.36.2](https://qgis.org/download/) installed  
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/) installed  

---

## Setup Instructions

1. **Clone this repo**  
   ```bash
   git clone https://github.com/AR-GeoAI/QGIS_jupyter.git
   cd QGIS_jupyter

2. **Create and activate the environment**  
   ```bash
   conda env create -f environment.yml
   conda activate qgis-jupyter

3. **Install the Jupyter kernel**  
   ```bash
   python -m ipykernel install --user --name=qgis-jupyter --display-name "Python (QGIS 3.36)"

4. **Launch Jupyter**  
   ```bash
   jupyter notebook

5. **Test the setup**
   - Open [notebooks/qgis_test.ipynb](notebooks/qgis_test.ipynb) and run all cells.
   - Expected output:
   ```python
   QGIS initialized successfully: <QgsProject object at ...>
   Layer valid: True
   Features in layer: 1
=======
"# Porphyry_Targeting_BCRegional" 
>>>>>>> 4103e1f (first commit)
