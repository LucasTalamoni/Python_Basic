"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
#cpf_input_str = ''

while True:
    cpf_input_str = input("Digite seu CPF (apenas números, 11 dígitos): ")

    # 1. Verifica se a entrada contém apenas dígitos
    if not cpf_input_str.isdigit():
        print("Erro: O CPF deve conter apenas números.")
        continue # Volta para o início do loop para pedir a entrada novamente

    # 2. Verifica se a entrada tem exatamente 11 dígitos
    if len(cpf_input_str) != 11:
        print("Erro: O CPF deve ter exatamente 11 dígitos.")
        continue # Volta para o início do loop para pedir a entrada novamente

    try:
        cpf = int(cpf_input_str)
    except ValueError:
        print("Erro de conversão")
        continue

    break

soma_cpf = 0
c = 10
for i, j in enumerate(cpf_input_str):
