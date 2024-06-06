import sys
import scores, reportWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PyQt5 import QtPrintSupport
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class Bank(scores.Scores):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # счета:
        self.tableView_score.clicked.connect(self.click_score)
        self.pushButton_score_dob.clicked.connect(self.score_dob_no_h)
        self.pushButton_score_edit.clicked.connect(self.score_edit_no_h)
        self.pushButton_score_dob_ok.clicked.connect(self.score_dob)
        self.pushButton_score_edit_ok.clicked.connect(self.score_edit)
        self.pushButton_score_delete.clicked.connect(self.score_delete)
        self.pushButton_score_dob_otmn.clicked.connect(self.score_dob_otmn)
        self.pushButton_score_edit_otmn.clicked.connect(self.score_edit_otmn)
        # операции по счету:
        self.tableView_operation.clicked.connect(self.click_operation)
        self.pushButton_operation_dob.clicked.connect(self.operation_dob_no_h)
        self.pushButton_operation_edit.clicked.connect(self.operation_edit_no_h)
        self.pushButton_operation_dob_otmn.clicked.connect(self.operation_dob_otmn)
        self.pushButton_operation_edit_otmn.clicked.connect(self.operation_edit_otmn)
        self.pushButton_operation_dob_ok.clicked.connect(self.operation_dob)
        self.pushButton_operation_edit_ok.clicked.connect(self.operation_edit)
        self.pushButton_operation_delete.clicked.connect(self.operation_delete)
        self.pushButton_all_operation.clicked.connect(self.all_operation)
        # перечень операций:
        # общие:
        self.pushButton_exit.clicked.connect(self.exit)
        self.pushButton_report.clicked.connect(self.report)
        
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setDatabaseName('postgres')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setUserName('postgres')
        db.setPassword('123456789')
        db.open()
        self.update_score()
        self.update_operation() 
        self.update_list_of_operations()

        # query = QSqlQuery()
        # query.exec_(f"SELECT DISTINCT account_number FROM public.score")
        # while query.next():
        #     value = str(query.value(0))
        #     if self.lineEdit_operation_dob_account_number.findText(value) == -1:
        #         self.lineEdit_operation_dob_account_number.addItem(value)

        # # selected_account_number = self.lineEdit_operation_dob_account_number.currentText()
        # # self.lineEdit_score_edit_account_number.setText(selected_account_number)

        # query2 = QSqlQuery()
        # query2.exec_(f"SELECT DISTINCT code_op FROM public.not_code")
        # while query2.next():
        #     value2 = str(query2.value(0))
        #     if self.lineEdit_operation_dob_operation_code.findText(value2) == -1:
        #         self.lineEdit_operation_dob_operation_code.addItem(value2)

    def score_dob_no_h(self):
        self.groupBox_score_dob.show()
        self.groupBox_score_edit.close()

    def score_edit_no_h(self):
        self.groupBox_score_edit.show()
        self.groupBox_score_dob.close()

    def operation_dob_no_h(self):
        query = QSqlQuery()
        query.exec_(f"SELECT DISTINCT account_number FROM public.score")
        while query.next():
            value = str(query.value(0))
            if self.lineEdit_operation_dob_account_number.findText(value) == -1:
                self.lineEdit_operation_dob_account_number.addItem(value)

        # selected_account_number = self.lineEdit_operation_dob_account_number.currentText()
        # self.lineEdit_score_edit_account_number.setText(selected_account_number)

        query2 = QSqlQuery()
        query2.exec_(f"SELECT DISTINCT code_op FROM public.not_code")
        while query2.next():
            value2 = str(query2.value(0))
            if self.lineEdit_operation_dob_operation_code.findText(value2) == -1:
                self.lineEdit_operation_dob_operation_code.addItem(value2)

        today = date.today()
        self.dateEdit_operation_dob_date.setDate(today)

        self.account_number = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 1))
        self.lineEdit_operation_dob_account_number.setCurrentText(self.account_number)
        self.operation_code = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 2))
        self.lineEdit_operation_dob_operation_code.setCurrentText(self.operation_code)

        self.groupBox_operation_dob.show()
        self.groupBox_operation_edit.close()

    def operation_edit_no_h(self):
        query = QSqlQuery()
        query.exec_(f"SELECT DISTINCT account_number FROM public.score")
        while query.next():
            value = str(query.value(0))
            if self.lineEdit_operation_edit_account_number.findText(value) == -1:
                self.lineEdit_operation_edit_account_number.addItem(value)

        query2 = QSqlQuery()
        query2.exec_(f"SELECT DISTINCT code_op FROM public.not_code")
        while query2.next():
            value2 = str(query2.value(0))
            if self.lineEdit_operation_edit_operation_code.findText(value2) == -1:
                self.lineEdit_operation_edit_operation_code.addItem(value2)

        self.account_number = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 1))
        self.lineEdit_operation_edit_account_number.setCurrentText(self.account_number)
        self.operation_code = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 2))
        self.lineEdit_operation_edit_operation_code.setCurrentText(self.operation_code)

        self.groupBox_operation_edit.show()
        self.groupBox_operation_dob.close()

    def score_dob_otmn(self):
        self.groupBox_score_dob.close()

    def score_edit_otmn(self):
        self.groupBox_score_edit.close()

    def operation_dob_otmn(self):
        self.groupBox_operation_dob.close()

    def operation_edit_otmn(self):
        self.groupBox_operation_edit.close()

    def update_score(self):
        t = QSqlTableModel()
        t.setTable('public.score')
        t.select()
        self.tableView_score.setModel(t)
        t.setHeaderData(1, Qt.Horizontal, "Номер счета")
        t.setHeaderData(2, Qt.Horizontal, "ФИО владельца")
        self.tableView_score.setColumnHidden(0, True)
        self.tableView_score.setColumnWidth(1, 200)
        self.tableView_score.setColumnWidth(2, 230)
        self.row_to_select = 0
        self.tableView_score.selectRow(self.row_to_select)

        self.score_account_number = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 1))
        self.lineEdit_score_edit_account_number.setText(self.score_account_number)
        self.fio = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 2))
        self.lineEdit_score_edit_fio.setText(self.fio)

        self.id_score = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 0))

    def update_operation(self):
        model = QSqlTableModel()
        model.setTable('public.account_transactions')
        model.setFilter(f"id_score = '{self.id_score}'")
        model.select()
        self.tableView_operation.setModel(model)
        model.setHeaderData(1, Qt.Horizontal, "Номер счета")
        model.setHeaderData(2, Qt.Horizontal, "Код операции")
        model.setHeaderData(3, Qt.Horizontal, "Дата")
        model.setHeaderData(4, Qt.Horizontal, "Сумма")
        self.tableView_operation.setColumnHidden(0, True)
        self.tableView_operation.setColumnWidth(1, 200)
        self.tableView_operation.setColumnWidth(2, 146)
        self.tableView_operation.setColumnWidth(3, 80) 
        self.tableView_operation.setColumnWidth(4, 100)
        self.tableView_operation.setColumnHidden(5, True)
        self.row_to_select2 = 0
        self.tableView_operation.selectRow(self.row_to_select2)

        self.operation_account_number = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 1))
        self.operation_code = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 2))
        self.datee = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 3))
        self.amount = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 4))
        self.operation_id_score = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 5))
        self.id_operation = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 0))
        # self.update_list_of_operations()

    def update_list_of_operations(self):
        t = QSqlTableModel()
        t.setTable('public.list_of_operations')
        t.setFilter(f"id_operation = '{self.id_operation}'")
        t.select()
        self.tableView_list_operation.setModel(t)
        t.setHeaderData(1, Qt.Horizontal, "Номер счета")
        t.setHeaderData(2, Qt.Horizontal, "Код операции")
        t.setHeaderData(3, Qt.Horizontal, "Операция")
        t.setHeaderData(4, Qt.Horizontal, "Процент")
        self.tableView_list_operation.setColumnHidden(0, True)
        self.tableView_list_operation.setColumnWidth(1, 200)
        self.tableView_list_operation.setColumnWidth(2, 140)
        self.tableView_list_operation.setColumnWidth(3, 230)
        self.tableView_list_operation.setColumnWidth(4, 100)
        self.tableView_list_operation.setColumnHidden(5, True)
        self.row_to_select3 = 0
        self.tableView_list_operation.selectRow(self.row_to_select3)

        self.id_list_operation = self.tableView_list_operation.model().data(self.tableView_list_operation.model().index(self.tableView_list_operation.currentIndex().row(), 0))

    def click_score(self, index):
        self.id_score = self.tableView_score.model().data(index.sibling(index.row(), 0))
        self.update_operation()
        self.update_list_of_operations()
        # счета:
        self.score_account_number = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 1))
        self.lineEdit_score_edit_account_number.setText(self.score_account_number)
        self.fio = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 2))
        self.lineEdit_score_edit_fio.setText(self.fio)
        # операции по счету:
        self.operation_account_number = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 1))
        self.operation_code = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 2))
        self.datee = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 3))
        self.amount = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 4))
        self.id_score = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 0))
        # self.operation_dob_no_h()
        try:
            self.lineEdit_operation_edit_account_number.itemText(self.operation_account_number)
            self.lineEdit_operation_edit_operation_code.itemText(self.operation_code)
            self.dateEdit_operation_edit_date.setDate(self.datee)
            self.lineEdit_operation_edit_amount.setText(self.amount)
        except TypeError:
            self.groupBox_operation_edit.close()

    def click_operation(self, index):
        self.id_operation = self.tableView_operation.model().data(index.sibling(index.row(), 0))
        self.update_list_of_operations()
        # операции по счету:
        self.operation_account_number = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 1))
        self.lineEdit_operation_edit_account_number.setCurrentText(self.operation_account_number)
        self.operation_code = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 2))
        self.lineEdit_operation_edit_operation_code.setCurrentText(self.operation_code) 
        self.datee = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 3))
        self.dateEdit_operation_edit_date.setDate(self.datee) 
        self.amount = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 4))
        self.lineEdit_operation_edit_amount.setText(str(self.amount)) 
        # операции:
        self.list_account_number = self.tableView_list_operation.model().data(self.tableView_list_operation.model().index(self.tableView_list_operation.currentIndex().row(), 1))
        self.list_operation_code = self.tableView_list_operation.model().data(self.tableView_list_operation.model().index(self.tableView_list_operation.currentIndex().row(), 2))
        self.operation = self.tableView_list_operation.model().data(self.tableView_list_operation.model().index(self.tableView_list_operation.currentIndex().row(), 3))
        self.percent = self.tableView_list_operation.model().data(self.tableView_list_operation.model().index(self.tableView_list_operation.currentIndex().row(), 4))
        try:
            self.lineEdit_operation_edit_account_number.itemText(self.operation_account_number)
            self.lineEdit_operation_edit_operation_code.itemText(self.operation_code)
            self.dateEdit_operation_edit_date.setDate(self.datee)
            self.lineEdit_operation_edit_amount.setText(self.amount)
        except TypeError:
            self.groupBox_operation_edit.close()

    def score_dob(self):
        account_number = self.lineEdit_score_dob_account_number.text()
        fio = self.lineEdit_score_dob_fio.text()
        check_query = QSqlQuery(f"SELECT COUNT(*) FROM public.score WHERE account_number = '{account_number}'")
        check_query.next()
        count = check_query.value(0)
        if count == 0:
            insert_query = QSqlQuery(f"INSERT INTO public.score (account_number, fio) VALUES ('{account_number}', '{fio}')")
            insert_query.exec()
            self.update_score()
            self.update_operation()
            # self.operation_dob_no_h()
            # self.operation_edit_no_h()
            self.lineEdit_score_dob_account_number.clear()
            self.lineEdit_score_dob_fio.clear()
            self.groupBox_score_dob.close()
        else:
            QMessageBox.warning(self, "Ошибка! Повторяющиеся значения!", "Такой номер счета уже существует.")
            self.lineEdit_score_dob_account_number.clear()
            self.lineEdit_score_dob_fio.clear()

        self.row_to_select = self.tableView_score.model().rowCount() - 1
        self.tableView_score.selectRow(self.row_to_select)
        self.id_score = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 0))

    def score_edit(self):
        q = f"UPDATE public.score set account_number = ('{self.lineEdit_score_edit_account_number.text()}'), fio = ('{self.lineEdit_score_edit_fio.text()}') where id = {self.id_score}"
        q2 = f"UPDATE public.account_transactions set account_number = ('{self.lineEdit_score_edit_account_number.text()}')"
        q3 = f"UPDATE public.account_transactions set id_score = ('{self.id_score}')"
        query = QSqlQuery(q)
        query2 = QSqlQuery(q2)
        query3 = QSqlQuery(q3)
        query.exec()
        query2.exec()
        query3.exec()
        self.update_score()
        self.update_operation()
        self.lineEdit_score_edit_account_number.clear()
        self.lineEdit_score_edit_fio.clear()

        # self.row_to_select = self.tableView_score.model().rowCount() - 1
        # self.tableView_score.selectRow(self.row_to_select)
        # self.id_score = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 0))
        # self.update_operation()

    def score_delete(self):
        selected_indexes = self.tableView_score.selectedIndexes()
        quest_score = 'Вы уверены, что хотите удалить данные?'
        quest_score2 = QMessageBox.question(self, 'Подтверждение удаления', quest_score, QMessageBox.Yes | QMessageBox.No)
        if quest_score2 == QMessageBox.Yes:
            if selected_indexes:
                self.id_score = self.tableView_score.model().data(self.tableView_score.model().index(self.tableView_score.currentIndex().row(), 0))
                # self.operation_account_number = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 1))
                self.id_score_operation = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 5))
                query = QSqlQueryModel()
                sql = f"DELETE FROM public.score WHERE id = '{self.id_score}'"
                sql2 = f"DELETE FROM public.account_transactions WHERE id_score = '{self.id_score_operation}'"
                query.setQuery(sql)
                query2 = QSqlQuery(f"SELECT COUNT(*) FROM public.account_transactions WHERE id_score = '{self.id_score_operation}'")
                query2.exec()
                if query2.next() and query2.value(0) > 0:
                    query.setQuery(sql2)
                self.update_score()
                self.update_operation()
                # self.update_operation()
                # self.operation_dob_no_h()
                # self.operation_edit_no_h()
            else:
                print("Вы допустили ошибку!")

    # def procent(self):
    #     amount = self.amount
    #     operation_code = self.operation_code
    #     query_procent = f"SELECT procent FROM public.not_code WHERE code_op = {operation_code}"
    #     procent_query = QSqlQuery(query_procent)
    #     procent_query.exec()
    #     print(procent_query.isActive())
    #     procent_query.next()
    #     if procent_query.isValid():
    #         procent = float(procent_query.value(0))
    #     else:
    #         procent = 0.0
    #     procent = float(procent)
    #     amount = float(amount)
    #     procent_itog = amount / 100 * procent
    #     self.amount_itog = amount - procent_itog

    def operation_dob(self):
        # Добавление операции:
        date = self.dateEdit_operation_dob_date.date().toString("yyyy-MM-dd")
        q = f"INSERT INTO public.account_transactions (account_number, operation_code, date, amount, id_score) VALUES ('{self.lineEdit_operation_dob_account_number.currentText()}', '{self.lineEdit_operation_dob_operation_code.currentText()}', '{date}', '{self.lineEdit_operation_dob_amount.text()}', '{self.id_score}')"
        query = QSqlQuery(QSqlDatabase.database())
        if query.exec(q):
            # self.update_score()
            print(query.isActive())
            self.update_operation()
            self.update_list_of_operations()
        else:
            print("Error executing the query:", query.lastError().text())

        # Добавление в перечень операций:
        operation_check = QSqlQuery(f"SELECT id FROM public.account_transactions WHERE account_number = '{self.lineEdit_operation_dob_account_number.currentText()}'")
        operation_check.next()
        operation = QSqlQuery(f"SELECT name FROM public.not_code WHERE code_op = '{self.lineEdit_operation_dob_operation_code.currentText()}'")
        operation.next()

        if operation.isValid():
            operation_code = operation.value(0)
            if operation_code != None:
                procent = QSqlQuery(f"SELECT procent FROM public.not_code WHERE code_op = '{self.lineEdit_operation_dob_operation_code.currentText()}'")
                procent.next()
                if procent.isValid():
                    procent_value = procent.value(0)
                    if procent_value != None:
                        q2 = f"INSERT INTO public.list_of_operations (account_number, code_operation, operation, procent, id_operation) SELECT '{self.lineEdit_operation_dob_account_number.currentText()}', '{self.lineEdit_operation_dob_operation_code.currentText()}', '{operation_code}', '{procent_value}', id FROM public.account_transactions WHERE account_number = '{self.lineEdit_operation_dob_account_number.currentText()}'"
                        query2 = QSqlQuery(QSqlDatabase.database())
                        if query2.exec(q2):
                            print(query2.isActive())

    def operation_edit(self):
        date = self.dateEdit_operation_edit_date.date().toString("yyyy-MM-dd")
        q = f"UPDATE public.account_transactions SET operation_code = '{self.lineEdit_operation_edit_operation_code.currentText()}', date = '{date}', amount = '{self.lineEdit_operation_edit_amount.text()}' WHERE id = {self.id_operation}"
        query = QSqlQuery(QSqlDatabase.database())
        if query.exec(q):
            # self.update_score()
            print(query.isActive())
            self.update_operation()
        else:
            print("Error executing the query:", query.lastError().text())

    def operation_delete(self):
        selected_indexes = self.tableView_operation.selectedIndexes()
        quest_operation = 'Вы уверены, что хотите удалить данные?'
        quest_operation2 = QMessageBox.question(self, 'Подтверждение удаления', quest_operation, QMessageBox.Yes | QMessageBox.No)
        if quest_operation2 == QMessageBox.Yes:
            if selected_indexes:
                self.id_operation = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 0))
                # лист операций будет - будут и строки:
                self.operation_account_number = self.tableView_operation.model().data(self.tableView_operation.model().index(self.tableView_operation.currentIndex().row(), 1))
                self.list_account_number = self.tableView_list_operation.model().data(self.tableView_list_operation.model().index(self.tableView_list_operation.currentIndex().row(), 1))
                query = QSqlQueryModel()
                sql = f"DELETE FROM public.account_transactions WHERE id = '{self.id_operation}'"
                sql2 = f"DELETE FROM public.list_of_operations WHERE id_operation = '{self.id_operation}'"
                query.setQuery(sql)
                query.setQuery(sql2)
                # query2 = QSqlQuery(f"SELECT COUNT(*) FROM public.account_transactions WHERE id_score = '{self.id_score_operation}'")
                # query2.exec()
                # if query2.next() and query2.value(0) > 0:
                #     query.setQuery(sql2)
                self.update_operation()
                self.update_list_of_operations()
                # self. дописать!!!
                # self.operation_dob_no_h()
                # self.operation_edit_no_h()
            else:
                print("Вы допустили ошибку!")

    def all_operation(self):
        query2 = QSqlQueryModel()
        sql2 = "SELECT * FROM public.account_transactions"
        query2.setQuery(sql2)
        self.tableView_operation.setModel(query2) 
        query2.setHeaderData(1, Qt.Horizontal, "Номер счета")
        query2.setHeaderData(2, Qt.Horizontal, "Код операции")
        query2.setHeaderData(3, Qt.Horizontal, "Дата")
        query2.setHeaderData(4, Qt.Horizontal, "Сумма") 
        self.tableView_operation.setColumnHidden(0, True)
        self.tableView_operation.setColumnWidth(1, 200)
        self.tableView_operation.setColumnWidth(2, 146)
        self.tableView_operation.setColumnWidth(3, 80) 
        self.tableView_operation.setColumnWidth(4, 100)
        self.tableView_operation.setColumnHidden(5, True)

    def report(self): 
        self.report2 = Print()
        self.report2.show()
        self.close()

    def exit(self):
        self.close()

