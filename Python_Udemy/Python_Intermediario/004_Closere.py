# Closure (Fechamento) em Python
# Um closure é uma função aninhada (interna) que se "lembra" e tem acesso a variáveis
# do escopo de sua função externa (envolvente), mesmo depois que a função externa
# já terminou sua execução.
#
# Em outras palavras, quando uma função interna é definida dentro de outra função
# e a função interna faz referência a uma variável do escopo da função externa,
# essa função interna, juntamente com o ambiente em que foi criada (incluindo
# as variáveis do escopo externo), forma um closure.

# Exemplo prático:
def criar_saudacao(saudacao):  # Esta é a função externa. 'saudacao' é uma variável do seu escopo.
    # A função interna 'saudar' é definida aqui.
    def saudar(nome):  # 'saudar' faz referência à variável 'saudacao' da função externa.
        return f"{saudacao}, {nome}!" # 'saudacao' é "fechada" dentro desta função.
    return saudar  # A função externa retorna a função interna 'saudar'.
                   # Neste ponto, 'criar_saudacao' termina, mas 'saudar' "lembra" o valor de 'saudacao'.

# Criamos duas instâncias de 'saudar', cada uma com um valor diferente para 'saudacao'.
# 'falar_bom_dia' é uma função que "lembra" que sua saudação é "Bom dia".
falar_bom_dia = criar_saudacao("Bom dia")
# 'falar_boa_noite' é outra função que "lembra" que sua saudação é "Boa Noite".
falar_boa_noite = criar_saudacao("Boa Noite")

# Agora podemos usar essas funções "pré-configuradas".
for nome in ["Maria", "Joao", "Tereza"]:
    # Cada chamada a 'falar_bom_dia' usa o 'saudacao' que foi fechado nela ("Bom dia").
    print(falar_bom_dia(nome))
    # Cada chamada a 'falar_boa_noite' usa o 'saudacao' que foi fechado nela ("Boa Noite").
    print(falar_boa_noite(nome))