compras = float(input("Digite o valor total da sua compra: "))

desconto1 = compras * 0.05
desconto2 = compras * 0.1
desconto3 = compras * 0.15

if compras <= 100:
    print("Você não teve desconto")
elif compras <= 300:
    print(f"Total da sua compra foi de {compras}, e seu desconto foi de {compras - desconto1}")
elif compras <= 500:
    print(f"Total da sua compra foi de {compras}, e seu desconto foi de {compras - desconto2}")
else:
    print(f"Total da sua compra foi de {compras}, e seu desconto foi de {compras - desconto3}")
