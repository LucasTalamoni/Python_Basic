import os
import sys

def esperar_tecla(msg="Pressione qualquer tecla para continuar..."):
    print(msg, end="", flush=True)

    if os.name == "nt":
        import msvcrt
        msvcrt.getch()
        print()
    else:
        import tty
        import termios

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print()


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def comparar_qtd(nome, qtd_solicitada):
    qtd = estoque[nome].get("qtd")
    if qtd_solicitada <= qtd:
        return qtd_solicitada

    else:
        print("Quantidade no estoque insuficiente!")
        print(f"Quantidade atual: {qtd}")
        while True:
            try:
                novo_valor = int(input(f"Digite um valor menor ou igual a {qtd}: "))
            except ValueError:
                print("Digite apenas numeros inteiros!!")
                continue

            if novo_valor <= qtd:
                return novo_valor


#Definindo o estoque inicial
estoque = {
    "arroz": {"preco": 12.90, "qtd": 50},
    "feijao": {"preco": 13.60, "qtd": 30},
    "carne": {"preco": 45.00, "qtd": 15},
    "leite":  {"preco":  4.50, "qtd": 100}
}

carrinho = {}
total = 0

print("Vamos iniciar a compra!!")
print("=" * 50)
print("Digite 's' quando quiser encerrar!")

while True:
    nome = input("Digite o nome do produto: ").lower().strip()
    if nome == "s":
        print("Encerrando...")
        esperar_tecla()
        break

    if nome not in estoque:
        print("Produto não encontrado no estoque!!")
        continue

    if nome in estoque:
        while True:
            try:
                qtd_solicitada = int(input("Digite a quantidade desejada: "))
                qtd_solicitada = comparar_qtd(nome, qtd_solicitada)
                break
            except ValueError:
                print("Digite apenas números inteiros!!")

        preco_produto = estoque[nome].get("preco")
        subtotal_item = preco_produto * qtd_solicitada
        carrinho[nome] = {"qtd": qtd_solicitada, "preco": preco_produto, "Total": subtotal_item}
        total = total + subtotal_item

limpar_tela()

if total > 200:
    total_desconto = total * 0.15
    total_final = total - total_desconto
    status_desconto = "COM DESCONTO de 15%"
else:
    status_desconto = "SEM DESCONTO de 15%"
    total_desconto = 0
    total_final = total

print("Total da compra")
print("=" * 50)

for produto, dados in carrinho.items():
    print(f"{produto.title()}: {dados['qtd']} und × R${dados['preco']:.2f} = R${dados['Total']:.2f}")

print("=" * 50)

print(f"Total: {total:.2f}")
print(f"Status do desconto: {status_desconto}")
print(f"Total do desconto: {total_desconto:.2f}")
print(f"Total da compra: {total_final:.2f}")