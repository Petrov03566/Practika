import add_Refilled,delete_refilled
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel,QSqlQueryModel
from PyQt5.QtWidgets import  QApplication,QHeaderView,QMainWindow,QWidget,QTableView

class Refilled(add_Refilled.Ui_Form):
    def __init__(self,work_id,update_ref,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.work_id = work_id
        self.update_ref = update_ref
        self.pushButton_cansel_refilled.clicked.connect(self.exit_refilled)
        self.pb_add_refilled.clicked.connect(self.add_refilled)
        

    def exit_refilled(self):
        self.close()
    
    def add_refilled(self):
        if self.lineEdit_name_printer2.text() and self.lineEdit_diagnostics.text() and self.lineEdit_clearing.text() and self.lineEdit_testing_device.text() and self.lineEdit_necessary.text():
            query_rt =QSqlQueryModel
            rt = QSqlQuery()
            rt.exec(f"INSERT INTO public.Refilled (name_printer2,diagnostics,clearing,testing_device,necessary) VALUES  ('{self.lineEdit_name_printer2.text()}', '{self.lineEdit_diagnostics.text()}','{self.lineEdit_clearing.text()}','{self.lineEdit_testing_device.text()}',{self.lineEdit_necessary.text()})")
            self.update_ref()

class DeleteRefilled(delete_refilled.Ui_Form):
    def __init__(self,tableView_refilled:QTableView,update_reffiled): 
        super().__init__()
        self.setupUi(self)  
        self.metroUpdate =update_reffiled
        row = tableView_refilled.currentIndex().row()
        self.id = tableView_refilled.model().index(row,0).data()
        self.pushButton_yes_refilled.clicked.connect(self.Okaction)
        self.pushButton_no_refilled.clicked.connect(self.CanselActiom)

    def Okaction(self):
        sql =f"DELETE FROM public.Reffiled WHERE id ='{self.id}'"
        query3 =QSqlQuery()
        query3.exec(sql)
        self.metroUpdate()
        self.close()

    def CanselActiom(self):
        self.close()


