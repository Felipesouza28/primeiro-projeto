import random

velocidade = random.randint(60,120)
print(f"Sua velocidade é {velocidade}")
# radar = int(input("Digite a velocidade: "))

if velocidade <= 80:
    print("Boa viagem, dirija com segurança!")
else:
    print("Se atente ao limite de velocidade!")