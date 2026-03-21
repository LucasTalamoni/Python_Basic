#Crie uma Calculadora Utilizando While

import os # Importa o sistema operacional do user

# Função criada para limpar a tela do user
def limpar_tela(): # Função para limpar a tela
    
    if os.name == 'nt': # Limpa a tela no Windows
        _ = os.system('cls')
    
    else: 
        _ = os.system('clear') # Limpa a tela em outros sistemas operacionais

# Faz com que o usuario digite apenas números e o operador correto
while True:
    limpar_tela()
    while True:
        # Verifica o numero
        try:
            number_1 = float (input('Digite um numero: '))
            number_2 = float (input('Digite outro numero: '))
            break
        except ValueError:
            print('Você não digitou um valor valido!!')
            input('Press enter...')
            limpar_tela()
    
    # Verifica o operador
    verifica_operador =  '+-/*'
    while True:
        operador = input('Digite um operador: ')
        if len(operador) > 1:
            print('Digite apenas um operador')
            continue # Faz com que volte a solicitar uma nova entrada apos encontrar um erro
        if operador not in verifica_operador:
            print('Digite apenas operadores conhecidos')
            continue # Faz com que volte a solicitar uma nova entrada apos encontrar um erro
        
        break # Sai do loop ao encontrar um operador válido

    if operador == '+':
        total = number_1 + number_2
        print(f'A soma resultou em: {total}')
    elif operador == '-':
        total = number_1 - number_2
        print(f'A subtração resultou em: {total}')
    elif operador == '/':
        total = number_1 / number_2
        print(f'A divisão resultou em: {total}')
    elif operador == '*':
        total = number_1 * number_2
        print(f'A multiplicação resultou em: {total}')
    else:
        print('OCORREU ALGUM ERRO!!!!!')

    sair = input('Deseja sair: [s]im, [n]ão: ').lower().startswith('s')
    #.lower() faz com que todas as letras se tornem minúsculo
    #.startswith() verifica se a primeira letra que foi digitada é a que está dentro dos (). Isto faz a string retornar um True, Caso contrario, ela retorna um false
    limpar_tela()

    if sair is True:
        break
