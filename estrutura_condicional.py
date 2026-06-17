# Casar ou Comprar uma Bicicleta ?

print(" Casar ou comprar uma Bicicleta ?")

resposta = input("Você está gordo ? sim/não: ")

if resposta == "sim":
    quer_emagrecer = input("Você quer emagrecer ? sim/não: ")
    if quer_emagrecer == "sim":
        print("Então Case!")
    else:
        print("Compre uma bicicleta!")
else:
    quer_engordar = input("Você quer engordar ? sim/não: ")
    if quer_engordar == "sim":
        print("Então Case!")
    else:
        print("Compre uma bicicleta!")