"""
Pyside standalone application
#pip install pyside2
"""
from PySide2 import QtCore, QtWebEngineWidgets, QtWidgets

URL = 'https://python.org'

app = QtWidgets.QApplication()
view = QtWebEngineWidgets.QWebEngineView()
view.load(QtCore.QUrl(URL))
view.show()
app.exec_()