import run()
from random import choice
aluno1 = str(input(' Digite o nome de um aluno: '))
aluno2 = str(input(' Digite o nome de um aluno: '))
aluno3 = str(input(' Digite o nome de um aluno: '))
aluno4 = str(input(' Digite o nome de um aluno: '))
list = [aluno1, aluno2, aluno3, aluno4]
escolha = choice(list)
print(' O aluno escolhido foi {}'.format(escolha))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p19
    p19.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
