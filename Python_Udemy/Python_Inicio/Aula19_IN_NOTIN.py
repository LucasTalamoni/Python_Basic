# Operadores in e not in
# in -> está entre
# not in -> não está entre

# Strings em Python são iteráveis
# Isso quer dizer que é possivel navegar entre caracter por caracter

#  0 1 2 3 4
#  L u c a s
# -5-4-3-2-1

nome = 'Lucas'
print(nome[3])
print(nome[-2])
# entre [] está indicando o indice que vc quer acessar
# A letra 'a' está no indice 3 e -2, então ela será exibida

# O in ou not in fara que o interpretador navegue entre os indices buscando o termo requisitado
nome = input('Digite seu nome: ')
encontrar = input('Digite a ou as letra(s) que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
    # Caso o interpretador encontre a o termo entre os indices ele irá parar aqui
else:
    print(f'{encontrar} não está em {nome}')