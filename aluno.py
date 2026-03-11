aluno = {}

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))

aluno["nome"] = nome
aluno["nota1"] = nota1
aluno["nota2"] = nota2

media = (nota1 + nota2) / 2
aluno["media"] = media

print("Dados do aluno:")
print(aluno)

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")