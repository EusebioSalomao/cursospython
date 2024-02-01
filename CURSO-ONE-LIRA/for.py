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