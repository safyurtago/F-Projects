import sys
from PyQt6.QtWidgets import *

class BoardButton (QPushButton):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def __setText(self, turn: bool) -> None:
        super().setText("X") if turn else super().setText("O")
        self.setDisabled(True)
    
    def mouseReleaseEvent(self, e) -> None:
        self.__setText(self.parent.turn)
        self.parent.turn = not self.parent.turn
        return super().mouseReleaseEvent(e)


class Board (QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.turn = True

        self.grid = QGridLayout()
        c = [(i, j) for i in range(3) for j in range(3)]
        for i in c:
            btn1 = BoardButton(self)
            self.grid.addWidget(btn1, *i)

        self.setLayout(self.grid)


app = QApplication([])
win = Board()
win.show()
sys.exit(app.exec())
