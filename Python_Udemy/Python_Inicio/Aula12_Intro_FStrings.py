nome = 'Lucas Talamoni'
altura = 1.82
peso = 78
imc = peso / altura ** 2

"f-strings" # Isso é uma formatação de strings (Basicamente ele cria um padrão de resposta)
# A forma correta de escrever é: f'{variavel}' restante da frase {variavel} resto da frase
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Lucas Talamoni tem 1.82 de altura,
# pesa 78 quilos e seu IMC é
# 23.54788069073783