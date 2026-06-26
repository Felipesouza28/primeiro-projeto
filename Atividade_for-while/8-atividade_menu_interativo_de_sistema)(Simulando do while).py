import time

while True:
    opcao = int(input("""
    MENU
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    5 - Sair
    Digite sua opcao:
"""))
    if opcao == 1:
        print("Somar")
    elif opcao == 2:
        print("Subtrair")
    elif opcao == 3:
        print("Multiplicar")
    elif opcao == 4:
        print("Dividir")
    elif opcao == 5:
        print("Saindo..,")
        time.sleep(1)
    else:
        print("Opção inválida, escolha uma nova!")