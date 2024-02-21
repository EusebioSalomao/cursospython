# Sorteando aluno para apagr o quadro

import random

alunos = []
contador = 1
while True:
    aluno = input(f'Digite o nome do {contador}º aluno: ')
    if aluno == 'Sair' or aluno == "1":
        break
    else:
        alunos.append(aluno)
    contador = contador + 1

    
print('LISTA DOS ALUNOS')
ordem = 1
for aluno in alunos:
    print(f'{ordem}º {aluno}')
    ordem = ordem + 1

escolhido = random.choice(alunos)
print(f'Para apagar o quadro foi sorteado/a {escolhido}')