import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from random import randint

x_random = randint(0, 900)
y_random = randint(0, 650)

class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("You Can't Move The Button")
        self.setGeometry(100, 100, 1000, 700)
        self.not_move = QPushButton("you can't move me", self)
        self.not_move.setGeometry(x_random, y_random, 150, 40)
        self.a = 100
        self.b = 100
    def moveEvent(self, a0) -> None:
        if self.x() > self.a: 
            self.not_move.move(self.not_move.x() - (self.x() - self.a), self.not_move.y())
            self.a = self.x()
        elif self.x() < self.a:
            self.not_move.move(self.not_move.x() + (self.a - self.x()), self.not_move.y())
            self.a = self.x()
        if self.y() > self.b: 
            self.not_move.move(self.not_move.x(), self.not_move.y() - (self.y() - self.b))
            self.b = self.y()
        elif self.y() < self.b:
            self.not_move.move(self.not_move.x(), self.not_move.y() + (self.b - self.y()))
            self.b = self.y()

        return super().moveEvent(a0)
        

        

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    sys.exit(app.exec())