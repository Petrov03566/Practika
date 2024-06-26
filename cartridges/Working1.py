import add_Working,delete_working
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel,QSqlQueryModel
from PyQt5.QtWidgets import  QApplication,QHeaderView,QMainWindow,QWidget,QTableView

class Working(add_Working.Ui_Form):
    def __init__(self,def_id,update_work,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_work_button)
        self.pushButton_2.clicked.connect(self.exit_ward)
      
        self.dep_id = def_id
        self.update_work = update_work

    def exit_ward(self):
        self.close()
    
    def add_work_button(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            query_wk = QSqlQuery()
            query_wk.exec(f"INSERT INTO public.Working (name_printer3, place_establishment) VALUES ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}')")
            self.update_work()

class DeleteWorking(delete_working.Ui_Form):
    def __init__(self,tableView_working:QTableView,update_workking): 
        super().__init__()
        self.setupUi(self)  
        self.metroUpdate =update_workking
        row = tableView_working.currentIndex().row()
        self.id = tableView_working.model().index(row,0).data()
        self.pushButton_yes_working.clicked.connect(self.Okaction2)
        self.pushButton_no_working.clicked.connect(self.CanselActiom2)

    def Okaction2(self):
        sql =f"DELETE FROM public.Working WHERE id ='{self.id}'"
        query =QSqlQuery()
        query.exec(sql)
        self.metroUpdate()
        self.close()

    def CanselActiom2(self):
        self.close()