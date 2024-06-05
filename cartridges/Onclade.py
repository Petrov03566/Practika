import add_On_clade
from PyQt5 import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class Oncladeadd(add_On_clade.Ui_Form):
    def __init__(self,update_Onclade):
        super().__init__()
        self.setupUi(self)

        self.update_Onclade =update_Onclade
        self.pushButton_add_onclade.clicked.connect(self.add_Onclade)
        self.pushButton_exit_onclade.clicked.connect(self.exit_onclade)

    def exit_onclade(self):
        self.close()

    
    def add_Onclade(self):
        query_rt = QSqlQuery()
        query_rt.exec(f"INSERT INTO public.On_clade (name_printer4,serial_number,port_number) VALUES  ('{self.lineEdit_nameprinter4.text()}', '{self.lineEdit_serial_number.text()}','{self.lineEdit_port_number.text()}')")
        