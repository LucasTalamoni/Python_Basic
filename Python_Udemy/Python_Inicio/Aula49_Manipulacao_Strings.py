palavras = "Uma frase cheia de plavras, apenas"

lista_palavras = palavras.split() # Divide a frase em palavras e cria uma lista
lista_frase = palavras.split(",") # Ao passar um argumento, ele irá dividir a frase quando encotrar esse argumento
#print(lista_palavras)
#print(lista_frase)

lista_frases_fixed = []

for i, frase in enumerate(lista_frase):
    lista_frases_fixed.append(lista_frase[i].strip())

frases_unidas = ', '.join(lista_frases_fixed) # join trabalha somente com iteraveis. Serve para unir strings
print(frases_unidas)