# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor

numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1

print(f'Voce digitou o número {numero}. \nO seu antecessor é {antecessor} e o seu sucessor é {sucessor}')
fim = 'FIM'
print('{:=^20}'.format(fim))

