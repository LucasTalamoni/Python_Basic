"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue 
    '''
    O continue faz com que seja pulado uma parte da execução
    No caso deste IF acima, ele faz com que quando o contador for igual a 6, ele pule todo o resto 
    e volte para o começo do while, sem que a execução do while seja interrompida, diferente
    do BREAK
    '''

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue


    print(contador)


print('Acabou')