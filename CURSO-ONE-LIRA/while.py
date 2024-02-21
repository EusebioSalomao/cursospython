contador = 0

#while contador < 1:
 #   print('increva-se no canal!')
  #  contador = contador + 1

#print('Obrigadopor se inscrever.')

#Exdrcício do cadastro de produto com while
produtos = []
def cadastrar_produto(novo_produto):
    mensagem = ''
    produto = novo_produto.capitalize()
    if produto in produtos:
        mensagem = 'O produto que tentou inserir já se encontra na lista de produtos.'
    else:
        produtos.append(produto)
        mensagem = 'Produto cadastrado com sucesso!'
    return mensagem

while True:
    print('Para sair digita 1')
    novo_produto = input('Didite um novo produto: ')
    if novo_produto == '1':
        break
    else:
       mensagem = cadastrar_produto(novo_produto)
       print(mensagem)

print('PRODUTOS CADASTRADOS')
print(produtos)
