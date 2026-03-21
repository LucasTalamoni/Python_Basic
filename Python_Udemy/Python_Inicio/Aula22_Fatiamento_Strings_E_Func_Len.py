"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'
print(f'{variavel[0:5]} -  do 0 até 4') # Vai mostrar do indice 0 até o 4
print(f'{variavel[:5]} - do 0 té 4') # Vai mostrar do indice 0 até o 4
print(f'{variavel[4:]} - do 5 até o final') # Vai mostrar do indice 5 até o final
print (variavel[0:9:2]) # 0 - onde é o inicio, 9 - quantidade de caracteres, 2 - é de quanto em quanto pula
print(variavel[::-1]) # Inverte a frase

print(f'{len(variavel)} - Função len') # len retorna a quantidade de caracteres da string
