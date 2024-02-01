nome = input('Digiteaquio seu nome: ')
email = input('Digiteo seu email: ')

posicao = nome.find(' ')
posicao2 = email.find('@')
servidor = email[posicao2:]
primeiro_nome = nome[:posicao]
#print(f'Usuário cadastrado com email {email} \nOla {primeiro_nome}, seja bem vindo!')
print(f'Nome: {nome}')
print(f'Enviamos um link de confirmação para o email {email[0]}***{servidor} ')