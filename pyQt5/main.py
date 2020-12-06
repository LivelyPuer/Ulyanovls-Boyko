import sys
from random import randrange

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QPolygonF, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.size = 0
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
        self.repaint()

    def draw(self):
        # Задаем кисть
        self.qp.setBrush(QColor("#FFFF00"))
        s = (self.size // 2)
        x, y = (200, 300)
        self.qp.drawPolygon(
            QPolygonF([QPointF(x, y - s), QPointF(x - s, y + s),
                       QPointF(x + s, y + s)]))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())