
# O while tbm tem seu Else

string = input('Digite seu Nome: ')

# Criação do Indice para ser o contador
i = 0

while i < len(string):
    letra = string[i] # Letra armazena o caractere correspondente ao indice

    if letra == ' ':
        print('Foi encontrado um espaço no seu nome')
        break

    print(letra) # Esse print exibe o caractere armazenado referende ao indice no momento
    i += 1 # Soma +1 ao indice para partir ao proximo
else:
    print("Não encontrei um espaço na string")

print('Esse print está fora so while/else')