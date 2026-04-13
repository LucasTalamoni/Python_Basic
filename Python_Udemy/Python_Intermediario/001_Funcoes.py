# criando funções em python
# Explicando o conceito de empacotamento segundo a convenção

x, y, *resto = 1, 2, 3, 4
print(x, y, resto) # retorno = 1 2 [3, 4]

def soma(*args): # quando queremos passar um empacotamento, utilziamos a palavra "args"
    total = 0
    for numero in args:
        total += numero
    return total # IMPORTANTE: é importante a função retornar algo. PRINT dentro de função não é retorno, é somente exibição

soma_01 = soma(1, 2, 3, 4, 5, 6, 7, 8)
print(f"Soma = {soma_01}")

numeros = 1,3,4,5,6,7,8
outra_soma = soma(*numeros) # é necessário desempacotar a variavel numeros antes de enviar para o *args. Se não, estariamos enviando uma tupla
print(outra_soma)