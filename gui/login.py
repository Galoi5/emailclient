from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, QCheckBox, 
                               QGridLayout, QPushButton)
from gui.gui import MainWindow


class LoginGui(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Login")
        
        
        self.username_label = QLabel("Email:")
        self.username_input = QLineEdit()
        self.username_label.setBuddy(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_label.setBuddy(self.password_input)

        self.toggle_password_echo_checkbox = QCheckBox("Show")
        self.toggle_password_echo_checkbox.toggled.connect(self.toggle_password_echo_mode)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.login)

        layout = QGridLayout()

        layout.addWidget(self.username_label, 0, 0)
        layout.addWidget(self.username_input, 0, 1)
        layout.addWidget(self.password_label, 1, 0)
        layout.addWidget(self.password_input, 1, 1)
        layout.addWidget(self.toggle_password_echo_checkbox, 1, 2)
        layout.addWidget(self.submit_button, 2, 0, 1, 3)

        self.setLayout(layout)

    def toggle_password_echo_mode(self):
        if self.toggle_password_echo_checkbox.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)

    def login(self):
        global main_gui
        main_gui = MainWindow()
        main_gui.showMaximized()
        self.deleteLater()


