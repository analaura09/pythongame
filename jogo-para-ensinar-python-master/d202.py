import funcao
print(" Exercício 202")

alunos=int(input("Digite a quantidade de alunos: "))
turmas=int(input("Digite a quantidade de turmas: "))

mediat=(funcao.media(alunos, turmas))
if mediat <= 40:
    print (f"A média por turma é igual a {mediat}")
else:
    print ("As turmas têm mais de 40 alunos.")
