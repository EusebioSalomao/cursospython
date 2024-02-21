from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aula 10 - QLineEdit')

        # Criar o campo detexto
        self.le = QLineEdit()
        self.le.setMaxLength(10) # Definir a quantidade de caracter
        self.le.setPlaceholderText('Digite o seu nome') 

        self.le.returnPressed.connect(self.return_pressed) # Executar a função atravéz do evento
        self.le.selectionChanged.connect(self.selection_changed)
        self.le.textChanged.connect(self.text_changed)
        self.le.textEdited.connect(self.text_Edited)

        self.setCentralWidget(self.le)

    def return_pressed(self):
        print('Botão clicado!')
        self.centralWidget().setText(f'Olá {self.le.text()}')

    def selection_changed(self):
        print('Seleção mudada')
        print(self.centralWidget().selectedText())

    def text_changed(self,s):
        print('Text changed...')
        print(s)

    def text_Edited(self,s):
        print('Text edited..')
        print(s)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()