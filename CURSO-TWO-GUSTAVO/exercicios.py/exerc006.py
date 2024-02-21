# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print(f'Primeira nota {nota1} \nSegunda nota {nota2} \nA média do aluno é {media:.2f}')
print('======= FIM ========')