
vendas = [123, 300, 213, 409]

ultimo = vendas[-1] # Retorna o último elemento da lista
total_vendas = sum(vendas) # Retorna a soma dos elemento da lista, no caso de números
quantidade = len(vendas) # Retorna a quantidade de elementos na lista
valor_max = max(vendas) # Retorna o valor máximo da lista
valor_min = min(vendas) # Retorna o valor mínimo da lista
posicao = vendas.index(300) # Retorna a posição do elemento

print(vendas[2:]) # Retorna os elementos a partir da posição definida, incluindo o elemento da posição
print(vendas[:2]) # Retorna os elementos até posição definida, mais o elemento da posição não conta

#Lista dde produto
produtos = ["iphone", "ipad", "sammssung"]
precos = [67900, 76500, 53000]
precos[0] = 112000 # Alterar o valor do elemento na posição selecionada
produtos.append('macbook') # Adiciona um novo elemento na lista (no final)
produtos.insert(2, 'nókia') # Adiciona um elemento numa determinada posição 
precos.append(136000) # Adiciona um novo elemento na lista
contar_elemento = produtos.count("iphone") # Conta quaantas vezes um elemento aparece em uma lista
consta_na_lista = 'nokia' in produtos # Verifica se um determinadoitem consta na lista, retornando true ou false
produtos.sort(reverse=True) # Ordena a lista decrescentemente
produtos.sort() # Ordena a lista crescentemente

print(produtos)
print(precos)

produtos.remove('ipad') # Remover de acordo ao valor doelemento
precos.pop(1) # Remover de acordo ao indice do elemento
