# High Order Function (HOF) é uma função que recebe uma ou mais funções como argumento, ou retorna uma função como resultado.
# Exemplo: map(), filter(), sorted() em Python são HOFs porque recebem uma função como argumento

def saudacao(msg, nome):
    return f"{msg}, {nome}"

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, "Olá", "Lucas!")) # 'saudacao' é passada como a função, e "Olá", "Lucas!" são empacotados em '*args'. Dentro de 'executa', '*args' é desempacotado para 'saudacao'.