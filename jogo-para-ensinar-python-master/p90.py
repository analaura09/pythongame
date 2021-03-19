aluno = dict()
aluno['nome']=input('nome:')
aluno['media']=float(input(f'media de {aluno["nome"]}:'))
if aluno['media'] >= 7:
    aluno['situaçao']='aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] ='reprovado'
print('-='*30)
for k,v in aluno.items():
    print(f'  - {k} é igual a {v}')
