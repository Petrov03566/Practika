import sys 
from Defective import Defectiveadd
from Working import Workingadd
from Refilled import Refilledadd
from Onclade import Oncladeadd
from PyQt5 import QtCore 
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication,QHeaderView
from PyQt5.QtCore import *
import MainWindow 

#  ##  #########################################ГЛАВНОЕ ОКНО ################################################
class PrinterMain(MainWindow.MainPrinter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        self.current_def = 0
        self.current_ref =0
        self.current_work = 0
        
        
        self.pb_add_defective.clicked.connect(self.add_Defective_button)
        self.pb_add_working.clicked.connect(self.add_Working_Button)
        self.pb_add_refueled.clicked.connect(self.add_Refilled_button)
        self.pushButton_add_on_clade.clicked.connect(self.add_Onclade_button)    
        self.tableView_working.clicked.connect(self.work_clicked)
        self.tableView_defective.clicked.connect(self.dp_clicked)
        self.tableView_defective.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_working.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_refueled.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        

        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("12345678") 
        db.setPort(5432)
        db.setDatabaseName("postgres")
        db.setHostName("localhost")
        db.open()

        self.update_def()
        self.update_work()
        self.update_ref()
   
        query = QSqlTableModel()
        sql = "SELECT * FROM public.Defective "
        query.setTable("Defective")
        query.select()
        query.removeColumn(0)
        self.tableView_defective.setModel(query)
        self.current_def=self.tableView_defective.model().index(0,0).data()
        query.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query.setHeaderData(1, QtCore.Qt.Horizontal,"ломка")
        query.setHeaderData(2, QtCore.Qt.Horizontal,"недостаток")
    
    
        query2 = QSqlTableModel()
        sql = "SELECT * FROM public.Refilled"
        query2.setTable("Refilled")
        query2.select()
        query2.removeColumn(0)
        self.tableView_refueled.setModel(query2)
        query2.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query2.setHeaderData(1, QtCore.Qt.Horizontal,"Диагностика")
        query2.setHeaderData(2, QtCore.Qt.Horizontal,"очистка")
        query2.setHeaderData(3, QtCore.Qt.Horizontal,"Тестирование устройство")
        query2.setHeaderData(4, QtCore.Qt.Horizontal,"необходимый")
        
       
    
        query3 = QSqlTableModel()
        sql = "SELECT * FROM public.Working"
        query3.setTable("Working")
        query3.select()
        query3.removeColumn(0)
        self.tableView_working.setModel(query3)
        self.current_def =self.tableView_working.model().index(0,0).data()
        query3.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query3.setHeaderData(1, QtCore.Qt.Horizontal,"место установление")

 
        query4 = QSqlTableModel()
        sql = "SELECT * FROM public.On_clade"
        query4.setTable("On_clade")
        query4.select()
        query4.removeColumn(0)
        self.tableView_on_clade.setModel(query4)
        query4.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query4.setHeaderData(1, QtCore.Qt.Horizontal,"серийный номер")
        query4.setHeaderData(2, QtCore.Qt.Horizontal,"порт номера ")
        
        
#####################################################Кнопка добавление ##############################
    def add_Defective_button(self):
        self.add_dt = Defectiveadd(self.update_def)
        self.add_dt.show()

    def add_Working_Button(self):
        self.add_w = Workingadd(self.current_def,self.update_work)
        self.add_w.show()

    def add_Refilled_button(self):
        self.add_rd =Refilledadd(self.current_work,self.update_ref)
        self.add_rd.show()

    def add_Onclade_button(self):
        self.add_clade =Oncladeadd(self.current_ref,self.update_Onclade)
        
    
    def dp_clicked(self):
        row = self.tableView_defective.selectedIndexes()[0].row()
        self.current_dep = self.tableView_defective.model().index(row, 0).data()

    def work_clicked(self):
        row = self.tableView_working.selectedIndexes()[0].row()
        self.current_ward = self.tableView_working.model().index(row, 0).data()

    def rd_clicked(self):
        row = self.tableView_refueled.selectedIndexes()[0].row()
        self.current_ward = self.tableView_refueled.model().index(row, 0).data()

    def update_def(self):
        query = QSqlTableModel()
        query.setTable("Defective")
        query.select()
        self.tableView_defective.setModel(query)
    
    def update_work(self):
        query2 = QSqlTableModel()
        query2.setTable("Working")
        query2.select()
        self.tableView_working.setModel(query2)

    def update_ref(self):
        query3 = QSqlTableModel()
        query3.setTable("Refilled")
        query3.select()
        self.tableView_working.setModel(query3)
        
    def update_Onclade(self):
        query4 = QSqlTableModel()
        query4.setTable("On_clade")
        query4.select()
        self.tableView_working.setModel(query4)



if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =PrinterMain()
    window.show()
    app.exec_()