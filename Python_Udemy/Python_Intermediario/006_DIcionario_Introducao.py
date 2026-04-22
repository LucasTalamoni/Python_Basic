pessoa = {
    'nome': 'Joao',
    'sobrenome': 'Chaves',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for qualquer_coisa in pessoa:
    print(qualquer_coisa, pessoa[qualquer_coisa])
# O valor da chave em um dicionario, é como se fosse um indice para uma lista