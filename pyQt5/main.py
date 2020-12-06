import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtWidgets


class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 625)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Клик!"))
        self.pushButton.setText(_translate("Form", "Клик!"))


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.size = 0
        self.color = QColor(0, 0, 0)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.size = randrange(100, 250)
        self.color = QColor(randrange(0, 255), randrange(0, 255),
                            randrange(0, 255))
        self.repaint()

    def draw(self):
        # Задаем кисть
        self.qp.setBrush(self.color)
        s = (self.size // 2)
        x, y = (200, 300)
        self.qp.drawEllipse(int(x - s), int(y - s),
                            int(self.size), int(self.size))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
