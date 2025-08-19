#Test for creating layout using QGIS processing programatically

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
        QgsApplication.setPrefixPath(str(qgis_path / "apps" / "qgis"), True)
        qgs = QgsApplication([], False)
        qgs.initQgis()
        
        print("QGIS initialized successfully:", QgsProject.instance())
        return qgs
    except Exception as e:
        print(f"Error initializing QGIS: {e}")
        raise

if __name__ == "__main__":
    qgs = initialize_qgis()

    #Import reuired modules
    from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsPointXY, QgsProject
    from qgis.PyQt.QtWidgets import QApplication
    from qgis.gui import QgsMapCanvas
    from qgis.PyQt.QtCore import Qt


    app = QApplication([])  # Needed for GUI apps
    canvas = QgsMapCanvas()
    canvas.setCanvasColor(Qt.white)
    canvas.show()

    # 4. Create polygon memory layer
    polygon_layer = QgsVectorLayer("Polygon?crs=EPSG:4326", "polygon_test", "memory")
    polygon_layer.startEditing()
    polygon_feature = QgsFeature()
    points = [QgsPointXY(30, 10), QgsPointXY(40, 20), QgsPointXY(30, 20), QgsPointXY(30, 10)]
    polygon_feature.setGeometry(QgsGeometry.fromPolygonXY([points]))
    polygon_layer.addFeature(polygon_feature)
    polygon_layer.commitChanges()

    # 5. Create point memory layer
    point_layer = QgsVectorLayer("Point?crs=EPSG:4326", "point_test", "memory")
    point_layer.startEditing()
    point_feature = QgsFeature()
    point_feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10, 20)))
    point_layer.addFeature(point_feature)
    point_layer.commitChanges()

    # 6. Add layers to project
    project = QgsProject.instance()
    project.addMapLayer(polygon_layer)
    project.addMapLayer(point_layer)

    # 7. Set canvas layers and zoom to extent
    canvas.setLayers([polygon_layer, point_layer])
    canvas.zoomToFullExtent()

    # 8. Run Qt application
    app.exec_()

    # 9. Exit QGIS properly
    qgs.exitQgis()
    print("Created image and exited successfully")
