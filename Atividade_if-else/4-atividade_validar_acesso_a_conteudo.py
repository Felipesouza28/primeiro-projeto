idade = int(input("Digite o ano de nascimento: "))

anos = 2026 - idade

if anos >= 16:
    print("Acesso ao filme está liberado!")
else:
    print("Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos.")

