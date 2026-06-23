salario = float(input("Digite seu salário bruto: "))

parcela = float(input("Valor que deseja pagar na parcela: "))

credito = salario * 0.30

if parcela <= credito:
    print("Crédito Aprovado")
else:
    print("Crédito Recusado")