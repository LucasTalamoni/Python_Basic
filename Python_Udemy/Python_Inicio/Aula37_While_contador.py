frase = 'aaaaooo'

# O código abaixo verifica qual letra apareceu mais vezes

i = 0
qtd_apareceu_mais_vezes = 0     # variavel que armazeno o numero de vezes da letra que mais apareceu
letra_apareceu_mais_vezes = ''  # variavel que armazena a letra que mais apareceu

while i < len(frase):   # Len conta os caracteres da frase
    letra_atual = frase[i]  # pega a letra atual para fazer sua contagem e ver quantas vezes ela apareceu

    if letra_atual == ' ':  # Se a letra atual for um espaço, ele ignora
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)    # Aqui ele faz a contagem de quantas vezes a letra que estamos verificando apareceu na frase

    if qtd_apareceu_mais_vezes <= qtd_atual:    # Verifica se a quantidade da letra que apareceu mais vezes é maior ou igual a letra que estamos verificando no momento
        qtd_apareceu_mais_vezes = qtd_atual     # qtd_apareceu_mais_vezes passar a ter o valor da qtd_atual o if for verdadeiro
        letra_apareceu_mais_vezes = letra_atual # letra_apareceu_mais_vezes passa a ter a letra_atual se o if for verdadeiro

    i += 1  # Soma +1 ao indice para partir para proxima letra

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)