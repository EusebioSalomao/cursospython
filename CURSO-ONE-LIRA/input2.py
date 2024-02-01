#EXERCICIO DE FATURAMENTO
faturamento = input('Informa o faturamento do dia: ')
custo = input('Custo: ')
faturamento = float(faturamento)
custo = float(custo)
lucro = float(faturamento) - float(custo)


print(f'Faturamento: {faturamento} \nCusto: {custo} \nLucro: {lucro:.2f}')