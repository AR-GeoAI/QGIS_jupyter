# setup/qgis_init.py
import sys
import os
from pathlib import Path
from qgis.core import QgsApplication, QgsProject

def initialize_qgis():
    qgis_path = Path(r"C:\Program Files\QGIS 3.36.2")

    sys.path.append(str(qgis_path / "apps" / "qgis" / "python"))
    sys.path.append(str(qgis_path / "apps" / "Python312" / "Lib" / "site-packages"))

    if sys.platform == "win32":
        os.add_dll_directory(str(qgis_path / "bin"))

    QgsApplication.setPrefixPath(str(qgis_path / "apps" / "qgis"), True)
    qgs = QgsApplication([], False)
    qgs.initQgis()

    print("QGIS initialized successfully:", QgsProject.instance())
    return qgs