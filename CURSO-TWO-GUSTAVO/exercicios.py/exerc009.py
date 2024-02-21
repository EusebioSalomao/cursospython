# TABUADA
numero = int(input('Digite um número inteiro para ver a sua tabuada: '))
contador = 1

while contador < 13:
    produto = numero * contador
    print(f'{numero} x {contador} = {produto}')
    contador = contador + 1

print('===== FIM =====')