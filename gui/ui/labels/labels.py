from PySide6.QtWidgets import(QPushButton, QWidget, QVBoxLayout)

class LabelsGui(QWidget):
    def __init__(self):
        super().__init__()

        self.labels = []
        self.file =  open("gui/ui/labels/names.txt", "r")
        self.lines = self.file.readlines()
        self.labels = self.lines

        layout = QVBoxLayout()
        layout.addWidget(self.Draw())
        self.setLayout(layout)

    def Draw(self):
        return QPushButton("Labels")
    
    def AddLabel(self, lable_name: str):
        self.labels.append(lable_name )
        open("gui/ui/labels/names.txt", "a").write("\n"+lable_name)

           
    def RemoveLabel(self, index: int):
        self.labels.remove[self.labels[index]]
        