# Exercício Prático Integrado - Caixa de Supermercado

## Descrição do Problema

Crie um programa interativo para simular um **caixa de supermercado simples**. O usuário cadastra produtos (nome e preço), calcula o total da compra, aplica **desconto de 10% se o total ultrapassar R$100** e exibe o resultado final.

**Tópicos integrados dos arquivos estudados:**
- Variáveis, entrada/saída, strings (Cap04)
- Listas, dicionários, loops, condicionais (Cap04/Cap06) 
- Manipulação strings, operadores aritméticos (Cap04)

---

## 🎯 Análise Completa do Problema

### **Entradas**
- Nomes dos produtos (string)
- Preços dos produtos (float) 
- Decisão de continuar adicionando ("sim/não")

### **Processamento**
1. Armazenar múltiplos produtos dinamicamente
2. Somar preços continuamente
3. Verificar condição de desconto (> R$100)
4. Calcular total final

### **Saídas**
- Lista formatada dos produtos comprados
- Total com/sem desconto
- Mensagem final formatada

---

## 🧠 Quebra em Partes Menores (Pensamento Lógico)

**Pergunte-se antes de programar:**
1. **Como coletar produtos sem saber a quantidade?** → Loop `while` com parada por input
2. **Onde armazenar nome+preço?** → Lista de dicionários
3. **Como somar dinamicamente?** → `total = 0` + somar em cada iteração
4. **Como aplicar desconto?** → `if total > 100: total *= 0.9`
5. **Como exibir bonito?** → f-strings + loop `for` para listar itens

---

## 💻 Pseudocódigo Estruturado Completo

```pseudocode
INÍCIO
    // Inicializações
    carrinho = {}  // Lista vazia de dicionários
    total = 0.0
    adicionarMais = "sim"
    
    // Loop principal de cadastro (while com condição dinâmica)
    ENQUANTO adicionarMais == "sim":
        nomeProduto = ENTRADA("Nome do produto: ").lower().strip()
        precoProduto = float(ENTRADA("Preço (R$): "))
        
        // Armazenar produto como dicionário e somar total
        carrinho.adicionar({"nome": preco, "nome": preco})
        total = total + preco
        
        // Perguntar se continua (normaliza input)
        adicionarMais = ENTRADA("Adicionar mais? (sim/não): ").lower().strip()
    
    // Lógica de desconto condicional (if/else)
    SE total > 100:
        desconto = total * 0.10  // 10%
        totalFinal = total - desconto
        statusDesconto = "✅ COM DESCONTO de 10%"
    SENÃO:
        totalFinal = total
        statusDesconto = "➡️ SEM DESCONTO"
    
    // Exibição formatada (for + f-strings)
    ESCREVER("🛒 CARRINHO DE COMPRAS")
    ESCREVER("=" * 40)
    
    PARA cada item em carrinho:
        ESCREVER(f"- {item['nome'].title()}: R$ {item['preco']:.2f}")
    
    ESCREVER("=" * 40)
    ESCREVER(f"Total: R$ {total:.2f}")
    ESCREVER(f"{statusDesconto}")
    ESCREVER(f"💰 TOTAL FINAL: R$ {totalFinal:.2f}")
    
FIM
