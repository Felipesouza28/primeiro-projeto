import random
numero_secreto = random.randint(1, 20)

while numero_secreto:
    num = int(input("Adivinhe o número que estou pensando: "))
    if num < numero_secreto:
        print("Muito baixo, tente outro!")
    elif num > numero_secreto:
        print("Muito alto, tente outro!")
    else:
        print(("Parabéns, você acertou!"))
        break