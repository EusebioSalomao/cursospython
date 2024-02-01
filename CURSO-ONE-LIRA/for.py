for i in range(10):
    print('Se inscreva no canal')

precos = [1500, 1000, 800, 2000]
taxa_imposto = 0.1

for preco in precos:
    imposto = preco * taxa_imposto
    print(f'Preço: {preco}, imposto: {imposto}')

#EXERCÍCIOS
    # Se o preço é até 1000 -: imposto é 10%
    # Se o preço é maior que 1000 -: imposto é 15%

total_imposto = 0
for preco in precos:
    if(preco <= 1000):
        imposto = preco * 0.1
        print(f'Preço: {preco}; Imposto: {imposto}')
    else:
        imposto = preco * 0.15
        print(f'Preço: {preco}; Imposto: {imposto}')
    total_imposto = total_imposto + imposto
print(f'Total de Imposto: {total_imposto} \nFIM!')

#EXERCÍCIO 02
vendas_22 ={"jan": 15000, "fev": 15500, "mar": 14000, "abri": 16600, "mai": 16300, "jun": 17000}
vendas_23 ={"jan": 17000, "fev": 15000, "mar": 17500, "abri": 16900, "mai": 16000, "jun": 18500}
# Saber quanto variou percentualmente cada mes de 2022 em comparação com 2022

for mes in vendas_22:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual = valor_23 / valor_22 -1
    print(f'Variação {var_percentual:.0%}')