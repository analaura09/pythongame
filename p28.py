import run()
from random import randint
from time import sleep
pc = randint(0,5)
print('-=-'*20)
print('vou pensar em um numero entre 0 e 5, tente adivinhar!')
print('-=-'*20)
player = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(5)
if player == pc:
    print('PARABÉNS VOCE CONSEGUIU ME VENCER!')
else:
    print('GAME OVER! VOCE PERDEU, TENTE DE NOVO!')

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p28
    p28.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
