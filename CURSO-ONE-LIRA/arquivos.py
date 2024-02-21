
# Abrir arquivo e feichar

with open("vendas.txt", "r") as arquivo:
    # Fazer o que quizar com o arquivo
   # infos = arquivo.read() # Faz a leitura do jeito padrão
    infos2 = arquivo.readlines() # Faz a leitira em linha

#print(infos)
print(infos2)