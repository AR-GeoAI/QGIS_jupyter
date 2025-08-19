import sys
import os
from qgis.core import QgsApplication, QgsProject

# Add QGIS Python paths
sys.path.append(r"C:\Program Files\QGIS 3.36.2\apps\qgis\python")
sys.path.append(r"C:\Program Files\QGIS 3.36.2\apps\Python312\Lib\site-packages")

# Add QGIS DLL directory
os.add_dll_directory(r"C:\Program Files\QGIS 3.36.2\bin")

# Initialize QGIS
QgsApplication.setPrefixPath(r"C:\Program Files\QGIS 3.36.2\apps\qgis", True)
qgs = QgsApplication([], False)
qgs.initQgis()

print("QGIS initialized:", QgsProject.instance())
