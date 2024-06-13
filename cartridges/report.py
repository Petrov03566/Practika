# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Report(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Report")
        self.showFullScreen()
        MainWindow.resize(1526, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_report = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_report.setGeometry(QtCore.QRect(460, 240, 911, 611))
        self.tableWidget_report.setStyleSheet("")
        self.tableWidget_report.setObjectName("tableWidget_report")
        self.tableWidget_report.setColumnCount(6)
        self.tableWidget_report.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_report.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_report.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_report.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_report.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_report.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget_report.setHorizontalHeaderItem(5, item)
        self.tableWidget_report.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_report.horizontalHeader().setStretchLastSection(True)
        self.dateEdit_start = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_start.setGeometry(QtCore.QRect(628, 123, 121, 31))
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.start_date_lbl = QtWidgets.QLabel(self.centralwidget)
        self.start_date_lbl.setGeometry(QtCore.QRect(460, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start_date_lbl.setFont(font)
        self.start_date_lbl.setObjectName("start_date_lbl")
        self.end_date_lbl = QtWidgets.QLabel(self.centralwidget)
        self.end_date_lbl.setGeometry(QtCore.QRect(800, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.end_date_lbl.setFont(font)
        self.end_date_lbl.setObjectName("end_date_lbl")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(1270, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_ready = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ready.setGeometry(QtCore.QRect(1130, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_ready.setFont(font)
        self.pushButton_ready.setStyleSheet("")
        self.pushButton_ready.setObjectName("pushButton_ready")
        self.pushButton_print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print.setGeometry(QtCore.QRect(1270, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_print.setFont(font)
        self.pushButton_print.setStyleSheet("")
        self.pushButton_print.setObjectName("pushButton_print")
        self.dateEdit_end = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_end.setGeometry(QtCore.QRect(965, 122, 121, 31))
        self.dateEdit_end.setObjectName("dateEdit_end")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget_report.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер счета"))
        item = self.tableWidget_report.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Код операции"))
        item = self.tableWidget_report.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget_report.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Операция"))
        item = self.tableWidget_report.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Процент"))
        item = self.tableWidget_report.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Сумма"))
        self.start_date_lbl.setText(_translate("MainWindow", "Стартовая дата:"))
        self.end_date_lbl.setText(_translate("MainWindow", "Конечная дата:"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход"))
        self.pushButton_ready.setText(_translate("MainWindow", "Готово"))
        self.pushButton_print.setText(_translate("MainWindow", "Печать"))
