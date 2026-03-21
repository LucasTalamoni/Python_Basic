"""
Flag(Bandeira) = Marcar um local
None = Não valor
Is e Is not = É ou não é (Tipo, Valor, identidade)
"""

condicao = False
passou_no_if = None # O None serve para 'setar' um valor vazio na variavel

if condicao:
    passou_no_if = True
    print('Faça Algo')
else:
    print('Não faça algo')

if passou_no_if is None: # 'is' é a mesma coisa que '=='
    print('Não passou no if')
else:
    print('Passou no if')