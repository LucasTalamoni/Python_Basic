#Essa função serve para coletar dados do usuario
#Sem uma variavel para armazenar, ela não serve para nada
#Ela só passa informação no tipo String
#Se precisar realizar contas, tera de fazer conversão
nome = input('Qual seu nome? ')
print(nome)
print(f'O seu nome é: {nome}')

numero_1 = input('Digite um número:')
numero_2 = input('Digite outro número: ')
print(f'A soma dos números é: {numero_1 + numero_2}')
#Ao executar esse print, o resultado será a concatenação (Grudar um no outro) dos dois numeros
#Isso acontece pq o input coletou 2 strings e não dois números
