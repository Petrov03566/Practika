import add_Refilled
from PyQt5 import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class Refilledadd(add_Refilled.Ui_Form):
    def __init__(self,work_id,update_ref):
        super().__init__()
        self.setupUi(self)
        
        self.work_id = work_id
        self.update_ref = update_ref
        self.pushButton_cansel_refilled.clicked.connect(self.exit_refilled)
        self.pb_add_refilled.clicked.connect(self.add_refilled)
        

    def exit_refilled(self):
        self.close()
    
    def add_refilled(self):
            if self.lineEdit_name_printer2.text() and self.lineEdit_diagnostics.text() and self.lineEdit_clearing.text() and self.lineEdit_testing_device.text() and self.lineEdit_necessary.text():
                query_rt = QSqlQuery()
                query_rt.exec(f"INSERT INTO public.Refilled (name_printer2,diagnostics,clearing,testing_device,necessary) VALUES  ('{self.lineEdit_name_printer2.text()}', '{self.lineEdit_diagnostics.text()}','{self.lineEdit_clearing.text()}','{self.lineEdit_testing_device.text()}',{self.lineEdit_necessary.text()})")
                self.update_ref()