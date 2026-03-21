texto = 'Python'

novo_texto = ''

for letra in texto:
    """
    - Dentro do laço for letra in texto:, o Python automaticamente cria a variável letra e a vai atribuindo
    cada caractere de texto a cada iteração do loop. Ou seja, no primeiro ciclo, letra será 'P', no segundo será 'y', e assim por diante. 
    - Não é necessário declarar letra antes do laço porque o Python cuida disso internamente dentro do for.
    """
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')