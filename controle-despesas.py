# controle_despesas.py
despesas = {}
print("Bem-vindo ao Controle de Despesas")
while True:
    categoria = input("Digite a categoria (ou 'sair' para encerrar): ")
    if categoria.lower() == 'sair':
        break
    valor = float(input(f"Digite o valor para {categoria}: "))
    despesas[categoria] = despesas.get(categoria, 0) + valor
