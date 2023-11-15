from PySide6.QtWidgets import(QPushButton, QWidget, QVBoxLayout)

class ImportantGui(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.addWidget(self.Draw())
        self.setLayout(layout)

    def Draw(self):
        return QPushButton("Important")