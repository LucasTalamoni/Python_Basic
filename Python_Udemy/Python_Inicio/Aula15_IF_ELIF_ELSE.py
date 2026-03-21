# if = se
#elif = se não se
#else = se não
#Ao encontrar uma condição verdadeira, o interpretador sai 
#do bloco de condição, mesmo que a proxima condição tbm seja verdadeira

entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você entrou!!')
elif entrada == 'sair':
    print('Você saiu!!')
else:
    print('Você não digitou uma opção valida!!')