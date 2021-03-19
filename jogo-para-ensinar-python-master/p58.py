from random import randint
pc = randint(0,10)
print('sou seu computador... acabei de pensar em um numero entre 0 e 10')
print('sera que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual é seu palpite?'))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('mais... tente mais uma vez')
        elif jogador > pc:
            print('menos... tente mais uma vez')
print('acertou com {} tentativas. parabens!'.format(palpites))
