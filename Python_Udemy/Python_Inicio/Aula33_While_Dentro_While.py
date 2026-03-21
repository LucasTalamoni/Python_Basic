"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        '''
        O sinal de igual na frente do nome da variavel, faz que o nome da variavel seja exibida, junto com seu valor
        '''
        coluna += 1
    linha += 1


print('Acabou')