"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você  vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os  # Importa o módulo os para manipulação de comandos do sistema, como limpar a tela do terminal

# Definição da palavra secreta que o jogador precisa adivinhar
palavra_secreta = 'perfume'  # A palavra a ser adivinhada

# Inicializa a variável que armazenará as letras corretas que o jogador adivinhou
letras_acertadas = ''  # Inicializa a string das letras acertadas (vazia no começo)

# Inicializa o contador de tentativas
numero_tentativas = 0  # Variável para contar o número de tentativas feitas

# Início do loop do jogo
while True:
    # Solicita ao jogador que digite uma letra
    letra_digitada = input('Digite uma letra: ') 
    numero_tentativas += 1  # A cada tentativa, incrementa o contador de tentativas

    # Verifica se o jogador digitou mais de uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')  # Informa que deve ser digitada apenas uma letra
        continue  # Retorna ao início do loop, pedindo uma nova entrada

    # Verifica se a letra digitada está presente na palavra secreta
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada  # Se a letra estiver na palavra, adiciona à lista de letras acertadas
    
    # Inicializa a variável para formar a palavra com os acertos
    palavra_formada = ''

    # Percorre cada letra da palavra secreta
    for letra_secreta in palavra_secreta:
        # Se a letra da palavra secreta já foi acertada, adiciona ela à palavra formada
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'  # Se a letra não foi acertada, adiciona um asterisco (*) para ocultá-la

# Explicação do for
# A cada iteração do loop, a variável letra_secreta percorre cada letra da palavra_secreta.
# Se a letra já foi acertada (se a letra está presente em letras_acertadas), ela é adicionada à palavra_formada na mesma posição em que ela aparece na palavra secreta.
# Se a letra não foi acertada ainda, um asterisco (*) é colocado no lugar dessa letra na palavra_formada.

# Explicação do loop:
    # for letra_secreta in palavra_secreta:
        # O comando for é um laço de repetição que vai iterar sobre cada caractere da variável palavra_secreta.
        # A cada iteração, o valor de cada caractere da palavra_secreta é atribuído à variável letra_secreta. Ou seja, letra_secreta vai "receber" as letras da palavra secreta uma por vez, da esquerda para a direita.
    # Exemplo: Se a palavra_secreta for "perfume", o laço vai funcionar assim:
        # Na 1ª iteração, letra_secreta será 'p'.
        # Na 2ª iteração, letra_secreta será 'e'.
        # Na 3ª iteração, letra_secreta será 'r', e assim por diante até a última letra.

    # Exibe a palavra formada até o momento (com as letras acertadas e os asteriscos nas letras faltantes)
    print('Palavra formada: ', palavra_formada)

    # Verifica se o jogador acertou toda a palavra
    if palavra_formada == palavra_secreta:
        os.system('cls')  # Limpa a tela do terminal (apenas para sistemas Windows)
        # Informa ao jogador que ele venceu
        print('VOCÊ GANHOU!!!!')
        print('A palavra era:', palavra_formada)
        print('Tentativas: ', numero_tentativas)  # Exibe o número de tentativas feitas

        # Reinicia o jogo (variáveis resetadas para um novo jogo)
        letras_acertadas = ''  # Reseta as letras acertadas
        numero_tentativas = 0  # Reseta o número de tentativas