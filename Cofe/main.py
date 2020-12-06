import sys
import sqlite3
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.TITLE = ['ID', 'Название', 'Степень обжарки', 'В зернах',
                      'Описание вкуса', 'Цена', 'Объем упаковки']
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        con = sqlite3.connect('coffee.db')
        self.cur = con.cursor()
        self.result = self.cur.execute("""SELECT * FROM coffees""")
        self.printTable(self.result)

    def printTable(self, result):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(len(self.TITLE))
        self.tableWidget.setHorizontalHeaderLabels(self.TITLE)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
