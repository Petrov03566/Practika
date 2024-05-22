import sys 
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from MainWindow import MainPrinter
from auth import Ui_MainWindow
from Defective import Add_Defective,Delete_Defective

#  ##  #########################################ГЛАВНОЕ ОКНО ################################################
class PrinterMain(MainPrinter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


      
    

if __name__ == '__main__':
    app =QApplication(sys.argv)
    window =PrinterMain()
    window.show()
    app.exec()