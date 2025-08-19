# setup/qgis_init.py
import sys
import os
from pathlib import Path

def initialize_qgis():
    try:
        # Default QGIS installation path (modify if needed)
        qgis_path = Path(r"C:\Program Files\QGIS 3.36.2")
        
        # Add QGIS Python and DLL paths
        sys.path.append(str(qgis_path / "apps" / "qgis" / "python"))
        sys.path.append(str(qgis_path / "apps" / "Python312" / "Lib" / "site-packages"))
        
        # Add QGIS DLL directory
        if sys.platform == "win32":
            os.add_dll_directory(str(qgis_path / "bin"))

        #Import QGIS modules
        from qgis.core import QgsApplication, QgsProject
        # Initialize QGIS
        from qgis.core import QgsApplication, QgsProject
        QgsApplication.setPrefixPath(str(qgis_path / "apps" / "qgis"), True)
        qgs = QgsApplication([], False)
        qgs.initQgis()
        
        print("QGIS initialized successfully:", QgsProject.instance())
        return qgs
    except Exception as e:
        print(f"Error initializing QGIS: {e}")
        raise

if __name__ == "__main__":
    initialize_qgis()

import sys
import os
