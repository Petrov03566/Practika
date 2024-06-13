# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scores.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QSizePolicy

class Scores(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.showFullScreen()
        MainWindow.resize(1918, 1053)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_score_dob = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_score_dob.setGeometry(QtCore.QRect(720, 60, 341, 221))
        self.groupBox_score_dob.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color: rgb(255, 249, 244);")
        self.groupBox_score_dob.setObjectName("groupBox_score_dob")
        self.lineEdit_score_dob_account_number = QtWidgets.QLineEdit(self.groupBox_score_dob)
        self.lineEdit_score_dob_account_number.setGeometry(QtCore.QRect(20, 60, 301, 26))
        self.lineEdit_score_dob_account_number.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_score_dob_account_number.setObjectName("lineEdit_score_dob_account_number")
        self.label_3 = QtWidgets.QLabel(self.groupBox_score_dob)
        self.label_3.setGeometry(QtCore.QRect(20, 37, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_score_dob)
        self.label_4.setGeometry(QtCore.QRect(20, 106, 131, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_score_dob_fio = QtWidgets.QLineEdit(self.groupBox_score_dob)
        self.lineEdit_score_dob_fio.setGeometry(QtCore.QRect(20, 130, 301, 26))
        self.lineEdit_score_dob_fio.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_score_dob_fio.setObjectName("lineEdit_score_dob_fio")
        self.pushButton_score_dob_ok = QtWidgets.QPushButton(self.groupBox_score_dob)
        self.pushButton_score_dob_ok.setGeometry(QtCore.QRect(50, 170, 101, 31))
        self.pushButton_score_dob_ok.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_score_dob_ok.setObjectName("pushButton_score_dob_ok")
        self.pushButton_score_dob_otmn = QtWidgets.QPushButton(self.groupBox_score_dob)
        self.pushButton_score_dob_otmn.setGeometry(QtCore.QRect(180, 170, 101, 31))
        self.pushButton_score_dob_otmn.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_score_dob_otmn.setObjectName("pushButton_score_dob_otmn")
        self.groupBox_score_btn = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_score_btn.setGeometry(QtCore.QRect(530, 60, 171, 201))
        self.groupBox_score_btn.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color: rgb(255, 249, 244);")
        self.groupBox_score_btn.setObjectName("groupBox_score_btn")
        self.pushButton_score_dob = QtWidgets.QPushButton(self.groupBox_score_btn)
        self.pushButton_score_dob.setGeometry(QtCore.QRect(30, 50, 101, 31))
        self.pushButton_score_dob.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_score_dob.setObjectName("pushButton_score_dob")
        self.pushButton_score_edit = QtWidgets.QPushButton(self.groupBox_score_btn)
        self.pushButton_score_edit.setGeometry(QtCore.QRect(30, 90, 101, 31))
        self.pushButton_score_edit.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_score_edit.setObjectName("pushButton_score_edit")
        self.pushButton_score_delete = QtWidgets.QPushButton(self.groupBox_score_btn)
        self.pushButton_score_delete.setGeometry(QtCore.QRect(30, 150, 101, 31))
        self.pushButton_score_delete.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_score_delete.setObjectName("pushButton_score_delete")
        self.groupBox_score_edit = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_score_edit.setGeometry(QtCore.QRect(720, 284, 341, 221))
        self.groupBox_score_edit.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color: rgb(255, 249, 244);")
        self.groupBox_score_edit.setObjectName("groupBox_score_edit")
        self.lineEdit_score_edit_account_number = QtWidgets.QLineEdit(self.groupBox_score_edit)
        self.lineEdit_score_edit_account_number.setGeometry(QtCore.QRect(20, 60, 301, 26))
        self.lineEdit_score_edit_account_number.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_score_edit_account_number.setObjectName("lineEdit_score_edit_account_number")
        self.label_7 = QtWidgets.QLabel(self.groupBox_score_edit)
        self.label_7.setGeometry(QtCore.QRect(20, 37, 121, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_score_edit)
        self.label_8.setGeometry(QtCore.QRect(20, 106, 131, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_score_edit_fio = QtWidgets.QLineEdit(self.groupBox_score_edit)
        self.lineEdit_score_edit_fio.setGeometry(QtCore.QRect(20, 130, 301, 26))
        self.lineEdit_score_edit_fio.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_score_edit_fio.setObjectName("lineEdit_score_edit_fio")
        self.pushButton_score_edit_ok = QtWidgets.QPushButton(self.groupBox_score_edit)
        self.pushButton_score_edit_ok.setGeometry(QtCore.QRect(50, 170, 101, 31))
        self.pushButton_score_edit_ok.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_score_edit_ok.setObjectName("pushButton_score_edit_ok")
        self.pushButton_score_edit_otmn = QtWidgets.QPushButton(self.groupBox_score_edit)
        self.pushButton_score_edit_otmn.setGeometry(QtCore.QRect(180, 170, 101, 31))
        self.pushButton_score_edit_otmn.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_score_edit_otmn.setObjectName("pushButton_score_edit_otmn")
        self.groupBox_operation_dob = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_operation_dob.setGeometry(QtCore.QRect(830, 520, 321, 371))
        self.groupBox_operation_dob.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color: rgb(255, 249, 244);")
        self.groupBox_operation_dob.setObjectName("groupBox_operation_dob")
        self.label_5 = QtWidgets.QLabel(self.groupBox_operation_dob)
        self.label_5.setGeometry(QtCore.QRect(20, 37, 121, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_operation_dob)
        self.label_6.setGeometry(QtCore.QRect(20, 106, 131, 20))
        self.label_6.setObjectName("label_6")
        self.pushButton_operation_dob_ok = QtWidgets.QPushButton(self.groupBox_operation_dob)
        self.pushButton_operation_dob_ok.setGeometry(QtCore.QRect(50, 320, 101, 31))
        self.pushButton_operation_dob_ok.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_operation_dob_ok.setObjectName("pushButton_operation_dob_ok")
        self.pushButton_operation_dob_otmn = QtWidgets.QPushButton(self.groupBox_operation_dob)
        self.pushButton_operation_dob_otmn.setGeometry(QtCore.QRect(180, 320, 101, 31))
        self.pushButton_operation_dob_otmn.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_operation_dob_otmn.setObjectName("pushButton_operation_dob_otmn")
        self.label_9 = QtWidgets.QLabel(self.groupBox_operation_dob)
        self.label_9.setGeometry(QtCore.QRect(20, 169, 131, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_operation_dob)
        self.label_10.setGeometry(QtCore.QRect(20, 240, 141, 31))
        self.label_10.setObjectName("label_10")
        self.lineEdit_operation_dob_amount = QtWidgets.QLineEdit(self.groupBox_operation_dob)
        self.lineEdit_operation_dob_amount.setGeometry(QtCore.QRect(20, 270, 281, 26))
        self.lineEdit_operation_dob_amount.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_operation_dob_amount.setObjectName("lineEdit_operation_dob_amount")
        self.lineEdit_operation_dob_account_number = QtWidgets.QComboBox(self.groupBox_operation_dob)
        self.lineEdit_operation_dob_account_number.setGeometry(QtCore.QRect(20, 60, 281, 26))
        self.lineEdit_operation_dob_account_number.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_operation_dob_account_number.setObjectName("lineEdit_operation_dob_account_number")
        self.dateEdit_operation_dob_date = QtWidgets.QDateEdit(self.groupBox_operation_dob)
        self.dateEdit_operation_dob_date.setGeometry(QtCore.QRect(20, 200, 281, 27))
        self.dateEdit_operation_dob_date.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.dateEdit_operation_dob_date.setObjectName("dateEdit_operation_dob_date")
        self.lineEdit_operation_dob_operation_code = QtWidgets.QComboBox(self.groupBox_operation_dob)
        self.lineEdit_operation_dob_operation_code.setGeometry(QtCore.QRect(20, 130, 281, 26))
        self.lineEdit_operation_dob_operation_code.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_operation_dob_operation_code.setObjectName("lineEdit_operation_dob_operation_code")
        self.groupBox_operation_btn = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_operation_btn.setGeometry(QtCore.QRect(640, 520, 171, 201))
        self.groupBox_operation_btn.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color: rgb(255, 249, 244);")
        self.groupBox_operation_btn.setObjectName("groupBox_operation_btn")
        self.pushButton_operation_dob = QtWidgets.QPushButton(self.groupBox_operation_btn)
        self.pushButton_operation_dob.setGeometry(QtCore.QRect(30, 50, 101, 31))
        self.pushButton_operation_dob.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_operation_dob.setObjectName("pushButton_operation_dob")
        self.pushButton_operation_edit = QtWidgets.QPushButton(self.groupBox_operation_btn)
        self.pushButton_operation_edit.setGeometry(QtCore.QRect(30, 90, 101, 31))
        self.pushButton_operation_edit.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_operation_edit.setObjectName("pushButton_operation_edit")
        self.pushButton_operation_delete = QtWidgets.QPushButton(self.groupBox_operation_btn)
        self.pushButton_operation_delete.setGeometry(QtCore.QRect(30, 150, 101, 31))
        self.pushButton_operation_delete.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_operation_delete.setObjectName("pushButton_operation_delete")
        self.pushButton_all_operation = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_all_operation.setGeometry(QtCore.QRect(660, 740, 121, 31))
        self.pushButton_all_operation.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_all_operation.setObjectName("pushButton_all_operation")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 500, 1161, 511))
        self.frame_2.setStyleSheet("background-color: rgb(255, 249, 244);\n"
"border-radius: 10px;  \n"
"border: 2px solid #FF6C00;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 510, 241, 31))
        self.label_2.setStyleSheet("font: 18pt \"Open Sans\";")
        self.label_2.setObjectName("label_2")
        self.tableView_operation = QtWidgets.QTableView(self.centralwidget)
        self.tableView_operation.setGeometry(QtCore.QRect(30, 550, 571, 391))
        self.tableView_operation.setObjectName("tableView_operation")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 251, 31))
        self.label.setStyleSheet("font: 18pt \"Open Sans\";")
        self.label.setObjectName("label")
        self.tableView_score = QtWidgets.QTableView(self.centralwidget)
        self.tableView_score.setGeometry(QtCore.QRect(30, 80, 461, 321))
        self.tableView_score.setObjectName("tableView_score")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 29, 1071, 391))
        self.frame.setStyleSheet("background-color: rgb(255, 249, 244);\n"
"border-radius: 10px;  \n"
"border: 2px solid #FF6C00;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(1730, 30, 101, 31))
        self.pushButton_back.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(1730, 70, 101, 31))
        self.pushButton_exit.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_report = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_report.setGeometry(QtCore.QRect(1580, 30, 101, 31))
        self.pushButton_report.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_report.setObjectName("pushButton_report")
        self.pushButton_help = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_help.setGeometry(QtCore.QRect(1580, 70, 101, 31))
        self.pushButton_help.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_help.setObjectName("pushButton_help")
        self.tableView_list_operation = QtWidgets.QTableView(self.centralwidget)
        self.tableView_list_operation.setGeometry(QtCore.QRect(1200, 280, 701, 711))
        self.tableView_list_operation.setObjectName("tableView_list_operation")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1220, 140, 251, 31))
        self.label_17.setStyleSheet("font: 18pt \"Open Sans\";")
        self.label_17.setObjectName("label_17")
        self.groupBox_operation_edit = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_operation_edit.setGeometry(QtCore.QRect(440, 330, 321, 371))
        self.groupBox_operation_edit.setStyleSheet("font: 12pt \"Open Sans\";\n"
"background-color: rgb(255, 249, 244);")
        self.groupBox_operation_edit.setObjectName("groupBox_operation_edit")
        self.label_11 = QtWidgets.QLabel(self.groupBox_operation_edit)
        self.label_11.setGeometry(QtCore.QRect(20, 37, 121, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_operation_edit)
        self.label_12.setGeometry(QtCore.QRect(20, 106, 131, 20))
        self.label_12.setObjectName("label_12")
        self.pushButton_operation_edit_ok = QtWidgets.QPushButton(self.groupBox_operation_edit)
        self.pushButton_operation_edit_ok.setGeometry(QtCore.QRect(50, 320, 101, 31))
        self.pushButton_operation_edit_ok.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_operation_edit_ok.setObjectName("pushButton_operation_edit_ok")
        self.pushButton_operation_edit_otmn = QtWidgets.QPushButton(self.groupBox_operation_edit)
        self.pushButton_operation_edit_otmn.setGeometry(QtCore.QRect(180, 320, 101, 31))
        self.pushButton_operation_edit_otmn.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_operation_edit_otmn.setObjectName("pushButton_operation_edit_otmn")
        self.label_13 = QtWidgets.QLabel(self.groupBox_operation_edit)
        self.label_13.setGeometry(QtCore.QRect(20, 169, 131, 31))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_operation_edit)
        self.label_14.setGeometry(QtCore.QRect(20, 240, 141, 31))
        self.label_14.setObjectName("label_14")
        self.lineEdit_operation_edit_amount = QtWidgets.QLineEdit(self.groupBox_operation_edit)
        self.lineEdit_operation_edit_amount.setGeometry(QtCore.QRect(20, 270, 281, 26))
        self.lineEdit_operation_edit_amount.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_operation_edit_amount.setObjectName("lineEdit_operation_edit_amount")
        self.lineEdit_operation_edit_account_number = QtWidgets.QComboBox(self.groupBox_operation_edit)
        self.lineEdit_operation_edit_account_number.setGeometry(QtCore.QRect(20, 60, 281, 26))
        self.lineEdit_operation_edit_account_number.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_operation_edit_account_number.setObjectName("lineEdit_operation_edit_account_number")
        self.dateEdit_operation_edit_date = QtWidgets.QDateEdit(self.groupBox_operation_edit)
        self.dateEdit_operation_edit_date.setGeometry(QtCore.QRect(20, 200, 281, 27))
        self.dateEdit_operation_edit_date.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.dateEdit_operation_edit_date.setObjectName("dateEdit_operation_edit_date")
        self.lineEdit_operation_edit_operation_code = QtWidgets.QComboBox(self.groupBox_operation_edit)
        self.lineEdit_operation_edit_operation_code.setGeometry(QtCore.QRect(20, 130, 281, 26))
        self.lineEdit_operation_edit_operation_code.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_operation_edit_operation_code.setObjectName("lineEdit_operation_edit_operation_code")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1190, 130, 721, 881))
        self.frame_3.setStyleSheet("background-color: rgb(255, 249, 244);\n"
"border-radius: 10px;  \n"
"border: 2px solid #FF6C00;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit_list_account_number = QtWidgets.QComboBox(self.frame_3)
        self.lineEdit_list_account_number.setGeometry(QtCore.QRect(290, 60, 281, 26))
        self.lineEdit_list_account_number.setStyleSheet("border-radius: 5px;  \n"
"border: 2px solid #FF6C00;")
        self.lineEdit_list_account_number.setObjectName("lineEdit_list_account_number")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1220, 190, 241, 21))
        self.label_18.setStyleSheet("font: 12pt \"Open Sans\";")
        self.label_18.setObjectName("label_18")
        self.pushButton_list_ok = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_list_ok.setGeometry(QtCore.QRect(1650, 230, 101, 31))
        self.pushButton_list_ok.setStyleSheet("font: 13pt \"Open Sans\";")
        self.pushButton_list_ok.setObjectName("pushButton_list_ok")
        self.frame_3.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.groupBox_score_dob.raise_()
        self.groupBox_score_btn.raise_()
        self.groupBox_score_edit.raise_()
        self.groupBox_operation_dob.raise_()
        self.groupBox_operation_btn.raise_()
        self.pushButton_all_operation.raise_()
        self.label_2.raise_()
        self.tableView_operation.raise_()
        self.label.raise_()
        self.tableView_score.raise_()
        self.pushButton_back.raise_()
        self.pushButton_exit.raise_()
        self.pushButton_report.raise_()
        self.pushButton_help.raise_()
        self.tableView_list_operation.raise_()
        self.label_17.raise_()
        self.groupBox_operation_edit.raise_()
        self.label_18.raise_()
        self.pushButton_list_ok.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Изменения:
        self.groupBox_score_edit.setGeometry(QtCore.QRect(720, 60, 341, 221))
        self.groupBox_score_dob.setVisible(False)
        self.groupBox_score_edit.setVisible(False)
        self.groupBox_operation_edit.setGeometry(QtCore.QRect(830, 520, 321, 371))
        self.groupBox_operation_dob.setVisible(False)
        self.groupBox_operation_edit.setVisible(False)
        self.lineEdit_operation_dob_account_number.setMinimumWidth(100)
        self.lineEdit_operation_dob_account_number.setMaximumHeight(200)
        self.lineEdit_operation_dob_account_number.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_score_dob.setTitle(_translate("MainWindow", "Добавить данные:"))
        self.label_3.setText(_translate("MainWindow", "Номер счета:"))
        self.label_4.setText(_translate("MainWindow", "ФИО владельца:"))
        self.pushButton_score_dob_ok.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_score_dob_otmn.setText(_translate("MainWindow", "Отмена"))
        self.groupBox_score_btn.setTitle(_translate("MainWindow", "Выберите операцию:"))
        self.pushButton_score_dob.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_score_edit.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_score_delete.setText(_translate("MainWindow", "Удалить"))
        self.groupBox_score_edit.setTitle(_translate("MainWindow", "Изменить данные:"))
        self.label_7.setText(_translate("MainWindow", "Номер счета:"))
        self.label_8.setText(_translate("MainWindow", "ФИО владельца:"))
        self.pushButton_score_edit_ok.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_score_edit_otmn.setText(_translate("MainWindow", "Отмена"))
        self.groupBox_operation_dob.setTitle(_translate("MainWindow", "Добавить данные:"))
        self.label_5.setText(_translate("MainWindow", "Номер счета:"))
        self.label_6.setText(_translate("MainWindow", "Код операции:"))
        self.pushButton_operation_dob_ok.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_operation_dob_otmn.setText(_translate("MainWindow", "Отмена"))
        self.label_9.setText(_translate("MainWindow", "Дата операции:"))
        self.label_10.setText(_translate("MainWindow", "Сумма операции:"))
        self.groupBox_operation_btn.setTitle(_translate("MainWindow", "Выберите операцию:"))
        self.pushButton_operation_dob.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_operation_edit.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_operation_delete.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_all_operation.setText(_translate("MainWindow", "Все операции"))
        self.label_2.setText(_translate("MainWindow", "Операции по счету:"))
        self.label.setText(_translate("MainWindow", "Имеющиеся счета:"))
        self.pushButton_back.setText(_translate("MainWindow", "Назад"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выйти"))
        self.pushButton_report.setText(_translate("MainWindow", "Отчет"))
        self.pushButton_help.setText(_translate("MainWindow", "Справка"))
        self.label_17.setText(_translate("MainWindow", "Перечень операций:"))
        self.groupBox_operation_edit.setTitle(_translate("MainWindow", "Изменить данные:"))
        self.label_11.setText(_translate("MainWindow", "Номер счета:"))
        self.label_12.setText(_translate("MainWindow", "Код операции:"))
        self.pushButton_operation_edit_ok.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_operation_edit_otmn.setText(_translate("MainWindow", "Отмена"))
        self.label_13.setText(_translate("MainWindow", "Дата операции:"))
        self.label_14.setText(_translate("MainWindow", "Сумма операции:"))
        self.label_18.setText(_translate("MainWindow", "Выберите счет для просмотра:"))
        self.pushButton_list_ok.setText(_translate("MainWindow", "Выбрать"))
