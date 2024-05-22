from auth import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import *

from MainWindow import MainPrinter

import sys

class Avtoriza (Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label = QLabel("Welcome to the Avtoriza!", self)
        

        self.pb_auth.clicked.connect(self.add_auth)
        self.pb_exit.clicked.connect(self.cansel_exit)

    def add_auth(self):
        if self.lineEdit_log.text() == 'admin' and self.lineEdit_psw.text() == '1234':
            self.main_printer = MainPrinter() 
            self.main_printer.show()  

    def cansel_exit(self):
        self.close()


app = QApplication(sys.argv)
window = Avtoriza()
window.show()
sys.exit(app.exec_())