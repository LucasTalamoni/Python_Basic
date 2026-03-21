# ID é onde a variavel está armazenada na memória

v1 = 'a'
v2 = 'a'
v3 = 'b'

print(id(v1))
print(id(v2))
print(id(v3))

'''
O python tenta ser o mais eficiente possivel
Então se ele detectar o mesmo valor para variaveis diferentes,
ele vai tentar usar um local só, na memória para armazenar esse valor
e usa-lo para diferentes variaveis, desde que o valor seja o mesmo

'''