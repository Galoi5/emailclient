from PySide6.QtWidgets import(QPushButton, QWidget, QVBoxLayout, QGroupBox,
                              QLineEdit, QHBoxLayout)
from PySide6.QtGui import QIcon

from gui.ui.base import AbstractMailBox


class InboxGui(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(AbstractMailBox().SearchBar())
        layout.addWidget(AbstractMailBox().ConfigBar())
        layout.addWidget(AbstractMailBox().EmailSlate())
        self.setLayout(layout)


    
