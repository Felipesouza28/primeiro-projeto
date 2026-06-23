retaA = int(input("Digite o valor do Reta A: "))
retaB = int(input("Digite o valor do Reta B: "))
retaC = int(input("Digite o valor do Reta C: "))

if retaA + retaB < retaC or retaA + retaC < retaB or retaB + retaC < retaA:
    print("Triângulo Inválido")
else:
    if retaA == retaB == retaC:
        print("Esse triângulo é Equilátero")
    elif retaA == retaB or retaA == retaC or retaB == retaC:
        print("Esse triângulo é Isósceles")
    else:
        print("Esse triângulo é Escaleno")


