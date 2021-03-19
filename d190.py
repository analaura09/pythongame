print ("Exercício 190")

alunos=int(input("Digite a quantidade de alunos: "))
turmas=int(input("Digite a quantidade de turmas: "))

media=(alunos/turmas)

if media <= 40:
    print (f"Por média as turmas terão {media} alunos")
else:
    print ("A turma tem mais de 40 alunos.")
