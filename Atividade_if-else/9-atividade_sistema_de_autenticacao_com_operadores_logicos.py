usuario = input("Digite seu usuario: ")
password = int(input("Digite sua senha: "))

login = 'admin'
senha = 9988

if usuario == login and password == senha:
    print("Usuário válido")
else:
    print("Dados de acesso inválidos")