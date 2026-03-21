"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Luiz'  # iterável

iteratador = iter(texto)  # iterator

while True:
     try:
         letra = next(iteratador)
         print(letra)
     except StopIteration: #StopIteration é a sinalização que o python passa quando não encontram mais valores na variavel
         break

# O código a cima é a mesma coisa que isso:
#for letra in texto:
 #   print(letra)