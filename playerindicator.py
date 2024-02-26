
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QSizePolicy
from PyQt5.QtGui import QPolygon, QPainter, QPen, QBrush
from PyQt5.QtCore import QPoint

class PlayerIndicator(QWidget):
    def __init__(self):
        super().__init__()
        self.setState(0)
        sz = self.sizePolicy()
        sz.setHorizontalPolicy(QSizePolicy.Preferred)
        sz.setVerticalPolicy(QSizePolicy.Preferred)
        self.setSizePolicy(sz)

    def resizeEvent(self, e):
        self.setMinimumWidth(self.height())

    def sizeHint(self):
        return QSize(10, 10)

    def setState(self, state):
        self.state = state
        self.update()

    def paintEvent(self, event):
        if self.state == 0:
            return
        qp = QPainter(self)
        qp.begin(self)  

        pen = QPen(Qt.black, 2, Qt.SolidLine)

        brush = QBrush(Qt.red, Qt.SolidPattern)

        qp.setPen(pen)
        qp.setBrush(brush)

        sz = self.size(); 

        poly = QPolygon()
        poly.append(QPoint(0, 0))
        poly.append(QPoint(int(sz.width() * 0.86), sz.height() // 2))
        poly.append(QPoint(0, sz.height()))
        qp.drawPolygon(poly)

        qp.end()

