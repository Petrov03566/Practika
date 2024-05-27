
from add_defective import Add_Defective
from delete_defective import Delete_Defective

from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from main import PrinterMain
class DefectiveAdd(Add_Defective,PrinterMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_add_defective.clicked.connect(self.add_defect_button)
        
        
        
 #Окно добавление данных 
   
    def add_defect_button(self):
        if self.lineEdit_name_pr.text() and self.lineEdit_break.text() and self.lineEdit_flaw.text():
            query_dt = QSqlQuery()
            query_dt.exec(f"INSERT INTO public.Defective (id, name_printer, breaking, flaw) VALUES  ('{self.lineEdit_name_pr.text()}', '{self.lineEdit_break.text()}', '{self.lineEdit_flaw.text()}')")
            