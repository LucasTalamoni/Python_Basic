"""
Interpolação básica de Strigs

s - String
d e i - int
f- float
x e X - Hexadecimal (0123456789ABCDEF)
x = minusculo
X = maiusculo
"""

nome = 'Lucas'
preco = 100.9653846
variavel = '%s, o preço total foi de R$%.2f' %(nome, preco)
'''
A interpolação basica funciona como na linguagem C, onde é preciso
colocar %s, %f, ou seja la qual for o tipo de variavel e logo em seguida
colocar as variaveis na ordem certa na frente. Não se esqueça do % antes
'''
print (variavel)