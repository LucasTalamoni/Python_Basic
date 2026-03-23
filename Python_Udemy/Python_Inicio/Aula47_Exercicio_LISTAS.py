"""
Faça uma lista de compras
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de indices
inexistentes
"""

lista_compras = []

while True:
    print("Digite uma opção \ni = Inserir \ns = Sair \nl = Listar \na = apagar")
    opcao = input("Digite: ")

    if opcao == "s":
        print("Saindo..")
        break
    elif opcao == "l":
        lista_compras_enumeradas = enumerate(lista_compras)
        print(next(lista_compras_enumeradas))
    elif opcao == "i":
        inserir = input("Digite o item para inserir: ")
        lista_compras.append(inserir)
    elif opcao == "a":
        try:
            indice_apagar = int(input("Digite o NÚMERO do item que quer apagar: "))
            # Verifica se o índice é válido antes de tentar apagar
            # "pop" remove os valores com base no indice
            # "remove" remove os valores com base no conteudo da variavel
            if 0 <= indice_apagar < len(lista_compras):
                item_removido = lista_compras.pop(indice_apagar)
                print(f"Item '{item_removido}' removido com sucesso!")
            else:
                print("Índice inválido. Não há item nessa posição.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o índice.")
        except IndexError:
            # Embora o 'if' acima já trate isso, é bom ter o except para robustez
            print("Índice inválido. Não há item nessa posição.")
    else:
        print("Opção invalida!!")