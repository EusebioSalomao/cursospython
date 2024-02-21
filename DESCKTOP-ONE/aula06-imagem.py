from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap

import sys

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aula 06 - imagem')

        widget = QLabel('Pixmap')
        widget.setPixmap(QPixmap("ppp.jpg"))
        widget.setScaledContents(True)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
window = MainWindows()
window.show()
app.exec_()