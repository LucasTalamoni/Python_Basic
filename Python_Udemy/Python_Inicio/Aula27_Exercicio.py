"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um numero inteiro: ')

try:
    num_int = int(num) #Conversão de str para inteiro
    par_impar = num_int % 2 == 0 #Calculo para ver se é par ou impar
    par_impar_texto = None #Variavel para armazenar o texto de par ou impar
    
    if par_impar: #aqui ele já esta retornando um valor booleano, então não é preciso verificar novamente
        par_impar_texto = 'Par'
    else:
        par_impar_texto = 'Impar'
    
    print(f'O número {num_int} é {par_impar_texto}')

except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a Hora: ')

try:
    hora_int = int (hora)
    if hora_int >= 0 and hora_int <= 11:
        print ('Bom Dia')
    elif hora_int >= 12 and hora_int <= 17:
        print ('Boa Tarde')
    elif hora_int >= 18 and hora_int <=23:
        print ('Boa noite')
    else:
        print('Não conheço essa hora')
except:
   print('Você não digitou números válidos')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print ('Seu nome é curto')
    elif tamanho_nome >=5 and tamanho_nome <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Digite mais de uma letra')