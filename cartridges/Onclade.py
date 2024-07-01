import add_On_clade
from PyQt5 import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class Oncladeadd(add_On_clade.Ui_Form):
    def __init__(self,update_Onclade,work_id,parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.work_id =work_id
        self.update_Onclade =update_Onclade
        self.pushButton_add_onclade.clicked.connect(self.add_Onclade)
        self.pushButton_exit_onclade.clicked.connect(self.exit_onclade)

    def exit_onclade(self):
        self.close()

    
    def add_Onclade(self):
        if self.lineEdit_nameprinter4.text() and self.lineEdit_port_number.text() and self.lineEdit_serial_number.text():
            query_on = QSqlQuery()
            query_on.exec(f"INSERT INTO public.\"On_clade\" (name_printer4,serial_number,port_number) VALUES ('{self.lineEdit_nameprinter4.text()}', '{self.lineEdit_serial_number.text()}','{self.lineEdit_port_number.text()}')")
            self.update_Onclade()

            query_on = QSqlTableModel()
            sql = "SELECT * FROM public.On_clade"
            query_on.setTable("On_clade")
            query_on.select()

