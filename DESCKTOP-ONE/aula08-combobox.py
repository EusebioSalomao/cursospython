from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aula 08 - Combobox')
        self.setFixedSize(QSize(400,300))

        self.combo = QComboBox()
        self.combo.addItems(['item 1', 'item 2', 'item 3'])
        self.setCentralWidget(self.combo)

        self.combo.currentIndexChanged.connect(self.index_change)
        self.combo.currentTextChanged.connect(self.text_change)

    def index_change(self,i):
        print(i)

    def text_change(self, s):
        print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()