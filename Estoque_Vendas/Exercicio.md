# 🏪 Exercício Avançado: Sistema de Estoque + Vendas

## 🎯 Descrição Completa do Problema

Crie um **sistema integrado** que gerencia **ESTOQUE** e processa **VENDAS** com:
- Estoque inicial de produtos (quantidade + preço unitário)
- Cliente escolhe produtos e quantidades
- **VERIFICAÇÃO** de estoque disponível
- **ATUALIZAÇÃO** automática do estoque
- Cálculo de **subtotal** (qtd × preço)
- **Desconto 15%** para compras > R$200
- Relatórios formatados profissionais

**Tópicos:** Dict aninhado, controle estoque, validações, funções, formatação avançada [file:24]

---

## 📋 Análise Lógica Completa

### **Entradas**
- Nome do produto (string)
- Quantidade desejada (int)
- Comando "fim" para encerrar


### **Processamento**
- Verificar produto no estoque
- Validar quantidade disponível
- Calcular subtotal (qtd × preço_unitário)
- Atualizar estoque (qtd -= vendida)
- Acumular total venda
- Aplicar desconto condicional


### **Saídas**
- Relatório de venda formatado
- Estoque atualizado
- Total com desconto

---

## 💻 Pseudocódigo Estruturado Completo

```pseudocode

INÍCIO

// 1. ESTOQUE INICIAL (dict aninhado)
estoque = {
    "arroz": {"preco": 12.90, "qtd": 50},
    "feijao": {"preco": 13.60, "qtd": 30},
    "carne": {"preco": 45.00, "qtd": 15},
    "leite":  {"preco":  4.50, "qtd": 100}
}

carrinho = {}  // {produto: {"qtd":2, "subtotal":25.80}}
total = 0.0

print("🏪 SISTEMA DE VENDAS")
print("=" * 50)
print("Digite 'fim' para encerrar venda")

// 2. LOOP PRINCIPAL DE VENDAS
ENQUANTO VERDADEIRO:
    nome = input("Produto: ").lower().strip()
    
    // SAÍDA RÁPIDA
    SE nome == "fim":
        print("✅ Finalizando venda...")
        QUEBRAR
    
    // 3. VERIFICAÇÃO DE ESTOQUE
    SE nome NAO em estoque:
        print(f"❌ {nome.title()} indisponível!")
        esperar_tecla()
        CONTINUAR
    
    // MOSTRAR ESTOQUE ATUAL
    qtd_disp = estoque[nome]["qtd"]
    preco_unit = estoque[nome]["preco"]
    print(f"📦 {nome.title()}: {qtd_disp} und | R${preco_unit:.2f}/und")
    
    // 4. CAPTURAR QUANTIDADE
    ENQUANTO VERDADEIRO:
        try:
            qtd = int(input("Quantidade: "))
            QUEBRAR
        except:
            print("❌ Digite número inteiro!")
    
    // 5. VALIDAR ESTOQUE SUFICIENTE
    SE qtd > qtd_disp:
        print(f"❌ Estoque insuficiente! Máx: {qtd_disp}")
        esperar_tecla()
        CONTINUAR
    
    // 6. VENDA APROVADA! 🎉
    subtotal = qtd * preco_unit
    carrinho[nome] = {"qtd": qtd, "subtotal": subtotal}
    total += subtotal
    
    // ATUALIZAR ESTOQUE
    estoque[nome]["qtd"] -= qtd
    
    print(f"✅ Vendido {qtd}x{xnome.title()}")
    print(f"   Subtotal: R${subtotal:.2f} | Total: R${total:.2f}")
    esperar_tecla()

// 7. FINALIZAR VENDA
limpar_tela()

SE total > 200:
    desconto = total * 0.15
    status = "🎁 15% DESCONTO"
SENÃO:
    desconto = 0
    status = "➡️ SEM DESCONTO"

total_final = total - desconto

// 8. RELATÓRIO
print("🏪 RELATÓRIO DE VENDA")
print("=" * 50)

print(f"{'PRODUTO':<15} {'QTD':>5} {'SUBTOTAL':>10}")
print("-" * 50)

para produto, dados em carrinho.items():
    print(f"{produto.title():<15} {dados['qtd']:>5} R${dados['subtotal']:>7.2f}")

print("-" * 50)
print(f"{'SUBTOTAL':<20} R${total:>7.2f}")
print(f"{'DESCONTO':<20} R${desconto:>7.2f}")
print(f"{status:<20}")
print("=" * 50)
print(f"TOTAL FINAL:       R${total_final:>7.2f}")

// 9. ESTOQUE FINAL (BONUS)
print("\n📊 ESTOQUE ATUALIZADO:")
para p, dados em estoque.items():
    if dados["qtd"] > 0:
        print(f"  {p.title()}: {dados['qtd']} und")

FIM
