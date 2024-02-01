faturamento = 1000
custo = 3000
lucro = faturamento - custo

if lucro > 0 :
    print(f'Lucro: {lucro}')

else:
    print(f'Prejuizo!')


# produtos = ['iphone', 'ipad', 'airpod']
# novo_produto = input('Isere um novo produto: ')

# if novo_produto in produtos:
#     print('Este produto ja consta nalista dos cadastrados!')
# else:
#     produtos.append(novo_produto)
#     print('Novo produto cadastrado com sucesso!')

# print(produtos)


# Exercício desafio
    # Sistema de consulta de  preços
    produtos = ['celular', 'camera', 'fone de ouvidos', 'monitor']
    precos = [1500, 1000, 800, 2000 ]

    print('Ola bem vindo!')
    produto_consultado = input('Por favor, informa o produto que pretende consultar:')
    produto_consultado.lower()

    if produto_consultado in produtos:
        posicao_prod = produtos.index(produto_consultado)
        print(f'Resultado encontrado \nDescrição: {produto_consultado.capitalize()} \nPreço: {precos[posicao_prod]}')
    else:
        print('Lamentamos! \nNão temos o produto que consultou.')
        
print('Obrigado por usarnossos serviços')