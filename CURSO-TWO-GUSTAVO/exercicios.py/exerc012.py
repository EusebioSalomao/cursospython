# Preço do produto

preco_actual = float(input('Informe o preço actual do produto'))
preco_novo = preco_actual - (preco_actual * 0.05)

print(f'Preço anterior é {preco_actual:.2f} \nDesconto: {preco_actual * 0.05} \nNovo preçõ: {preco_novo}')