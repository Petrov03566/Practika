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
            rt.exec(f"INSERT INTO public.\"Refilled\" (name_printer2,diagnostics,clearing,testing_device,necessary) VALUES  ('{self.lineEdit_name_printer2.text()}', '{self.lineEdit_diagnostics.text()}','{self.lineEdit_clearing.text()}','{self.lineEdit_testing_device.text()}',{self.lineEdit_necessary.text()})")
            self.update_ref()

            query = QSqlTableModel()
            sql = "SELECT * FROM public.Refilled"
            query.setTable("Refilled")
            query.select()


