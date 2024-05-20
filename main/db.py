from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
class Database():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setDatabaseName("postgres")
        self.db.setUserName("postgres")
        self.db.setPassword("12345678")
        self.db.setPort(5432)
        self.db.setHostName("localhost")
        self.query = QSqlQuery()
        self.db.open()

        



        


 
