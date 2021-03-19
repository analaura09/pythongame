from random import randint
opçao = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
print('''suas opcoes:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input(' Qual a sua jogada?'))
print('*=-'*11)
print('computador jogou {}'.format(opçao[pc]))
print('o jogador jogou {}'.format(opçao[jogador]))
print('*=-'*11)
if pc == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')

elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
         print('JOGADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')
elif pc == 2:
    if jogador == 0:
         print('JOGADOR VENCE!')
    elif jogado == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')
        
