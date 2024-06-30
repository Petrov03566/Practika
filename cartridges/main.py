import sys
from Working1 import Working
from Defect import Defective
from Refilled1 import Refilled
from onclade import Onclade
from PyQt5 import QtCore 
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel,QSqlQueryModel
from PyQt5.QtWidgets import  QApplication,QHeaderView,QMainWindow,QWidget
from PyQt5.QtCore import Qt
from MainWindow import MainPrinter

#  ##  #########################################ГЛАВНОЕ ОКНО ################################################
class PrinterMain(MainPrinter):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        mainwindow =QMainWindow(None)

        self.current_def = 0 
        self.current_ref =0
        self.current_work = 0
        self.current_onclade = 0
        
        self.pb_add_defective.clicked.connect(self.add_Defective_button)
        self.pb_add_working.clicked.connect(self.add_Working_Button)
        self.pb_add_refueled.clicked.connect(self.add_Refilled_button)
        self.pb_delete_defective.clicked.connect(self.delete_defective)
        self.pushButton_delete_working.clicked.connect(self.delete_working)
        self.pb_delete_refueled.clicked.connect(self.delete_refilled)
        self.pushButton_add_on_clade.clicked.connect(self.add_Onclade_button)
        self.tableView_working.clicked.connect(self.work_clicked)
        self.tableView_defective.clicked.connect(self.dp_clicked)
        self.tableView_on_clade.clicked.connect(self.oe_clicked)
        
        self.tableView_defective.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_working.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_refueled.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_defective.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        

        db = QSqlDatabase.addDatabase("QPSQL")
        db.setUserName("postgres")
        db.setPassword("Doctor") 
        db.setPort(5432)
        db.setDatabaseName("Cartridges")
        db.setHostName("localhost")
        db.open()
        if db.open():
            print("Database connection established")
        else:
            print("Failed to connect to the database")

        self.update_def()
        self.update_work()
        self.update_ref
        self.update_Onclade()
        
        self.table()
        self.tavle2()
        self.tavle3()
        self.table_4()

    def table(self):
        query = QSqlTableModel()
        sql = "SELECT * FROM public.Defective"
        query.setTable("Defective")
        query.select()
        query.removeColumn(0)
        self.tableView_defective.setModel(query)
        self.current_def=self.tableView_defective.model().index(0,0).data()
        query.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query.setHeaderData(1, QtCore.Qt.Horizontal,"ломка")
        query.setHeaderData(2, QtCore.Qt.Horizontal,"недостаток")
    
    def tavle2(self):
        query2 = QSqlTableModel()
        sql = "SELECT * FROM public.Refilled"
        query2.setTable("Refilled")
        query2.select()
        query2.removeColumn(0)
        self.tableView_refueled.setModel(query2)
        self.current_ref = self.tableView_refueled.model().index(0,0).data()
        query2.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query2.setHeaderData(1, QtCore.Qt.Horizontal,"Диагностика")
        query2.setHeaderData(2, QtCore.Qt.Horizontal,"очистка")
        query2.setHeaderData(3, QtCore.Qt.Horizontal,"Тестирование устройство")
        query2.setHeaderData(4, QtCore.Qt.Horizontal,"необходимый")
        
       
    def tavle3(self):
        query3 = QSqlTableModel()
        sql = "SELECT * FROM public.Working"
        query3.setTable("Working")
        query3.select()
        query3.removeColumn(0)
        self.tableView_working.setModel(query3)
        self.current_work =self.tableView_working.model().index(0,0).data()
        query3.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query3.setHeaderData(1, QtCore.Qt.Horizontal,"место установление")

    def table_4(self):
        query4 = QSqlTableModel()
        sql = "SELECT * FROM public.On_clade"
        query4.setTable("On_clade")
        query4.select()
        query4.removeColumn(0)
        self.tableView_on_clade.setModel(query4)
        self.current_work =self.tableView_on_clade.model().index(0,0).data
        query4.setHeaderData(0, QtCore.Qt.Horizontal,"Имя принтера")
        query4.setHeaderData(1, QtCore.Qt.Horizontal,"серийный номер")
        query4.setHeaderData(2, QtCore.Qt.Horizontal,"порт номера ")
        
        
