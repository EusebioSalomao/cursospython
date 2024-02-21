from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aula 09 - Listabox')
        lb = QListWidget()
        lb.addItems(['item 1', 'item 2','item 3'])
        self.setCentralWidget(lb)
        lb.currentItemChanged.connect(self.index_change) # Chamando evento para executar a função
        lb.currentTextChanged.connect(self.text_changed) # Chamando evento para executar a função

    def index_change(self,i):
        print(i.text())
    
    def text_changed(self,s):
        print(s)
        if s == 'item 2':
            print('ok')
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()