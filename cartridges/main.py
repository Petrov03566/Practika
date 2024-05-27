import sys
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from MainWindow import MainPrinter
from avtoriza import Avtoriza
from auth import Ui_MainWindow
from Defective import Add_Defective,Delete_Defective


#  ##  #########################################ГЛАВНОЕ ОКНО ################################################
class PrinterMain(MainPrinter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_connection()
        self.pb_add_defective.clicked.connect(self.open_button_defect)
    
    def db_connection(self):
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("12345678")
        db.setPort(5432)
        db.setDatabaseName("postgres")
        db.setHostName("localhost")
        db.open()
       

        query = QSqlTableModel()
        sql = "SELECT * FROM public.Defective "
        query.setTable("Defective")
        query.select()
        query.removeColumn(0)
        self.tableView_defective.setModel(query)


        query2 = QSqlTableModel()
        sql = "SELECT * FROM public.Refilled "
        query2.setTable("Refilled")
        query2.select()
        query2.removeColumn(0)
        self.tableView_refueled.setModel(query2)


        query3 = QSqlTableModel()
        sql = "SELECT * FROM public.Working "
        query3.setTable("Working")
        query3.select()
        query3.removeColumn(0)
        self.tableView_working.setModel(query3)
        

        query4 = QSqlTableModel()
        sql = "SELECT * FROM public.On_clade "
        query4.setTable("On_clade")
        query4.select()
        query4.removeColumn(0)
        self.tableView_on_clade.setModel(query4)
    
    def open_button_defect(self):
        self.defect =Add_Defective(tableView_defective= self.tableView_defective)
        self.defect.show()
    



if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =PrinterMain()
    window.show()
    app.exec()