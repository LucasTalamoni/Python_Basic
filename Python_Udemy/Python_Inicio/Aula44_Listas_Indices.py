"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +

    append = adiciona um unico elemento ao final de uma lista
    insert = insere um elemento em uma posição especifica dentro da lista
    pop = remove e retorna o elemente de um indice especificado (ou ultimo, se nenhum indice for fernecido)
    del = remove um elemento da lista com base em um indice especifico
    clear = remove todos os elementos da lista
    extend = adiciona todos os elementos de um iteravel (como lista, tupla, conjunto, etc) ao final da lista

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)