class Print(reportWindow.Report):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_exit.clicked.connect(self.exit2)
        self.calendarWidget.clicked.connect(self.start_data)
        self.calendarWidget_2.clicked.connect(self.end_data)
        self.pushButton_ready.clicked.connect(self.ok)
        self.pushButton_print.clicked.connect(self.print_ok)

        # self.TextEdit = QTextEdit()
        # self.TextDocument = QTextDocument()
        # self.click1 = 0
        # self.click2 = 0
        self.update_report()

    def start_data(self):
        self.data = self.calendarWidget.selectedDate()
        self.a = self.data.toString("yyyy-MM-dd")
        print(self.a)

    def end_data(self):
        self.data2 = self.calendarWidget_2.selectedDate()
        self.b = self.data2.toString("yyyy-MM-dd")
        print(self.b) 

    def ok(self):
        try:   
            self.update_report2()
        except AttributeError:
            print('Необходимо выбрать дату!')

    def update_report(self):
        # sql = f"SELECT public.score.account_number, public.score.fio, public.account_transactions.operation_code, public.account_transactions.date, public.account_transactions.amount, public.list_of_operations.operation, public.list_of_operations.procent FROM public.score, public.account_transactions, public.list_of_operations"
        # INNER JOIN public.invoice ON public.goodsininvoice.id_invoice = public.invoice.number INNER JOIN public.provider ON public.provider.id = public.invoice.id_provider INNER JOIN public.goods ON public.goods.id = public.goodsininvoice.id_goods
        # sql = "SELECT * FROM public.list_of_operations"
        query = QSqlQueryModel()
        sql = "SELECT public.list_of_operations.*, public.account_transactions.date, public.account_transactions.amount " +\
            "FROM public.list_of_operations " +\
            "JOIN public.account_transactions ON public.list_of_operations.id_operation = public.account_transactions.id"
        query.setQuery(sql)
        self.tableView.setModel(query)
        query.setHeaderData(0, Qt.Horizontal, "ID")
        query.setHeaderData(1, Qt.Horizontal, "Номер счета")
        query.setHeaderData(2, Qt.Horizontal, "Код операции")
        query.setHeaderData(3, Qt.Horizontal, "Операция")
        query.setHeaderData(4, Qt.Horizontal, "Процент")
        # query.setHeaderData(5, Qt.Horizontal, "Операция")
        query.setHeaderData(6, Qt.Horizontal, "Дата")
        query.setHeaderData(7, Qt.Horizontal, "Сумма")
        self.tableView.setColumnWidth(0, 60)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 140)
        self.tableView.setColumnWidth(3, 240)
        self.tableView.setColumnWidth(4, 100)
        self.tableView.setColumnHidden(5, True)
        self.tableView.setColumnWidth(6, 100)
        self.tableView.setColumnWidth(7, 130)

    def update_report2(self):
        query = QSqlQueryModel()
        sql = "SELECT public.list_of_operations.*, public.account_transactions.date, public.account_transactions.amount " +\
            "FROM public.list_of_operations " +\
            "JOIN public.account_transactions ON public.list_of_operations.id_operation = public.account_transactions.id " +\
            f"WHERE public.account_transactions.date BETWEEN '{self.a}' AND '{self.b}'"
        query.setQuery(sql)
        self.tableView.setModel(query)

    def print_ok(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            printer = dialog.printer()
            text_doc = QtGui.QTextDocument()
            html = self.build_document()
            text_doc.setHtml(html)
            text_doc.print(printer)

    def build_document(self):
        query = QSqlQueryModel()
        sql = "SELECT public.list_of_operations.*, public.account_transactions.date, public.account_transactions.amount " +\
            "FROM public.list_of_operations " +\
            "JOIN public.account_transactions ON public.list_of_operations.id_operation = public.account_transactions.id " 
            # f"WHERE public.account_transactions.date BETWEEN '{self.a}' AND '{self.b}'"
        query.setQuery(sql)
        
        c = canvas.Canvas('output.pdf')
        c.setFont("Helvetica", 7) 
        y = 750

        for row in range(query.rowCount()):
            id = query.record(row).value('id')
            account_number = query.record(row).value("account_number")
            code_operation = query.record(row).value('code_operation')
            operation = query.record(row).value('operation')
            procent = query.record(row).value('procent')
            # formatted_date = query.data().toString("yyyy-MM-dd")
            amount = query.record(row).value('amount')

            c.drawString(20, y, f"ID: {id} Номер счета: {account_number} Код операции: {code_operation} Операция: {operation} Процент: {procent} Сумма: {amount}") 
            y -= 20

        c.save()

    # def print_ok(self):
    #     dialog = QtPrintSupport.QPrintDialog()
    #     if dialog.exec_() == QtWidgets.QDialog.Accepted:
    #         printer = dialog.printer()
    #         text_doc = QtGui.QTextDocument()
    #         html = self.build_document()
    #         text_doc.setHtml(html)
    #         text_doc.print(printer)

    # def build_document(self):
    #     query = QSqlQueryModel()
    #     sql = "SELECT public.list_of_operations.*, public.account_transactions.date, public.account_transactions.amount " +\
    #         "FROM public.list_of_operations " +\
    #         "JOIN public.account_transactions ON public.list_of_operations.id_operation = public.account_transactions.id " +\
    #         "WHERE public.account_transactions.date BETWEEN '{self.a}' AND '{self.b}'"
    #     query.setQuery(sql)
        
    #     for row in range(query.rowCount()):
    #         id = query.record(row).value('id')
    #         account_number = query.record(row).value("account_number")
    #         code_operation = query.record(row).value('code_operation')
    #         operation = query.record(row).value('operation')
    #         procent = query.record(row).value('procent')
    #         formatted_date = date.toString("yyyy-MM-dd")
    #         amount = query.record(row).value('amount')

    #         c = canvas.Canvas('output.pdf')
    #         c.setFont("DejaVu", 12) 
    #         c.drawString(100, 750, f"ID: {id} Номер счета: {account_number} Код операции: {code_operation} Операция: {operation} Процент: {procent}  Дата: {formatted_date} Сумма: {amount}") 
    #         c.save()

    def exit2(self):
        self.close()

app = QApplication(sys.argv)
window = ()
window.show()
app.exec()  