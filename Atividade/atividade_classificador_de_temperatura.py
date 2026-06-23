import random

temperatura = random.randint(0,40)
print(f"Quantos °C está lá fora? {temperatura}")

if temperatura < 15:
    print("Clima Frio, pegue seu casaco")

elif temperatura <= 25:
        print("Clima Agradável")
else:
    print("Clima Quente")