"""
O Problema
Você recebe a seguinte string (entrada):
"  Eletrônicos  ;  Cozinha ; Games  ; Periféricos  "

Sua missão é transformar essa bagunça em uma frase organizada e bonita para exibir no site (saída):
"Categorias disponíveis: Eletrônicos > Cozinha > Games > Periféricos"
"""

palavras = "  Eletrônicos  ;  Cozinha ; Games  ; Periféricos  "

palavras_separadas = palavras.split(";")
#print(type(palavras_separadas))

palavras_formatadas = []

for i, palavra in enumerate(palavras_separadas):
    palavras_formatadas.append(palavras_separadas[i].strip())
    #palavras_formatadas.append(palavra.strip()) OBS: É a mesma coisa

#print(palavras_formatadas)

palavras_unidas = ' > '.join(palavras_formatadas)

print(palavras_unidas)