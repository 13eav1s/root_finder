'''
Нахождение корней функции комбинированным методом
Краснов Леонид ИУ7-21Б
'''

"""
Необходимо вычислить корни функции на отрезке [a; b] заданным методом. Для вычисления отрезок [a; b] делится на
элементарные отрезки с шагом h. На каждом элементарном отрезке у функции не более одного корня. Для каждого
элементарного отрезка, на котором есть корень, итерационно вычисляется приближенное значение корня с заданной точностью
eps. Для обнаружения медленного процесса сходимости или расходимости метода количество итераций ограничивается числом
Nmax.
Исходные данные: функция в аналитическом виде, начало и конец отрезка a, b, шаг деления отрезка h, максимальное
количество итераций Nmax, точность eps.
Получаемые значения:
[xi; xi+1] – элементарный отрезок, на котором производится вычисление корня функции
заданным методом,
x’ – приближенное значение корня,
f(x’) – значение функции в точке корня (данная величина является вещественным числом в нормальной форме, вводится с
одним значащим разрядом в мантиссе),
Код ошибки – числовое значение, отражающее причину невозможности определения приближенного значения корня функции на
данном интервале заданным методом.
2) график функции на отрезке [a; b], на котором отмечаются корни, экстремумы и точки перегиба функции. Для построения
графика используется библиотека matplotlib.
Вариант 6 метод: комбинированный;
"""

from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QTableWidget, QTableWidgetItem
from math import *
from matplotlib import pyplot as plt

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
        self.pushButton_Calc.clicked.connect(lambda: get_all(self.line_func.text(), self.line_a.text(),
                                                             self.line_b.text(), self.line_h.text(),
                                                             self.line_Nmax.text(), self.line_eps.text(),
                                                             self.tableWidget))
        self.pushButton_plot.clicked.connect(lambda: plot_graph(self.line_func.text(), self.line_a.text(),
                                                                self.line_b.text()))

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
        # self.tableWidget.setRowCount(1)
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
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Функция"))
        self.label_2.setText(_translate("MainWindow", "Точка a"))
        self.label_3.setText(_translate("MainWindow", "Шаг деления h"))
        self.label_4.setText(_translate("MainWindow", "Nmax"))
        self.pushButton_plot.setText(_translate("MainWindow", "Построить график"))
        self.label_5.setText(_translate("MainWindow", "Точка b"))
        self.label_6.setText(_translate("MainWindow", "Точность eps"))


def derivative1(x, dx, func):
    return (f(x + dx, func) - f(x, func)) / dx


def derivative2(x, dx, func):
    return (derivative1(x + dx, dx, func) - derivative1(x, dx, func)) / dx


def maina():
    dx = 0.00001
    func = str(input("Введите функцию: "))
    a = float(input("Введите начало отрезка: "))
    b = float(input("Введите конец отрезка: "))
    h = float(input("Введите шаг: "))
    eps = float(input("Введите допустимую погрешность: "))
    x1 = a
    x2 = a + h
    flag = 0
    while x2 < b + h / 2:
        if f(x1, func) * derivative2(x1, dx, func) > 0 > f(x2, func) * derivative2(x2, dx, func):
            while abs(x1 - x2) >= eps:
                newx1 = x1 - (f(x1, func) / derivative1(x1, dx, func))
                newx2 = x2 - ((x1 - x2) / (f(x1, func) - f(x2, func))) * f(x2, func)
                x1 = newx1
                x2 = newx2
            print((x1 + x2) / 2)
            flag = 1
        elif f(x1, func) * derivative2(x1, dx, func) < 0 < f(x2, func) * derivative2(x2, dx, func):
            while abs(x1 - x2) >= eps:
                newx1 = x2 - ((x1 - x2) / (f(x1, func) - f(x2, func))) * f(x2, func)
                newx2 = x1 - (f(x1, func) / derivative1(x1, dx, func))
                x1 = newx1
                x2 = newx2
            print((x1 + x2) / 2)
            flag = 1
        else:
            print("На отрезке больше одного корня или корней нет")
        x1 = x2
        x2 += h
    if flag == 0:
        print("Нет корней на введенном вами интервале")
    return 0


def f(x, func):
    y = eval(func)
    return y


