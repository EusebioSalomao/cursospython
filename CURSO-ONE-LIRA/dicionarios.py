produtos = {"iphone": 90500, "ipad": 40000, "celular": 59980} # Criação de Dicionário

produto_consultado = input('Digite o nome do produto: ')
produto_consultado = produto_consultado.lower() # Converter para minúsculo
print(produto_consultado)

if produto_consultado in produtos:
    print('RESULTADO OBTIDO')
    preco = produtos[produto_consultado] # Retorna o valor da posição da chave
    print(f'Descrição: {produto_consultado.capitalize()}') # Retorna a descrição com inicial maiúscula
    print(f'Preço: {preco:.2f}')
else:
    print('Lamentamos \nEste produto não consta na nossa lista!')

print('OBRIGADO POR USAR OS NOSSOS SERVIÇOS!')