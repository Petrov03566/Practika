from add_Working import Add_Working
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class WorkingAdd(Add_Working):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_work_button)
        
    
    def add_work_button(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            query_wk = QSqlQuery()
            query_wk.exec(f"INSERT INTO public.Working (id, name_printer3,place_establishment) VALUES  ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}',')")