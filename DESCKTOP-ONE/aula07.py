from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('AULA 07 - CHECK BOX')
        ck = QCheckBox('Marque se é verdadeiro')
        ck.setCheckState(Qt.Checked)
        ck.stateChanged.connect(self.show_state)
        self.setCentralWidget(ck)


    def show_state(self, s):
        print('Clicou!')
        print(s == Qt.Checked)
        print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()