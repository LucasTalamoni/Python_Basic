"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar seua idade
Se nome e idade forem digitados exiba:
- Seu nome é:
- Seu nome invertido é:
- Seu nome contém (ou não) espaços
- Seu nome tem (n) letras
- A primeira letra do seu nome é:
- A última letra do seu nome é:
Se nada for digitado em nome ou idade exiba:
 "Desculpe, você deixou campos vazios."
"""
# Pega os dados do usuário
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ') #FIM

# Verifica se o usuário deixou algum campo vazio
# Campos sem valores são considerados falsos. Se alguma condição for falsa, já ira negar o IF
if nome and idade:

# Exibe o nome do usuário
    print(f'Seu nome é: {nome}') #FIM

# Exibe o nome invertido do usuário
    print(f'Seu nome invertido fica: {nome[::-1]}') #FIM

# Verifica se o usuário digitou espaço no nome
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços') #FIM IF-ELSE

# Exibe o número de caracteres
    print(f'Seu nome contém {len(nome)} caracteres') #FIM

# Exibe a primeira letra
    print(f'A primeira letrado seu nome é: {nome[0]}') #FIM

# Exibe a última letra
    print(f'A última letra do seu nome é: {nome[-1]}') #FIM

else:
    print('Desculpe, você deixou campos vazios...') #FIM IF-ELSE