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

#---------------------- Verificação Primeiro digitio ---------------------------------------------

cpf_nove_digito = cpf_input_str[:9]
contador_1 = 10
resultado_1 = 0
for i in cpf_nove_digito:
    resultado_1 += (int(i) * contador_1)
    contador_1 -= 1

digito_validador_1 = ((resultado_1 * 10) % 11)
digito_validador_1 = digito_validador_1 if digito_validador_1 < 10 else 0

#------------------------ Fim verificação primeiro digito ---------------------------------------

#------------------------ Verificação Segundo digito --------------------------------------------

cpf_dez_digito = cpf_nove_digito + str(digito_validador_1)
contador_2 = 11
resultado_2 = 0

for i in cpf_dez_digito:
    resultado_2 += (int(i) * contador_2)
    contador_2 -= 1

digito_validador_2 = ((resultado_2 * 10) % 11)
digito_validador_2 = digito_validador_2 if digito_validador_2 < 10 else 0

#------------------------ Fim verificação primeiro digito ---------------------------------------

cpf_gerado_calculo = f'{cpf_nove_digito}{digito_validador_1}{digito_validador_2}'

if cpf_gerado_calculo == cpf_input_str:
    print(f"O CPF: {cpf} é válido")
else:
    print(f"O CPF {cpf} não é válido!!")