def tangent(func, dx, x):
    k = derivative1(x, dx, func)
    b = f(x, func) - k * x
    y = str(k) + "*x+" + str(b)
    return y


def linearity_test(func, a, b, dx):
    rez = 0
    x = a
    while x < b:
        rez += f(x, func) - f(x, tangent(func, dx, a))
        x += 1
    if abs(rez) < 0.1:
        mess = QtWidgets.QMessageBox()
        mess.setText("Вы ввели линейную функцию!")
        mess.exec()
        return 0
    else:
        return 1


def get_all(func, a, b, h, Nmax, eps, tab):
    mess = QtWidgets.QMessageBox()
    mess.setText("Коды ошибок:\n 0: Ошибки нет \n 1: Превышено количество итераций \n 2: Не найден существующий корень")
    mess.exec()
    info = []
    if func == "" or a == "" or b == "" or h == "" or Nmax == "" or eps == "":
        mess = QtWidgets.QMessageBox()
        mess.setText("Вы не ввели один из параметров!")
        mess.exec()
        return 0
    a = float(a)
    b = float(b)
    h = float(h)
    Nmax = float(Nmax)
    eps = float(eps)
    info.append(func)
    info.append(a)
    info.append(b)
    info.append(h)
    info.append(Nmax)
    info.append(eps)

    dx = 0.00001
    x1 = a
    x2 = a + h
    flag = 0
    N = 0
    solve_index = 0
    tab.setRowCount(0)

    #  Проверка функции на линейность
    if linearity_test(func, a, b, dx) == 0:
        return 0

        #  разделяем заданный интервал на отрезки длины h
    c = a
    d = c + h
    while d <= b + h:
        x0 = c
        x1 = d
        #  проверка на существования корня на заданном отрезке
        if f(x0, func) * f(x1, func) > 0:
            c = d
            d += h
            continue
        else:
            tab.insertRow(tab.rowCount())

            item = QtWidgets.QTableWidgetItem()
            tab.setItem(N, 1, item)
            item = tab.item(N, 1)
            item_text = "[" + str(x0) + "; " + str(x1) + "]"
            item.setText(item_text)
            iter_num = 0
            #  Нахожедние корня
            while True:
                iter_num += 1
                if f(x0, func) * derivative2(x0, dx, func) < 0:
                    x0 = x0 - f(x0, func) * (x0 - x1) / (f(x0, func) - f(x1, func))
                elif f(x0, func) * derivative2(x0, dx, func) > 0:
                    x0 = x0 - f(x0, func) / derivative1(x0, dx, func)

                if f(x1, func) * derivative2(x1, dx, func) < 0:
                    x1 = x1 - f(x1, func) * (x1 - x0) / (f(x1, func) - f(x0, func))
                elif f(x1, func) * derivative2(x1, dx, func) > 0:
                    x1 = x1 - f(x1, func) / derivative1(x1, dx, func)

                if abs(x1 - x0) <= 2 * eps:
                    break

                if iter_num >= Nmax:
                    item = QtWidgets.QTableWidgetItem()
                    tab.setItem(N, 2, item)
                    item = tab.item(N, 2)
                    item_text = str(round((x1 + x0) / 2, 2))
                    item.setText(item_text)

                    item = QtWidgets.QTableWidgetItem()
                    tab.setItem(N, 3, item)
                    item = tab.item(N, 3)
                    item_text = str(round(f((x1 + x0) / 2, func), 2))
                    item.setText(item_text)

                    item = QtWidgets.QTableWidgetItem()
                    tab.setItem(N, 4, item)
                    item = tab.item(N, 4)
                    item_text = str(iter_num)
                    item.setText(item_text)

                    item = QtWidgets.QTableWidgetItem()
                    tab.setItem(N, 5, item)
                    item = tab.item(N, 5)
                    item_text = "1"
                    item.setText(item_text)

                    item = QtWidgets.QTableWidgetItem()
                    tab.setItem(N, 0, item)
                    item = tab.item(N, 0)
                    item.setText(str(solve_index + 1))
                    break



            if (x1 + x0) / 2 > b:
                item = QtWidgets.QTableWidgetItem()
                tab.setItem(N, 2, item)
                item = tab.item(N, 2)
                item_text = "-"
                item.setText(item_text)

                item = QtWidgets.QTableWidgetItem()
                tab.setItem(N, 0, item)
                item = tab.item(N, 0)
                item.setText(item_text)

                item = QtWidgets.QTableWidgetItem()
                tab.setItem(N, 3, item)
                item = tab.item(N, 3)
                item.setText(item_text)

                item = QtWidgets.QTableWidgetItem()
                tab.setItem(N, 4, item)
                item = tab.item(N, 4)
                item.setText(item_text)

                item = QtWidgets.QTableWidgetItem()
                tab.setItem(N, 5, item)
                item = tab.item(N, 5)
                item.setText(item_text)
                return 0


            item = QtWidgets.QTableWidgetItem()
            tab.setItem(N, 2, item)
            item = tab.item(N, 2)
            item_text = str(round((x1 + x0) / 2, 2))
            item.setText(item_text)

            item = QtWidgets.QTableWidgetItem()
            tab.setItem(N, 3, item)
            item = tab.item(N, 3)
            item_text = str(round(f((x1 + x0) / 2, func), 2))
            item.setText(item_text)

            item = QtWidgets.QTableWidgetItem()
            tab.setItem(N, 4, item)
            item = tab.item(N, 4)
            item_text = str(iter_num)
            item.setText(item_text)

            item = QtWidgets.QTableWidgetItem()
            tab.setItem(N, 5, item)
            item = tab.item(N, 5)
            if abs(x0 + x1)/2 > d:
                item_text = "2"
            elif iter_num >= Nmax:
                item_text = "1"
            elif iter_num < Nmax:
                item_text = "0"
            item.setText(item_text)

            item = QtWidgets.QTableWidgetItem()
            tab.setItem(N, 0, item)
            item = tab.item(N, 0)
            item.setText(str(solve_index + 1))

            solve_index += 1

            flag = 1
            N += 1

        c = d
        d += h
    if flag == 0:
        mess = QtWidgets.QMessageBox()
        mess.setText("На заданном отрезке нет ни одного корня!")
        mess.show()
    return 0


