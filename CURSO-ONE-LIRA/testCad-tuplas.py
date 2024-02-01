# EXERCÍCIO DE CADASTRO USANDO TUPLAS

nome = input('Informe seu nome por favor: ')
email = input('Informe seu E-Mail: ')

nome = nome.capitalize()
email = email.lower()

dados = {'nome': nome, 'email': email}
servidor = ''
if '@' in dados['email']:
    posicao = dados['email'].find('@')
    servidor = dados['email'][posicao:]
    posi_nome = dados['nome'].find(' ')
    primeiro_nome = dados['nome'][:posi_nome]
    print(f'\n Ola {primeiro_nome} \nSeja Bem Vindo')
    print(f'Enviamos um link de confirmação para o E-Mail: {dados["email"][0]}***{servidor}')
else:
    print(f'Erro! \nDigita correctamente o E-Mail: exemplo@hotmail.com \nTente novamente.')