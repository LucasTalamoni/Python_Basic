"""
Formatação básica de strings

s- Strings
d - int
f - Float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda (Preenche caracteres a esqueda)
< - Direita (Preenche caracteres a direita)
^ - Centro
Sinal - + ou -
Ex.: 0>-100, .1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print (f'{variavel}')
print (f'.{variavel: >10}') # Preenche 10 caracteres a esquerda (7 espaços em branco + ABC)
print (f'{variavel: <10}.') # Preenche 10 caracteres a direita (ABC + espaços em branco)
print (f'{variavel: ^11}.') # Preenche 11 caracteres e coloca a variavel no centro (Ele tenta colocar a variavel no meio de 10 caracteres)
# Se não colocar nada ele preenche com espaço em branco, caso coloque algo, ele preenche com o que for colocado
# EX:
print (f'{variavel:$^10}.')