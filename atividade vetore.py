import time

lista_de_compras = ["Arroz", "Feijão", "Carne", "Biscoito", "Café"]
itens_comprados = []

print("Lista de compras:")

for i in lista_de_compras:
    time.sleep(0.5)
    print(i)

while lista_de_compras:
    compras = input("Digite o item que pegou agora: ").strip().capitalize()
    if compras in lista_de_compras:
        print(f"Você pode riscar {compras} da sua lista!")
        lista_de_compras.remove(compras)
        print(f"Falta pegar {len(lista_de_compras)} itens")
        itens_comprados.append(compras)
    elif compras in itens_comprados:
        print(f"Você já pegou esse item")
    else:
        print("Esse item não existe na sua lista!")
print("Parabéns! Você terminou todas as compras!")