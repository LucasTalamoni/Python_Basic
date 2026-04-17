# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.
# Mostre se o número é par ou impar

def mult_numeros (*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def verifica_paridade (*args):
    for n in args:
        if n % 2 == 0:
            return print(f"{n} é Par")
        
    return print(f"{n} é Impar")


numeros = 1,2,3,4,5,6
passando_numeros = mult_numeros(*numeros)
print(f"Primeira forma de passar os argumentos {passando_numeros}")

numeros_diretos = mult_numeros(1,2,3,4,5,6)
print(f"Segunda forma de passar os argumentos {numeros_diretos}")

#print("Multiplicando direto para comprar resultado: ", 1*2*3*4*5*6)

for numero in numeros:
    verifica_paridade(numero)