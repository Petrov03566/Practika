
from add_defective import Add_Defective
from delete_defective import Delete_Defective
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from main import PrinterMain
class DefectiveAdd(PrinterMain,Add_Defective):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_add_defective.clicked.connect(self.add_defect_button)
        self.pushButton_cansel_pr.clicked.connect(self.add_cl_defective)
        
        

       

 #Окно добавление данных 
    def add_defect_button(self):
        if self.lineEdit_break.text() and  self.lineEdit_flaw.text() and self.lineEdit_name_pr.text():
            query_dt = QSqlQuery()
            query_dt.exec(f"SELECT * FROM public.Defective(id,name_printer,breaking,flaw VALUES('{self.lineEdit_break.text()}',))")
            self.close()
            

    def add_cl_defective(self):
        self.close()

        
    



# class DefectiveDelete(Delete_Defective):
#     def __init__(self):
#         super().__init__()

        
        


        
