"""
Operadores de atribuição
= - Igual
+= - Soma
-= - Subtração
*= - Multiplicação
/= - Divisão
//= - Divisão com resultado inteiro, somente
**= - Potencia
%= - Módulo
"""
contador = 10
variavel = '1'
variavel_02 = 10

###

contador += 5
print(contador)
'''
Ele pega o valor da variavel e soma com valor 5
'''

variavel += '2'
print(variavel)
'''
Esse tipo de atribuição tbm serve para concatenar as strings, lembrando que quando está entre '', se torna uma 
string. O resultado dessa atribuição será 12
'''

variavel_02 *= '2'
print(variavel_02)
'''
Tbm é possivel fazer a repetição
O resultado desse comando será 2222222222
'''
