#Compare Valores

First = int(input('Digite um Valor: '))
Second = int(input("Digite outro Valor: "))
#PS: Essa conversão de string para int usada acima não é recomendada pois pode gerar um erro caso o usuario digite uma letra
if First > Second:
    print(f'O valor {First} é maior que {Second}')
elif First == Second:
    print (f'O valor {First} é igual à {Second}')
elif First < Second:
    print(f'O valor {First} é menor que {Second}')
else:
    print('Deu tudo errado')