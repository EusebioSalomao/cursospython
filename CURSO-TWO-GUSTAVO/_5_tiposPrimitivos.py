# TIPOS DE VARIÁVEIS PRIMITIVAS E SAIDA DE DADOS EM PYTHON
#  inteiros, float, boleano (bool)  e string (str)

n1 = 1 # Inteiro (int)
n2 = 2
n3 = 2.3 # float (ponto flutuante)
nome = "Eusébio"

s = n1 + n2
print(s) # Comando de saida
print(nome)

nome2 = input('Digita um nome: ')
print(nome2.isalpha())
n3 = int(input('Digite um nímero: '))

n4 = int(input('Digite outro nímero: '))

soma = n3 + n4
print(f'Ola {nome2},  a soma entre {n3} e {n4} é {soma}')

# Desafio
print('==== DESAFIO =====')
entrada = input('Digite algo: ')
