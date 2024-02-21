""" nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome)) """

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
produto = n1 * n2
coef = n1 / n2
pot = n1 ** n2

print('A soma é {}, \nO produto é {}, \nO coeficiente é {:.2f}, \nA potencia é {}'.format(s, produto, coef, pot))