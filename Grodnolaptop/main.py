import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QHeaderView, QTableView
from PyQt5.QtSql import QSqlTableModel
from Base_Window import Ui_MainWindow
from splashcreen import GIF_Window
from  PyQt5.QtCore import Qt, QSortFilterProxyModel, QDate
from PyQt5.QtWinExtras import QtWin
from DB_connection import Data
from Dialog_Window import Ui_Dialog
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
import pandas as pd
from win32com.shell import shell, shellcon
import os




class CustomFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.filters = {
            'client': "",
            'device': "",
            'service': "",
            'status': "",
            'price': "",
            'phone': "",
            'master': ""
        }

    def set_filter(self, column, value):#Метод для установки фильтра по столбцу
        self.filters[column] = value

    def filterAcceptsRow(self, source_row, source_parent):
        model = self.sourceModel()

        #Проверка каждого столбца по соответствующему фильтру
        client_index = model.index(source_row, 1, source_parent)  # Столбец 1: клиент
        device_index = model.index(source_row, 2, source_parent)  # Столбец 2: устройство
        service_index = model.index(source_row, 3, source_parent)  # Столбец 3: услуга
        status_index = model.index(source_row, 4, source_parent)  # Столбец 4: статус
        price_index = model.index(source_row, 5, source_parent)  # Столбец 5: цена
        phone_index = model.index(source_row, 7, source_parent)  # Столбец 7: телефон
        master_index = model.index(source_row, 8, source_parent)  # Столбец 8: мастер

        #Получение значения из каждой ячейки
        client = model.data(client_index, Qt.DisplayRole)
        device = model.data(device_index, Qt.DisplayRole)
        service = model.data(service_index, Qt.DisplayRole)
        status = model.data(status_index, Qt.DisplayRole)
        price = model.data(price_index, Qt.DisplayRole)
        phone = model.data(phone_index, Qt.DisplayRole)
        master = model.data(master_index, Qt.DisplayRole)

        phone = str(phone)#Перевод в строкое значение номер телефона
        price = str(price)#Перевод в строкое значение цены
        #Проверка фильтров для каждого столбца
        if self.filters['client'].lower() not in client.lower():
            return False
        if self.filters['device'].lower() not in device.lower():
            return False
        if self.filters['service'].lower() not in service.lower():
            return False
        if self.filters['status'].lower() not in status.lower():
            return False
        if self.filters['price'].lower() not in price.lower():
            return False
        if self.filters['phone'].lower() not in phone.lower():
            return False
        if self.filters['master'].lower() not in master.lower():
            return False

        return True

class CenteredSqlTableModel(QSqlTableModel): #Подкласс класса QsqlTableModel для выравнивания элементов по центру
    def data(self, index, role):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter  # Выравниваем данные по центру
        return super().data(index, role)

