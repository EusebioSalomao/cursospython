# Compra de dolares
# USD 1.00 = R$ 3.27

valor_existente = float(input('Informa a quantidade de dinheiro: '))
taxa_dolar = 3.27
dolar_comprado = valor_existente / taxa_dolar

print(f'Com R$ {valor_existente} voce pode comprar USD {dolar_comprado:.2f}')