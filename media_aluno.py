nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3) / 3


if media >= 7:
    print(f"Aluno(a) aprovado(a) com média {media: .2f} " )
elif media >= 3 and media <7:
    print(f"Aluno(a) em Recuperação com média {media: .2f}")
    fez_recuperacao = input("Aluno(a) fez a recuperação? sim/não: ")
    if fez_recuperacao == "sim":
        nota_recuperacao = float(input("Digite a nota da sua recuperação: "))
        if nota_recuperacao >= 5:
            print("Aluno(a) aprovado pela recuperação")
        else:
            print("Ãluno não obteve nota suficiente para ser aprovado após a recuperação")
    else:
        print("Sem chance de nova recuperação!")
else:
    print(f"Aluno(a) reprovado(a) com média {media: .2f}")