class GrodnoLaptop(QMainWindow):
    def __init__(self):
        super(GrodnoLaptop,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.con = Data()   #Экземпляр класс Data из файла DB_connection
        self.view_table()


        #Загрузка шрифтов
        path=os.path.dirname(os.path.abspath(__file__))
        QFontDatabase.addApplicationFont(path+"\\fonts\\Inter-Medium.otf")
        QFontDatabase.addApplicationFont(path+"\\fonts\\Jost-SemiBold.ttf")
        QFontDatabase.addApplicationFont(path+"\\fonts\\Roboto.ttf")


        #Подключение кнопок к методам
        self.ui.order_btn.clicked.connect(self.new_order_window)
        self.ui.edit_btn.clicked.connect(self.new_order_window)
        self.ui.del_btn.clicked.connect(self.delete_selected_order)
        self.ui.search_Button.clicked.connect(self.apply_filter)
        self.ui.clear_Button.clicked.connect(self.delete_filter)
        self.ui.help_btn.clicked.connect(self.open_manual)
        self.desktop_path = shell.SHGetKnownFolderPath(shellcon.FOLDERID_Desktop)
        self.ui.export_btn.clicked.connect(lambda: self.export_to_excel_with_pandas(self.ui.tableView, f"{self.desktop_path}\\Данные.xlsx"))

    def view_table(self):
        self.model=CenteredSqlTableModel(self)
        self.model.setTable('orders')
        self.model.setHeaderData(0, Qt.Horizontal, "Номер")
        self.model.setHeaderData(1, Qt.Horizontal, "Клиент")
        self.model.setHeaderData(2, Qt.Horizontal, "Устройство")
        self.model.setHeaderData(3, Qt.Horizontal, "Услуга")
        self.model.setHeaderData(4, Qt.Horizontal, "Статус")
        self.model.setHeaderData(5, Qt.Horizontal, "Цена")
        self.model.setHeaderData(6, Qt.Horizontal, "Дата")
        self.model.setHeaderData(7, Qt.Horizontal, "Телефон")
        self.model.setHeaderData(8, Qt.Horizontal, "Мастер")
        self.model.setHeaderData(9, Qt.Horizontal, "Комментарий")
        self.model.select()
        self.proxy_model=CustomFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.ui.tableView.setModel(self.proxy_model)
        self.ui.tableView.resizeRowsToContents()
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #Динамическое изменение размеров столбцов
        self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents) #Динамическое изменение размеров строк
        self.ui.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.ui.tableView.resizeRowsToContents()
        self.ui.tableView.setWordWrap(True)


    def apply_filter(self):#Применение фильтра
        self.proxy_model.set_filter('client', self.ui.client_lineEdit.text())
        self.proxy_model.set_filter('device', self.ui.device_lineEdit.text())
        self.proxy_model.set_filter('service', self.ui.service_lineEdit.text())
        self.proxy_model.set_filter('price', self.ui.price_lineEdit.text())
        self.proxy_model.set_filter('status', self.ui.status_comboBox.currentText() )
        self.proxy_model.set_filter('phone', self.ui.phonenumber_lineEdit.text())
        self.proxy_model.set_filter('master', self.ui.master_comboBox.currentText())

        #Пересчитываем фильтрацию
        self.proxy_model.invalidateFilter()


    def delete_filter(self): #Очистка фильтра
        self.ui.client_lineEdit.clear()
        self.ui.device_lineEdit.clear()
        self.ui.service_lineEdit.clear()
        self.ui.price_lineEdit.clear()
        self.ui.phonenumber_lineEdit.clear()
        self.ui.status_comboBox.setCurrentIndex(-1)
        self.ui.master_comboBox.setCurrentIndex(-1)
        self.proxy_model.setFilterRegExp("")
        self.proxy_model.setFilterKeyColumn(-1)

        self.filters = {
        'client': '',
        'device': '',
        'service': '',
        'status': '',
        'price': '',
        'phone': '',
        'master': ''
    }
        self.view_table()
    
    
    def new_order_window(self):
        self.new_window = QDialog()
        self.ui_window=Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        
        sender=self.sender() #Сохранение сигнала последней нажатой кнопки
        if sender.text() == "Заказ": #Открытие меню добавления заказа
            self.ui_window.add_Button.clicked.connect(self.add_order)
            self.new_window.show()
        else: #Открытие меню редактирования заказа
            self.ui_window.add_Button.clicked.connect(self.edit_selected_order)
            elems=[]
            elems.append(self.con.get_change(id=self.index()))
            try:
                el1=elems[0][0]
                el2=elems[0][1]
                el3=elems[0][2]
                el4=elems[0][3]
                el5=elems[0][4]
                el6=elems[0][5]
                el7=elems[0][6]
                el8=elems[0][7]
                el9=elems[0][8]
                self.ui_window.client_lineEdit.setText(str(el1))
                self.ui_window.device_lineEdit.setText(str(el2))
                self.ui_window.service_lineEdit.setText(str(el3))
                if el4=="Активен":
                    self.ui_window.status_comboBox.setCurrentIndex(0)
                else:
                    self.ui_window.status_comboBox.setCurrentIndex(1)
                self.ui_window.price_lineEdit.setText(str(el5))
                self.ui_window.dateEdit.setDate(QDate.fromString(el6,"dd.MM.yyyy"))
                self.ui_window.phone_lineEdit.setText(str(el7))
                if el8=="Константин":
                    self.ui_window.master_comboBox.setCurrentIndex(0)
                else:
                    self.ui_window.master_comboBox.setCurrentIndex(1)
                self.ui_window.comment_lineEdit.setText(str(el9))

                self.new_window.show()
            except IndexError:
                QMessageBox.warning(None, "Ошибка", "Необходимо выбрать строку", QMessageBox.Ok)

    def index(self):
            if self.ui.tableView.selectedIndexes():
                selected_row=self.ui.tableView.selectedIndexes()[0].row()
                index=self.ui.tableView.model().index(selected_row,0)
                id=str(index.data())
                return id
            else:
                return False


    def add_order(self): #Метод добавления нового заказа
        client=self.ui_window.client_lineEdit.text()
        device=self.ui_window.device_lineEdit.text()
        service=self.ui_window.service_lineEdit.text()
        status=self.ui_window.status_comboBox.currentText()
        price=self.ui_window.price_lineEdit.text()
        date=self.ui_window.dateEdit.text()
        number=self.ui_window.phone_lineEdit.text()
        master=self.ui_window.master_comboBox.currentText()
        comment=self.ui_window.comment_lineEdit.text()

        self.con.add_new_order(client, device, service, status, price, date, number, master, comment)
        self.view_table()
        self.new_window.close()

    def edit_selected_order(self): #Метод редактирования выбранного заказа
        if self.ui.tableView.selectedIndexes():
            selected_row=self.ui.tableView.selectedIndexes()[0].row()
            index=self.ui.tableView.model().index(selected_row,0)
            id=str(index.data()) #id выбранной ячейки

            #Выбор значений из элементов
            client=self.ui_window.client_lineEdit.text()
            device=self.ui_window.device_lineEdit.text()
            service=self.ui_window.service_lineEdit.text()
            status=self.ui_window.status_comboBox.currentText()
            price=self.ui_window.price_lineEdit.text()
            date=self.ui_window.dateEdit.text()
            number=self.ui_window.phone_lineEdit.text()
            master=self.ui_window.master_comboBox.currentText()
            comment=self.ui_window.comment_lineEdit.text()
            self.con.edit_order(client, device, service, status, price, date, number, master, comment, id)
        else: #Если строка не выбрана
            QMessageBox.warning(None, "Ошибка", "Необходимо выбрать строку", QMessageBox.Ok)

        self.view_table()
        self.new_window.close()

    def delete_selected_order(self): #Метод удаления заказа
        if self.ui.tableView.selectedIndexes():
            selected_row=self.ui.tableView.selectedIndexes()[0].row()
            index=self.ui.tableView.model().index(selected_row,0)
            id=str(index.data())
            self.con.delete_order(id)
        else:
            QMessageBox.warning(None, "Ошибка", "Необходимо выбрать строку", QMessageBox.Ok)

        self.view_table()

    
    def export_to_excel_with_pandas(self, table_view, file_path):
        model = table_view.model()
        if not model:
            return

        #Собираем данные в список
        data = []
        headers = [model.headerData(col, Qt.Horizontal) for col in range(model.columnCount())]

        for row in range(model.rowCount()):
            row_data = [model.index(row, col).data() for col in range(model.columnCount())]
            data.append(row_data)

        #Создание DataFrame и записываем в Excel
        df = pd.DataFrame(data, columns=headers)
        df.to_excel(file_path, index=False)
        QMessageBox.about(None, "Выполнено", "Файл успешно создан на рабочем столе")


    def open_manual(self):
        path=os.path.dirname(os.path.abspath(__file__))+r"\manual.chm"
        if os.path.exists(path):
            os.startfile(path)


    


if __name__=="__main__":
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)#Обращение к пользовательскому идентификатору приложения
    app=QApplication(sys.argv)
    splash=GIF_Window()
    path=os.path.dirname(os.path.abspath(__file__))
    splash.setWindowIcon(QIcon(path+"\\GL.ico"))
    splash.show()

    global window
    
    global splash_shown
    splash_shown=False

    def show_Base_Window():
        global window, splash_shown
        if not splash_shown:# Проверка не запускалась ли заставка ранее
            splash_shown=True
            window = GrodnoLaptop()  # Создаем основное окно
            window.show()  # Показываем основное окно
            splash.close()  # Закрываем заставку
    splash.start_timer(callback=show_Base_Window, duration=4000)


    sys.exit(app.exec_())
