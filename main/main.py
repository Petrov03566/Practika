import sys 
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from MainWindow import MainPrinter
from auth import Ui_MainWindow
from add_defective import Add_Defective
from delete_defective import Delete_Defective

class PrinterMain(MainPrinter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb_add_defective.clicked.connect(self.add_defect_button)
        self.pb_delete_defective.clicked.connect(self.del_defective)
    
    # Открытия добавление данных 
    def add_defect_button(self):
        self.defect = Add_Defective(self.tableView_defective)
        self.defect.show()
    
    def del_defective(self):
        self.delete_defective = Delete_Defective()
        self.delete_defective.setupUi(self.delete_defective)
        self.delete_defective.show()
        
        

if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =PrinterMain()
    window.show()
    app.exec()


