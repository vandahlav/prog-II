"""udělejte aplikaci, která bude mít okénko stupně, minuty a vteřiny 
a pod tím okýnko pro desetinné číslo """

from PySide6.QtCore import QObject, Slot, Property, QUrl, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView
import sys

VIEW_URL = "view_dms.qml"

class DMS_converter(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.d = 0
        self.m = 0
        self.s = 0
        self.d_float = 0

    #STUPNĚ
    def set_stupne (self, value):
        if value != self.d:
            self.d = value
            self.d_changed.emit(self.d)

    def get_stupne(self):
        return self.d
    
    #property to spojí s qml; nutné tohle mít na úrovni fcí
    #díky property a proměnné stupně pak můžu s tím pracovat
    d_changed = Signal(int)
    stupne = Property(int, get_stupne, set_stupne, notify=d_changed)

    #MINUTY
    def set_minuty(self, value):
        if value != self.m:
            self.m = value
            self.m_changed.emit(self.m)
    
    def get_minuty(self):
        return self.m
    
    m_changed = Signal(int)
    minuty = Property(int, get_minuty, set_minuty, notify=m_changed)
    
    #SEKUNDY
    def set_sekundy(self, value):
        if value != self.s:
            self.s = value
            self.s_changed.emit(self.s)
    
    def get_sekundy(self):
        return self.s
    
    s_changed = Signal(int)
    sekundy = Property(int, get_sekundy, set_sekundy, notify=s_changed)

    #VŠECHNO NAJEDNOU
    def set_d_float (self, value):
        if value != self.d_float:
            self.d_float = value
            self.d_float_changed.emit()
    
    def get_d_float (self):
        return self.d_float

    d_float_changed = Signal()
    vsechno = Property(float, get_d_float, set_d_float, notify = d_float_changed)

    @Slot()
    def prevod (self):
        print("To float.")
        self.vsechno = self.stupne + self.minuty/60 + self.sekundy/3600
    
    @Slot()
    def prevod_2 (self):
        print("To DMS.")
        value = float(self.vsechno)
        self.stupne = int(value)

        value = (value-self.stupne)*60
        self.minuty = int(value)

        value = (value-self.minuty)*60
        self.sekundy = int(value)

app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)

dms = DMS_converter()
ctxt = view.rootContext()
ctxt.setContextProperty('dms', dms)

view.setSource(url)
view.show()
app.exec_()