from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication   #aplikace s grafickým rozhraním 
from PySide6.QtQuick import  QQuickView    
import sys  #něco jako arcgparse

VIEW_PATH = "viewf.qml"

# Create the application object and pass command line arguments to it
app = QGuiApplication(sys.argv)

# Create the view object
view = QQuickView()         #to, co je uvnitř okna aplikace
# Set the QML file to view
view.setSource(QUrl(VIEW_PATH))     #tady mun řeknu, odkud si má načíst grafické rozhranní; předám jako QUrl, mohla bych tp totiž mít jako url z netu 
# Resize the view with the window
view.setResizeMode(QQuickView.ResizeMode.SizeRootObjectToView)      #řeknu mu, ať se grafické rozhranní otevře a roztáhne na velikost vytvořeného okna
# Show the view (open the window)
view.show()     

# Run the event loop - smyčka událostí 
app.exec()

