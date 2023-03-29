import sys
from PyQt6.QtWidgets import *
# from PyQt6.QtGui import *
# from PyQt6.QtCore import *
from random import randint

x_random = randint(0, 900)
y_random = randint(40, 650)

class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("MOVE IT")
        self.setGeometry(100, 100, 1000, 700)
        self.label = QLabel("", self)
    
        self.button1 = QPushButton("Right", self)
        self.button1.setGeometry(10, 0, 100, 40)
        self.button2 = QPushButton("Left", self)
        self.button2.setGeometry(110, 0, 100, 40)
        self.button3 = QPushButton("Up", self)
        self.button3.setGeometry(210, 0, 100, 40)
        self.button4 = QPushButton("Down", self)
        self.button4.setGeometry(310, 0, 100, 40)
        
        self.button1.clicked.connect(lambda: self.move__me("Right"))
        self.button2.clicked.connect(lambda: self.move__me("Left"))
        self.button3.clicked.connect(lambda: self.move__me("Up"))
        self.button4.clicked.connect(lambda: self.move__me("Down"))

        self.move_me = QPushButton("MOVE ME", self)
        self.move_me.setGeometry(x_random, y_random, 100, 40)
        
    def  move__me(self, direction):
        if self.move_me.x() > 1000: self.move_me.move(0, self.move_me.y())
        elif self.move_me.x()+100 < 0: self.move_me.move(1000, self.move_me.y())
        if self.move_me.y() > 700: self.move_me.move(self.move_me.x(), 0)
        elif self.move_me.y()+40 < 0: self.move_me.move(self.move_me.x(), 700)
        if direction.lower() == 'right': 
            self.move_me.move(self.move_me.x()+10, self.move_me.y())
        elif direction.lower() == 'left': 
            self.move_me.move(self.move_me.x()-10, self.move_me.y())
        elif direction.lower() == 'up': 
            self.move_me.move(self.move_me.x(), self.move_me.y()-10)
        elif direction.lower() == 'down': 
            self.move_me.move(self.move_me.x(), self.move_me.y()+10)
    
        
        

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    sys.exit(app.exec())