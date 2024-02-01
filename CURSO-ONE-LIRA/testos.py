faturamento = 1000
custo = 700
lucro = faturamento - custo
taxa_imposto = 0.1

#Formasde imprimir
print(f"Faturamento: {faturamento},\nCusto: {custo}, \nLucro: {lucro - (lucro * taxa_imposto)}")
print("Lucro sem desconto de imposto: " + str(lucro))

#Converter testo minisculo para maiuscula
email = 'EUSEBIO@hotmail.com'

email = email.lower()
print(f"E-mail: {email}")

#Pesquisar um determinado caracter denreo de uma string
#Se existir retorna o indice ou a posição onde está
# Se não existir na string, retorna -1
posicao = email.find("@")
print(f"Posição: {posicao}") 
print(email[posicao])# Retorna o valor que está na posição correspondente da string

servidor = email[posicao:] # Retorna parte da string desde a posição até o final
print(f"Servidor: {servidor}")

nome_email = email[:posicao] # Retorna parte da string desde o início até a posição
print(f"Nome do E-Mail: {nome_email}")

servidor_sem = email[posicao+1:] # Retorna parte da string desde a posição até o final, sem o elemento que está na posição
print(f"Servidor: {servidor_sem}")

# Tamanho de um texto
tamanho = len(email)
print(f"Tamanho: {tamanho}")

# Trocando um pedaço de texto
email_trocado = email.replace("hotmail.com", "gmail.com")
print(f"Em-Mail trocado: {email_trocado}")

# Mudar as iniciais para maiuscula
nome = 'ulica abel samba bueti'
frase = 'meu irmão ligou para mim ontem.'
nome = nome.title() # Todas iniciais de cada palavra a maiúsculas
frase = frase.capitalize() # Só a primeira letra a maiuscula
print(f"Nome: {nome}")
print(f"Frase: {frase}")

# Especiais
# Casas decimais e virgulas nos valores
print(f"Faturamento: {faturamento:,.2f}kz \nCusto: {custo:.2f}  \nLucro: {lucro - (lucro * taxa_imposto):.2f}")

# Percentual
margem = lucro / faturamento
print(f'Percentagem da margem: {margem:.0%}') # Para duas casas decimais ({margem:.2%})


# EXERCÍCIOS
nome2 = 'António Vissoca Neto'
email_novo = 'vissoca@gmail.com' 

# Descubra o servidor do email

posicao2 = email_novo.find('@')
servidor2 = email_novo[posicao2:]
print(f'Novo servidor 2: {servidor2}')

# Pegar o primeiro nome do usuário
posicaoN = nome2.find(' ')
primeiro_nome = nome2[:posicaoN]

print(f'Primeiro nome: {primeiro_nome}')

# Construa uma mensagem 'usuário nome cadastrdo com sucesso com o email vissoca@...' 
mensagem = f'Usuário {nome2} cadastrado com sucesso com email {email_novo}'
print(mensagem)

# Enviamos um link de confirmação para email v***@gmail.com
email_barrado = email_novo[0]+ '***' +  email_novo[posicao2:]
mensage2 = f'Enviamos um link de confirmação para {email_barrado}' 
print(mensage2)

