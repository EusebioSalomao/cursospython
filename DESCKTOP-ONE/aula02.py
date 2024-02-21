from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize # Para trabalhar com tamanhos
import sys

# Criação de classe com miniconfiguração
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Minha primeira app")
        self.button = QPushButton("CLIQUE AQUI!") # Criar um botão
        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.cliked_button) # Chamando o evento clicked para executar a função clicked_button

    # Criar uma função para responder o evento clicar do botão
    def cliked_button(self):
        print('Botão clicado!')
        self.button.setEnabled(False)
        self.setWindowTitle('Primeiro click')

app = QApplication(sys.argv)

window = MainWindow() # Uma variável recebe a classe criada
window.show()
app.exec_()