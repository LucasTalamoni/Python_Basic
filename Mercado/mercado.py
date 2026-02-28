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

carrinho = {}
total = 0.0

print("Vamos iniciar a contagem dos produtos!")
print("=" * 40)
print("Digite 'S' para encerrar!")

while True:
    nome = input("Digite o nome do produto: ").lower().strip()
    if nome == "s":
        print("Encerrando...")
        esperar_tecla()
        break
    
    while True:
        try:
            preco = float(input("Digite o preço: "))
            break
        except ValueError:
            print("Digite apenas números!!")

    carrinho[nome] = preco
    total += preco
    
limpar_tela()

if total > 100:
    desconto = total * 0.10
    total_final = total - desconto
    status_desconto = "COM DESCONTO"
else:
    total_final = total
    desconto = 0
    status_desconto = "SEM DESCONTO"

print("CARRINHO DE COMPRAS")
print("=" * 40)

for nome, preco in carrinho.items():
    print(f"PRODUTO: {nome}  PREÇO: {preco:.2f}")

print("="*40)
print(f"Total da compra: {total:.2f}")
print(f"Status do desconto: {status_desconto}")
print(f"Total de desconto: {desconto:.2f}")
print(f"Total da compra com desconto: {total_final:.2f}")