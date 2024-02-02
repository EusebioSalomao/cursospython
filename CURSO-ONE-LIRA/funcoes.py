# FUNÇÕES EM PYTHON
lista_precos = [1500, 1000, 800, 2000]
total_imposto = 0

def calcular_imposto(preco):
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(f'Preço: {preco}, Imposto: {imposto}')
    return imposto

for preco in lista_precos:
    imposto = calcular_imposto(preco)
    total_imposto = total_imposto + imposto

print(f'Total de imposto: {total_imposto}')


# Função com parametros definido
notas = [20, 12, 9]
def calcular_media(nota, div1=1, div2=2, div3=3):
    if len(notas) == 1:
        media = sum(notas) / div1
    elif len(notas) == 2:
        media = sum(notas) / div2
    else:
        media = sum(notas) / div3
    return media

for nota in notas:
    media = calcular_media(nota)
    print(f'Nota: {nota}, Media: {media:.2f}')


# Função retornando Tupla (Uma túma é imutável)
def calculo(preco, ir=0.276, csll=0.035, iss=0.05):
    imposto_ir = preco * ir 
    imposto_csll = preco * csll 
    imposto_iss = preco * iss 
    # Retorna uma tupla
    return imposto_ir, imposto_csll, imposto_iss

resposta = calculo(1000)
print(resposta)