from PyQt5 import QtWidgets,QtSql
import os
class Data:
    def __init__(self):
        super(Data,self).__init__()
        self.connection()

    def connection(self):
        path=os.path.dirname(os.path.abspath(__file__))
        db=QtSql.QSqlDatabase.addDatabase('QSQLITE') #Установка соединения с базой данных SQLITE3
        db.setDatabaseName(path+r'\orders_db.db') #Определение имени базе данных
        if not db.open(): #Если база данных не найдена, то открывается диалоговое окно
            QtWidgets.QMessageBox.critical(None, "Не удаётся открыть базу данных ", "Система не смогла найти файл базы данных", QtWidgets.QMessageBox.Ok)
            return False
        
        query = QtSql.QSqlQuery() #Экземпляр для создания SQL-запросов
        query.exec('''CREATE TABLE IF NOT EXISTS orders (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   client TEXT NOT NULL,
                   device TEXT NOT NULL,
                   service TEXT NOT NULL,
                   status TEXT NOT NULL,
                   price INTEGER,
                   date TEXT NOT NULL,
                   number INTEGER,
                   master TEXT NOT NULL,
                   comment TEXT NOT NULL)
                   ''')
        return True

    def create_query(self, sql_query, sql_query_values=None):#Метод для обработки SQL-запросов 
        query=QtSql.QSqlQuery()
        query.prepare(sql_query)
        if sql_query_values is not None:
            for query_value in sql_query_values:
                query.addBindValue(query_value)

        
        query.exec()
        return query

    def add_new_order(self, client, device, service, status, price, date, phone_number, master, comment):#Метод для добавления заказов в базу данных
        order_query="INSERT INTO orders (client, device, service, status, price, date, number, master, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.create_query(order_query,[client,device,service,status,price,date,phone_number,master, comment])

    def edit_order(self, client, device, service, status, price, date, phone_number, master, comment, id):#Метод для редактирования записи
        edit_query="UPDATE orders SET client=?, device=?, service=?, status=?, price=?, date=?, number=?, master=?, comment=? WHERE id=?"
        self.create_query(edit_query,[client,device,service,status,price,date,phone_number,master,comment,id])

    def delete_order(self, id):#Метод для удаления заказа 
        delete_query="DELETE FROM orders WHERE id=?"
        self.create_query(delete_query,[id])
    
    def get_change(self,id):#Метод получения значений из выбранной строки
        get_query="SELECT client, device, service, status, price, date, number, master, comment FROM orders WHERE id=?"
        result=self.create_query(get_query,[id])
        elements=[]
        if result.next():
            for i in range(9):
                elements.append(result.value(i))
        return elements
            



    