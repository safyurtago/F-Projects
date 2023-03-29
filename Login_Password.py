import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MyWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.users_list = []
        self.setGeometry(100, 100, 700, 300)
        self.setWindowTitle("Login Password")
        self.login_label = QLabel()
        self.login_label.setText("Login")
        self.password_label = QLabel()
        self.password_label.setText("Password")
        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("Enter your login...")
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Enter your password...")
        self.sign_in_btn = QPushButton("SignIn")
        self.sign_in_btn.clicked.connect(self.sign_in)
        self.sign_up_btn = QPushButton("SignUp")
        self.sign_up_btn.clicked.connect(self.sign_up)
    
        self.main_layout = QVBoxLayout()

        self.label_box = QHBoxLayout()
        self.label_box.addWidget(self.login_label)
        self.label_box.addWidget(self.password_label)
        
        self.edit_box = QHBoxLayout()
        self.edit_box.addWidget(self.login_edit)
        self.edit_box.addWidget(self.password_edit)

        self.sign_box = QHBoxLayout()
        self.sign_box.addWidget(self.sign_in_btn)
        self.sign_box.addWidget(self.sign_up_btn)
        self.sign_box.addStretch()

        self.main_layout.addLayout(self.label_box)
        self.main_layout.addLayout(self.edit_box)
        self.main_layout.addLayout(self.sign_box)
        self.main_layout.addStretch()

        self.setLayout(self.main_layout)

    def sign_up(self):
        temp = self.login_edit.text(), self.password_edit.text()
        if temp not in self.users_list:
            self.users_list.append(temp)
        else:
            temp_box = QDialog()
            temp_box.setWindowTitle("!!! You have already signed up !!!")
            temp_box.setGeometry(500,500,400,40)
            temp_box.exec()
        self.login_edit.clear(), self.password_edit.clear()
        

    def sign_in(self):
        temp = self.login_edit.text(), self.password_edit.text()
        if temp in self.users_list:
            temp_box = QDialog()
            temp_box.setWindowTitle("Congratulations!!! You have just entered to the system")
            temp_box.setGeometry(500,500,500,40)
            temp_box.exec()
        else:
            temp_box = QDialog()
            temp_box.setWindowTitle("You need to sign up first or Wrong information")
            temp_box.setGeometry(500,500,400,40)
            temp_box.exec()
        self.login_edit.clear(), self.password_edit.clear()


if __name__ == "__main__":
    App = QApplication([])
    win = MyWindow()
    win.show()
    sys.exit(App.exec())