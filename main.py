'''
Программа калькулятор
Краснов Леонид ИУ7-21Б
'''

"""

"""

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QTableWidget, QTableWidgetItem
from math import *

#  import design
import sys


class MainWindow(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.add_functions()


    def add_functions(self):
        self.pushButton_Calc.clicked.connect(lambda: getresult(self.line_func.text()))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_func = QtWidgets.QLineEdit(self.centralwidget)
        self.line_func.setGeometry(QtCore.QRect(36, 25, 115, 20))
        self.line_func.setObjectName("line_func")
        self.line_a = QtWidgets.QLineEdit(self.centralwidget)
        self.line_a.setGeometry(QtCore.QRect(187, 25, 115, 20))
        self.line_a.setObjectName("line_a")
        self.line_h = QtWidgets.QLineEdit(self.centralwidget)
        self.line_h.setGeometry(QtCore.QRect(338, 25, 115, 20))
        self.line_h.setObjectName("line_h")
        self.line_Nmax = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Nmax.setGeometry(QtCore.QRect(489, 25, 115, 20))
        self.line_Nmax.setObjectName("line_Nmax")
        self.pushButton_Calc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Calc.setGeometry(QtCore.QRect(36, 100, 568, 60))
        self.pushButton_Calc.setObjectName("pushButton_Calc")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 240, 620, 191))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(36, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(187, 10, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(338, 10, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(489, 10, 111, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plot.setGeometry(QtCore.QRect(36, 160, 568, 60))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.line_b = QtWidgets.QLineEdit(self.centralwidget)
        self.line_b.setGeometry(QtCore.QRect(187, 70, 115, 20))
        self.line_b.setObjectName("line_b")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(187, 50, 111, 16))
        self.label_5.setObjectName("label_5")
        self.line_eps = QtWidgets.QLineEdit(self.centralwidget)
        self.line_eps.setGeometry(QtCore.QRect(489, 70, 115, 20))
        self.line_eps.setObjectName("line_eps")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(489, 50, 111, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Calc.setText(_translate("MainWindow", "Посчитать"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№Корня"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "[xi; xi+1]"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "x\'"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "f(x’)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "N итераций"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Код ошибки"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Функция"))
        self.label_2.setText(_translate("MainWindow", "Точка a"))
        self.label_3.setText(_translate("MainWindow", "Шаг деления h"))
        self.label_4.setText(_translate("MainWindow", "Nmax"))
        self.pushButton_plot.setText(_translate("MainWindow", "Построить график"))
        self.label_5.setText(_translate("MainWindow", "Точка b"))
        self.label_6.setText(_translate("MainWindow", "Точность eps"))



def getresult(text):
    print(text)
    x = 10
    print(eval(text))
    return 0



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
