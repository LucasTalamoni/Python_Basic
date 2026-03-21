# Faça uma iteração com seu nome, Usando while

nome = 'Lucas Talamoni'

indice = 0
novo_nome = '' # Vazio para poder armazenar as alterações
while indice < len(nome): # Enquanto o indice for menor que o indice de cada letra do nome
    letra = nome[indice]
    if letra == ' ':
     indice += 1 # O incremento deve ser feito, para que quando ele entre nesse if, não fique em um looping
     continue
    novo_nome += f'"{letra} - {indice}"' # Sera adicionado as letras dos do nome na nova variavel, junto de seus indices
    indice += 1
    
novo_nome += ' *' # Adiciona * no final
print(novo_nome)