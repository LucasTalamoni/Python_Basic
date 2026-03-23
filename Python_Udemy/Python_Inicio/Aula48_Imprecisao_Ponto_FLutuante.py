valor_01 = 0.1
valor_02 = 0.7

total = valor_01 + valor_02

print(total) # 0.7999999999
print(f"Total: {total:.2f}") # 0.80
print(f"Total: {round(total, 2)}") # round(variavel, Numero_casas) OBS: Ignora os zeros

# Se for realmente necessário trabalhar com números de pontos flutuantes, procure sobre o módulo chamado "decimal"