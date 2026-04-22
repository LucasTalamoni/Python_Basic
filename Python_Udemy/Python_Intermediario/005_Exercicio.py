# Crie funções que duplicam, triplicam e quadriplicam o numero recebido como parametro

def multiplicador(multiplicador):
    def multiplicar(number):
        return multiplicador * number
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

for numeros in [2,5]:
    print(f"Duplicar {numeros} = {duplicar(numeros)}")
    print(f"Triplicar {numeros} = {triplicar(numeros)}")
    print(f"Quadruplicar {numeros} = {quadruplicar(numeros)}")