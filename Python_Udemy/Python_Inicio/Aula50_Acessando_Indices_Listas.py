salas = [
    [1, "Joao", "Pedro"],
    [2, "Ana", "Maria", "Jose"],
    [3, "Antonio", (80, 90, 70)]
]

#Sintaxe basica = nome_lista [indice_lista][indice_objetivo]
#print(salas[0][0], salas[0][1])
#print(salas[1][2])
#print(salas[2][0], salas[2][1])

for sala in salas:
    print(f"A Sala é {sala}")
    for aluno in sala:
        print(aluno)
    print("-" * 10)