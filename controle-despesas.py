# controle_despesas.py
despesas = {}
print("Bem-vindo ao Controle de Despesas")
while True:
    categoria = input("Digite a categoria (ou 'sair' para encerrar): ")
    if categoria.lower() == 'sair':
        break
    valor = float(input(f"Digite o valor para {categoria}: "))
    despesas[categoria] = despesas.get(categoria, 0) + valor
# controle_despesas.py (continuado)
total = sum(despesas.values())
print("\nRelatório de Despesas:")
for categoria, valor in despesas.items():
    print(f"{categoria}: R${valor:.2f}")
print(f"Total: R${total:.2f}")
