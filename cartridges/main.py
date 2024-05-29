from PyQt5 import *
import sys
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import MainWindow
import add_Working
import add_defective
import delete_defective

#  ##  #########################################ГЛАВНОЕ ОКНО ################################################
class PrinterMain(MainWindow.MainPrinter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
         
        self.current_def = 0
        self.current_work = 0

        self.tableView_defective.clicked.connect(self.dp_clicked)
        self.pb_add_defective.clicked.connect(self.add_Defective_button)
        # self.pb_add_working.clicked.connect(self.add_Ward_Button)
        
        
    
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("12345678")
        db.setPort(5432)
        db.setDatabaseName("postgres")
        db.setHostName("localhost")
        db.open()

        self.update_def()
        self.update_work()
       
    
        query = QSqlTableModel()
        sql = "SELECT * FROM public.Defective "
        query.setTable("Defective")
        query.select()
        query.removeColumn(0)
        self.tableView_defective.setModel(query)

   

        query2 = QSqlTableModel()
        sql = "SELECT * FROM public.Refilled"
        query2.setTable("Refilled")
        query2.select()
        query2.removeColumn(0)
        self.tableView_refueled.setModel(query2)

        query3 = QSqlTableModel()
        sql = "SELECT * FROM public.Working"
        query3.setTable("Working")
        query3.select()
        query3.removeColumn(0)
        self.tableView_working.setModel(query3)

        query4 = QSqlTableModel()
        sql = "SELECT * FROM public.On_clade"
        query4.setTable("On_clade")
        query4.select()
        query4.removeColumn(0)
        self.tableView_on_clade.setModel(query4)

    def add_Defective_button(self):
        self.add_d = Defective_Add(self.update_def)
        self.add_d.show()

   
        
    # def add_Ward_Button(self):
    #     self.add_w = WorkingAdd(self.current_def, self.update_work)
    #     self.add_w.show()

 

    def dp_clicked(self):
        row = self.tableView_defective.selectedIndexes()[0].row()
        self.current_dep = self.tableView_defective.model().index(row, 0).data()

    def ward_clicked(self):
        row = self.tableView_working.selectedIndexes()[0].row()
        self.current_work = self.tableView_working.model().index(row, 0).data()
    
    def update_def(self):
        query = QSqlTableModel()
        query.setTable("Defective")
        query.select()
        self.tableView_defective.setModel(query)
    
    def update_ref(self):
        query = QSqlTableModel()
        query.setTable("Refilled")
        query.select()
        self.tableView_refueled.setModel(query)
    
    def update_work(self):
        query = QSqlTableModel()
        query.setTable("Working")
        query.select()
        self.tableView_working.setModel(query)


class  Defective_Add(add_defective.Add_Defective):
    def __init__(self,update_def):
        super().__init__()
        self.setupUi(self)
    
        self.update_def = update_def
        
        self.pushButton_add_pr.clicked.connect(self.add_b_defective)
        self.pushButton_cansel_pr.clicked.connect(self.exit_defect)
        
        
 #Окно добавление данных 
    def exit_defect(self):
        self.close()

    def add_b_defective(self):
            query_dt = QSqlQuery()
            query_dt.exec(f"INSERT INTO public.Defective (name_printer,breaking,flaw) VALUES ('{self.lineEdit_name_pr.text()}', '{self.lineEdit_break.text()}', '{self.lineEdit_flaw.text()}')")
            self.update_def()

    
class WorkingAdd(add_Working.Add_Working):
    def __init__(self,update_work):
        super().__init__()
        self.setupUi(self)

        self.update_wok =update_work
        self.pushButton.clicked.connect(self.add_work_button)
        
    
    def add_work_button(self):
        if self.lineEdit.text() and self.lineEdit_2.text():
            query_wk = QSqlQuery()
            query_wk.exec(f"INSERT INTO public.Working (name_printer3,place_establishment) VALUES  ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}',')")
        

    
    
if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =PrinterMain()
    window.show()
    app.exec()