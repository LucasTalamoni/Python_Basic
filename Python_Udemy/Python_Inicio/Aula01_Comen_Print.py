# Para adicionar Comentarios é necessario adicionar # no começo da frase
# No comentario o interpretador não lê, ele ignora tudo o que vem na linha

"""
Isto é uma DocString (As três aspas)
é semelhante a um comentario, porém podemos pular linhas
"""

'''
Tbm é possivel usar aspas simples
'''

"""
As DocString's o interpretador lê e somente as guarda na memória
sem fazer nada 
"""
print(123)
print('Text')
print(12, 34)
print(12, 34, sep="-")
print(12, 34, 1001, sep=" -- ")
# sep= é um separador que atua entre as virgulas
#O que tiver entre as aspas, ficará no meio do texto por virgula