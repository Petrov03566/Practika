import add_On_clade
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel,QSqlQueryModel
from PyQt5.QtWidgets import  QApplication,QHeaderView,QMainWindow,QWidget

class Onclade(add_On_clade.Ui_Form):
    def __init__(self,onclade_id,update_onclade,parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.onclade =onclade_id
        self.update_onclade =update_onclade
        self.pushButton_add_onclade.clicked.connect(self.add_onclade)
        self.pushButton_exit_onclade.clicked.connect(self.close_onclade)

    def close_onclade(self):
        self.close()
    def add_onclade(self):
        if self.lineEdit_nameprinter4.text() and self.lineEdit_serial_number.text() and self.lineEdit_port_number.text():
            query_oe =QSqlQuery()
            query_oe.exec(f"INSERT INTO public.On_clade(name_printer4,serial_number,port_number) VALUES ('{self.lineEdit_nameprinter4.text()}','{self.lineEdit_serial_number.text()}','{self.lineEdit_port_number.text()}')")
            self.update_onclade()
            
