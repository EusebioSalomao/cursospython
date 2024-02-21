# Ordem de apresntação do trabalho
import random
alunos = []

ordem = 1
while True:
    aluno = input(f'Digite o nome do {ordem}º aluno: ')
    if aluno == "1":
        break
    else:
        alunos.append(aluno)
        ordem = ordem + 1

print('Ordem de apresentação dos trabalhos')
random.shuffle(alunos)
ordem2 = 1
for aluno in alunos:
        print(f'{ordem2}º {aluno}')
        ordem2 = ordem2 + 1
