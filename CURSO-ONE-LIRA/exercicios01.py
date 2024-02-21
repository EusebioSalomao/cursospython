# Cada venda, o vendedor ganha R$2 e 1% do valor de venda
# Calcular o valor total de bonus pago e o bonus de cada vendedor

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180,]
}

total_bonhus_pago = 0
for vendedor in vendas:
    ganho_venda = 0
    ganho_percentual = 0
    bonus = 0
    for venda in vendas[vendedor]:
        ganho_venda = ganho_venda + 2
        ganho_percentual = ganho_percentual + (venda * 0.01)
        bonus = ganho_venda + ganho_percentual
    total_bonhus_pago = total_bonhus_pago + bonus
    print(f'Vendedor: {vendedor}, Bonus: {bonus}')
print(f'Total de bonus pago: {total_bonhus_pago}')