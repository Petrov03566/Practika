# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_refilled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 100)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 0, 430, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_yes_refilled = QtWidgets.QPushButton(Form)
        self.pushButton_yes_refilled.setGeometry(QtCore.QRect(30, 70, 75, 23))
        self.pushButton_yes_refilled.setObjectName("pushButton_yes_refilled")
        self.pushButton_no_refilled = QtWidgets.QPushButton(Form)
        self.pushButton_no_refilled.setGeometry(QtCore.QRect(400, 70, 75, 23))
        self.pushButton_no_refilled.setObjectName("pushButton_no_refilled")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Вы точно хотите удалить строку !"))
        self.pushButton_yes_refilled.setText(_translate("Form", "да "))
        self.pushButton_no_refilled.setText(_translate("Form", "нет"))
