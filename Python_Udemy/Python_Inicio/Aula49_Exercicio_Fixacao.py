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

pavras_formatadas = []
for i, palavra in palavras_separadas:
    