import sys
import sqlite3
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, \
    QComboBox


class addEditCoffee(QMainWindow):
    def __init__(self, parent, con, edit=False, options=()):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.parent = parent
        self.con = con
        self.edit_coffee = edit
        if edit:
            self.id = options[0]
            self.options = options
            self.edit()
        self.pushButton.clicked.connect(self.add_edit)

    def edit(self):
        _, name, deef, corn, about, price, size = self.options
        self.name.setText(name)
        self.deef.setText(deef)
        self.comboBox.setCurrentIndex(0 if corn == 'true' else 1)
        self.url.setText(about)
        self.price.setText(str(price))
        self.spinBox.setValue(size)

    def add_edit(self):
        if self.edit_coffee:
            self.con.cursor().execute(
                f"""UPDATE coffees SET name='{self.name.text()}',
d='{self.deef.text()}',
corns='{self.comboBox.currentText()}',
about='{self.url.text()}', price={self.price.text()},
size={self.spinBox.value()} WHERE id={self.id}""")
        else:
            self.con.cursor().execute(
                f"""INSERT INTO coffees(name, 

d, corns, about, price, size)
         VALUES('{self.name.text()}', '{self.deef.text()}',
'{self.comboBox.currentText()}', '{self.url.text()}', {self.price.text()},
{self.spinBox.value()})""")
        self.con.commit()
        self.close()
        self.parent.printTable()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.TITLE = ['ID', 'Название', 'Степень обжарки', 'В зернах',
                      'Описание вкуса', 'Цена', 'Объем упаковки']
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.con = sqlite3.connect('coffee.db')
        self.cur = self.con.cursor()
        self.printTable()
        self.select = 0
        self.tableWidget.cellClicked.connect(self.upload)
        self.add.clicked.connect(self.add_co)
        self.edit.clicked.connect(self.edit_co)

    def upload(self):
        for item in self.tableWidget.selectedItems():
            self.select = item.row()

    def add_co(self):
        self.a = addEditCoffee(self, self.con)
        self.a.show()

    def edit_co(self):
        res = self.cur.execute(f"""SELECT * FROM coffees WHERE id={self.tableWidget.item(self.select, 0).text()}""").fetchone()
        self.a = addEditCoffee(self, self.con, True, res)
        self.a.show()

    def printTable(self):
        result = self.cur.execute("""SELECT * FROM coffees""").fetchall()
        print(result)
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
