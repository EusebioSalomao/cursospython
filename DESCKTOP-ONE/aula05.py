from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QSize

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AULA05')

        widget = QLabel('Aula 05 - Label') # Criar uma label
        font = widget.font() # criar uma variavel para font
        font.setPointSize(35) # definir a font
        widget.setFont(font) # Atribuir a font a label(widget)

        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Alinhamento centrado na vertical e na horizontal
        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()