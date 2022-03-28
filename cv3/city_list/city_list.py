from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel, QByteArray
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtPositioning import QGeoCoordinate
from PySide2 import QtCore
from enum import Enum
import typing
import sys
import json

#VIEW_URL = "simple_view.qml"   # Simple user interface
VIEW_URL = "view_city.qml"   # Advanced user interface
CITY_LIST_FILE = "souradnice.json"


class CityListModel(QAbstractListModel):
    """ Class for maintaining list of cities"""

    class Roles(Enum):
        AREA = QtCore.Qt.UserRole+0
        POPULATION = QtCore.Qt.UserRole+1
        LOCATION = QtCore.Qt.UserRole+2

    def __init__(self,filename=None):
        """Initialize and load list from given file"""
        QAbstractListModel.__init__(self)
        self.city_list = []
        if filename:
            self.load_from_json(filename)

    def load_from_json(self,filename):
        """Load list of cities from given file"""
        with open(filename,encoding="utf-8") as f:
            self.city_list = json.load(f)

            # Create QGeoCoordinate from the original JSON location
            # Rozbalí ten zápis v .jsonu
            for c in self.city_list:
                pos = c['location']
                lon,lat = pos.split("(")[1].split(")")[0].split(" ") # Get the part between brackets and split it on space
                c['location'] = QGeoCoordinate(float(lat),float(lon)) # Create QGeoCoordinate and overwrite original `location` entry


    def rowCount(self, parent:QtCore.QModelIndex=...) -> int:
        print("rowCount called")
        """ Return number of cities in the list"""
        return len(self.city_list)

    def data(self, index:QtCore.QModelIndex, role:int=...) -> typing.Any:
        print(f"data[{index.row()}], role {role}")
        """ For given index and DisplayRole return name of the selected city"""
        # Return None if the index is not valid
        if not index.isValid():
            return None
        # Co má pro jakou roli vrátit z dat .json
        if role == QtCore.Qt.DisplayRole:
            return self.city_list[index.row()]["muniLabel"]
        elif role == self.Roles.AREA.value:
            return self.city_list[index.row()]["area"]
        elif role == self.Roles.POPULATION.value:
            return self.city_list[index.row()]["population"]
        elif role == self.Roles.LOCATION.value:
            return self.city_list[index.row()]["location"]
    
    def roleNames(self) -> typing.Dict[int, QByteArray]:
        roles = super().roleNames() #vrátí seznam původních rolí
        roles[self.Roles.AREA.value] = QByteArray(b'area')
        roles[self.Roles.POPULATION.value] = QByteArray(b'population')
        roles[self.Roles.LOCATION.value] = QByteArray(b'location')
        print(roles)
        return roles


app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)
citylist_model = CityListModel(CITY_LIST_FILE)
ctxt = view.rootContext()
ctxt.setContextProperty('cityListModel',citylist_model)
view.setSource(url)
view.show()
app.exec_()
