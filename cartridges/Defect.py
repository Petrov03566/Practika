from PyQt5 import QtCore 
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel,QSqlQueryModel
from PyQt5.QtWidgets import  QApplication,QHeaderView,QMainWindow,QWidget,QTableView
import add_defective,delete_defective

class Defective(add_defective.Ui_MainWindow):
    def __init__(self,  update_def,parent=None): 
        super().__init__(parent)
        self.setupUi(self)
    
        self.update_def =update_def 
        
        self.pushButton_add_pr.clicked.connect(self.add_b_defective)
        self.pushButton_cansel_pr.clicked.connect(self.add_cansel_defective)
    

    def add_b_defective(self):
        if self.lineEdit_name_pr.text() and self.lineEdit_break.text() and self.lineEdit_flaw.text():
            query_dt = QSqlQuery()
            query_dt.exec(f"INSERT INTO public.Defective(name_printer, breaking, flaw) VALUES ('{self.lineEdit_name_pr.text()}','{self.lineEdit_break.text()}','{self.lineEdit_flaw.text()}')")                
            self.update_def()
    
            
            print("Database connection established")
        else:
            print("Error inserting data:", query_dt.lastError().text())

            
    def add_cansel_defective(self):
        self.close()

class DeleteDefective(delete_defective.Ui_MainWindow):
    def __init__(self,tableView_defective:QTableView,update): 
        super().__init__()
        self.setupUi(self)  
        self.metroUpdate =update
        row = tableView_defective.currentIndex().row()
        self.id = tableView_defective.model().index(row,0).data()
        self.pb_yes_defective.clicked.connect(self.Okaction)
        self.pB_no_defective.clicked.connect(self.CanselActiom)

    def Okaction(self):
        sql =f"DELETE FROM public.Defective WHERE id ='{self.id}'"
        query =QSqlQuery()
        query.exec(sql)
        self.metroUpdate()
        self.close()

    def CanselActiom(self):
        self.close()
