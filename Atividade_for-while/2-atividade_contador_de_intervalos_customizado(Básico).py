num1 = int(input("Digite o valor inicial: "))
num2 = int(input("Digite o valor final: "))
num3 = int(input("Digite o valor de intervalo: "))

if num3 == 0:
    print("O valor do intervalo não pode ser zero")
    
for i in range(num1, num2, num3):
    print(i)