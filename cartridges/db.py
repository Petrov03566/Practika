from PyQt5.QtSql import *



def connect():
        db = QSqlDatabase.addDatabase("QPSQL")
        db.setDatabaseName("postgres")
        db.setUserName("postgres")
        db.setPassword("12345678")
        db.setPort(5432)
        db.setHostName("localhost")
        db.open()


