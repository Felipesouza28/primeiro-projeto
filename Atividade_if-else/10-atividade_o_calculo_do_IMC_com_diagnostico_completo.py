peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC <= 24.9:
    print("Peso ideal (parabéns)")
elif IMC <= 29.9:
    print("Levemente acima do peso")
elif IMC <= 34.9:
    print("Obesidade Grau I")
else:
    print("Obesidade Severa/Mórbida")