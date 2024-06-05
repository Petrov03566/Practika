from add_defective import Ui_MainWindow
import delete_defective
from PyQt5 import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *




class Defectiveadd(Ui_MainWindow):
    def init(self,tableView_defective,update_def):
        super().__init__()
        self.setupUi(self)
        
        self.update_def =update_def
        self.tableView_defective =tableView_defective
        self.pushButton_add_pr.clicked.connect(self.add_b_defective)
    

    def add_b_defective(self):
        if self.lineEdit_name_pr.text() and self.lineEdit_break.text() and self.lineEdit_flaw.text():
            query_dt = QSqlQuery()
            query_dt.exec(f"INSERT INTO public.Defective(name_printer, breaking, flaw) VALUES ('{self.lineEdit_name_pr.text()}', '{self.lineEdit_break.text()}', '{self.lineEdit_flaw.text()}')")
            self.tableView_defective()
            

class DefectDelete(delete_defective.Ui_MainWindow):
    def init(self):
        super().__init__()
        self.setupUi(self)
   
        self.pB_no_defective.clicked.connect(self.delete_no_defect)
    
    def delete_no_defect(self):
        self.close