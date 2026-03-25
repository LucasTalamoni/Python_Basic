Tupla = "Tupla", "Lista", "Dicionario"
string = "Python 123"
lista = ["Arroz", "Feijao", 123, "maria", "Tres"]
salas = [
    [1, "Joao", "Pedro"],
    [2, "Ana", "Maria", "Jose"],
    [3, "Antonio", (80, 90, 70)]
]

p, *_, u = lista
#print(p, u)

print(*lista)
print(lista)
print(Tupla)
print(*Tupla)

print(*salas)
print(*salas, sep='\n')