#####################################################Кнопка добавление ##############################
    def add_Defective_button(self):      
        self.add_dt = Defective(self.update_def)  
        self.add_dt.show() # Pass self as parent
    
    def delete_defective(self):
            query_del = QSqlTableModel()
            query_del.setTable("Defective")
            query_del.select()
            selected = self.tableView_defective.selectedIndexes()

            rows = set(index.row() for index in selected)
            rows = list(rows)
            rows.sort()
            if selected:
                first = rows[0]
                query_del.removeRow(first)
                query_del.select()

            query = QSqlTableModel()
            query.setTable("Defective")
            query.select()
            self.tableView_defective.setModel(query)
            self.tableView_defective.setColumnHidden(0,True)

        
    def add_Working_Button(self):
        self.add_w = Working(self.current_def, self.update_work)
        self.add_w.show()

    def delete_working(self):
            query_work = QSqlTableModel()
            query_work.setTable("Working")
            query_work.select()
            selected = self.tableView_working.selectedIndexes()

            rows = set(index.row() for index in selected)
            rows = list(rows)
            rows.sort()
            if selected:
                first = rows[0]
                query_work.removeRow(first)
                query_work.select()
                
            query_work = QSqlTableModel()
            query_work.setTable("Defective")
            query_work.select()
            self.tableView_working.setModel(query_work)
            self.tableView_working.setColumnHidden(0,True)



    def add_Refilled_button(self):
        self.add_rd =Refilled(self.current_work,self.update_ref)
        self.add_rd.show()

    def delete_refilled(self):
            query_ref = QSqlTableModel()
            query_ref.setTable("Refilled")
            query_ref.select()
            selected = self.tableView_refueled.selectedIndexes()

            rows = set(index.row() for index in selected)
            rows = list(rows)
            rows.sort()
            if selected:
                first = rows[0]
                query_ref.removeRow(first)
                query_ref.select()
            
            
            query_ref = QSqlTableModel()
            query_ref.setTable("Defective")
            query_ref.select()
            self.tableView_refueled.setModel(query_ref)
            self.tableView_refueled.setColumnHidden(0,True)



    def add_Onclade_button(self):
        self.add_oe = Onclade(self.current_def,self.update_Onclade)
        self.add_oe.show()

    
    
        
    def dp_clicked(self):
        row = self.tableView_defective.selectedIndexes()[0].row()
        self.current_dep = self.tableView_defective.model().index(row, 0).data()

    def work_clicked(self):
        row = self.tableView_working.selectedIndexes()[0].row()
        self.current_ward = self.tableView_working.model().index(row, 0).data()

    def rd_clicked(self):
        row = self.tableView_refueled.selectedIndexes()[0].row()
        self.current_ward = self.tableView_refueled.model().index(row, 0).data()
    def oe_clicked(self):
        row = self.tableView_on_clade.selectedIndexes()[0].row()
        self.current_ward = self.tableView_on_clade.model().index(row, 0).data()

# ###############################Обновление данных ###############################
    def update_def(self):
        query = QSqlTableModel()
        query.setTable("Defective")
        query.select()
        self.tableView_defective.hideColumn(0)
        self.tableView_defective.setModel(query)
        
    
    def update_work(self):
        query2 = QSqlTableModel()
        query2.setTable("Working")
        query2.select()
        self.tableView_working.hideColumn(0)
        self.tableView_working.setModel(query2)
   
    def update_ref(self):
        query3 = QSqlTableModel()
        query3.setTable("Refilled")
        query3.select()
        self.tableView_refueled.hideColumn(0)
        self.tableView_refueled.setModel(query3)
        
    def update_Onclade(self):
        query4 = QSqlTableModel()
        query4.setTable("On_clade")
        query4.select()
        self.tableView_on_clade.hideColumn(0)
        self.tableView_on_clade.setModel(query4)
    
            
if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =PrinterMain()
    window.show()
    sys.exit(app.exec_())