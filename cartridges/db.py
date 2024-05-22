from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import Qt



def connect():
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setDatabaseName("postgres")
        db.setUserName("postgres")
        db.setPassword("12345678")
        db.setPort(5432)
        db.setHostName("localhost")
        db.open()


# def get_models():
#         model = QSqlQueryModel()
#         model.setQuery(f"SELECT * FROM public.Defective(id,name_printer,breaking,flaw) VALUES ('{}',")



       



        



        


 
