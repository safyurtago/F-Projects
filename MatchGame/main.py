import time
import sys
from PyQt6.QtWidgets import *
from numbers_list import *

class MyButton(QPushButton):
    def __init__(self, parent, idx):
        super().__init__()
        self.parent = parent
        self.idx = idx
        self.turn = False


    def setText(self, turn) -> None:
        print(self.parent.lst)
        if len(self.parent.lst) > 1 and self.parent.lst[0] == self.parent.lst[1]:
            super().setText(f"{return_value(self.idx)}")
            self.parent.lst.pop(0)
            self.parent.lst.pop(0)
            self.setDisabled(True)
        elif len(self.parent.lst) == 1:
            if turn == False: 
                super().setText(f"{return_value(self.idx)}")  
            else: 
                super().setText("")
            self.turn = False
        if len(self.parent.lst) > 1 and self.parent.lst[0] != self.parent.lst[1]:
            self.parent.lst.pop(0)
            self.parent.lst.pop(0)
        

    def mouseReleaseEvent(self, e) -> None:
        self.parent.lst.append(return_value(self.idx))
        self.setText(self.turn)
        return super().mouseReleaseEvent(e)
    
    def leaveEvent(self, a0) -> None:
        self.turn = True
        self.setText(self.turn)
        return super().leaveEvent(a0)
    
        

class MainWindow (QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.turn = False
        self.lst = []
        self.fill_grid()

    def fill_grid(self):
        self.grid = QGridLayout()
        c = [(i, j) for i in range(4) for j in range(4)]
        self.idx = 0

        for i in c:
            btn = MyButton(self, self.idx)
            self.idx += 1
            self.grid.addWidget(btn, *i)
        self.setLayout(self.grid)
        
 


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())