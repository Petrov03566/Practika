import add_Working
from PyQt5 import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class Workingadd(add_Working.Ui_Form):
    def __init__(self,def_id,update_work):
        super().__init__()
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
            query_wk.exec(f"INSERT INTO publc.Working (name_printer3,place_establishment) VALUES  ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}')")
            self.update_work()
