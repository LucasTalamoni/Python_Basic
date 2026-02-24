import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

carrinho = {}
total = 0.0
sair = "nao"

print("Vamos iniciar a contagem dos produtos!")
print("=" * 40)

while sair != "sim":
    nome = input("Digite o nome do produto: ").lower().strip()
    
    while True:
        try:
            preco = float(input("Digite o preço: "))
            break
        except ValueError:
            print("Digite apenas números!!")

    carrinho[nome] = preco
    total += preco
    
    sair = input("Deseja sair? \nDigite: ").lower().strip()
    limpar_tela()
    
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
print(f"Total da compra: {total_final:.2f}")
print(f"Status do desconto: {status_desconto}")
print(f"Total de desconto: {desconto:.2f}")