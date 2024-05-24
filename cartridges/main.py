import sys ,psycopg2 
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
        self.pb_add_defective.clicked.connect(self.add_defect)
    
    def db_connection(self):
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("12345678")
        db.setPort(5432)
        db.setDatabaseName("postgres")
        db.setHostName("localhost")
        db.open()
          # LoginMain.auth_login_cl
        self.db2 = psycopg2.connect(dbname= 'postgres', user = 'postgres', password = '12345678', host = 'localhost', port = 5432)
        self.cursor = self.db2.cursor()


    def add_defect(self):
        self.addDefect = Add_Defective(self.tableView_defective)
        self.addDefect.show()



if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =PrinterMain()
    window.show()
    app.exec()