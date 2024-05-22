import sys
from add_defective import Add_Defective
from delete_defective import Delete_Defective
from PyQt5.QtWidgets import *
from main import PrinterMain
class DefectiveMain(PrinterMain):
    def __init__(self):
        super().__init__()
        self.setupUi()

       

 #Окно добавление данных 
    def add_defect_button(self):
        self.defect = Add_Defective(self.tableView_defective)
        self.defect.show()
    

    def del_defective(self):
        self.defect2 =Delete_Defective(tableView_defective =self.tableView_defective)
        self.close()

        
        


        