def inflection_point(func, a, b):
    eps = 1e-3
    h = 1e-3
    x = []
    x0 = a
    while x0 < b:
        if abs(derivative2(x0, 0.001, str(func))) < eps:
            x.append(x0)
        x0 += h
    y = []
    for i in x:
        y.append(f(i, func))
    return x, y


def extreme_point(func, a, b):
    eps = 1e-3
    h = 1e-3
    x = []
    x0 = a
    while x0 < b:
        if abs(derivative1(x0, 0.0001, func)) < eps:
            x.append(x0)
        x0 += h
    y = []
    for i in x:
        y.append(f(i, func))
    return x, y


def root_point(func, a, b):
    eps = 1e-3
    h = 1e-3
    x = []
    y = []
    x0 = a
    while x0 < b:
        if abs(f(x0, func)) < eps:
            x.append(x0)
        x0 += h
    for i in x:
        y.append(f(i, func))
    return x, y


def plot_graph(func, a, b):
    graph = plt
    a = float(a)
    b = float(b)
    h = 1e-2

    inflections_x, inflections_y = inflection_point(func, a, b)

    extreme_x, extreme_y = extreme_point(func, a, b)

    root_x, root_y = root_point(func, a, b)

    mask = 0

    plt.scatter(inflections_x[mask], inflections_y[mask], c='red', s=40, marker='x', label='Точки перегиба')
    plt.scatter(extreme_x[mask], extreme_y[mask], c='orange', s=40, marker='o', label='Экстремиумы')
    plt.scatter(root_x[mask], root_y[mask], c='blue', s=40, marker='d', label='Корни')

    plt.legend(loc="upper left")



    for mask in range(1, len(inflections_y)):
        plt.scatter(inflections_x[mask], inflections_y[mask], c='red', s=40, marker='x', label='Точки перегиба')

    for mask in range(1, len(extreme_x)):
        plt.scatter(extreme_x[mask], extreme_y[mask], c='orange', s=40, marker='o', label='Экстремиумы')

    for mask in range(1, len(root_y)):
        plt.scatter(root_x[mask], root_y[mask], c='blue', s=40, marker='d', label='Корни')

    x = []
    y = []

    while a < b:
        x.append(a)
        y.append(f(a, func))
        a += h
    graph.plot(x, y)
    graph.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
