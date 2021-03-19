import run()
from random import randint
from time import sleep
def sorteia(lista):
    print('sorteando 5 valores da lista:',end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='',flush = True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares de {lista}, temos {soma}')

num = list()
sorteia(num)
somaPar(num)

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo3? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p100
    p100.run()
if opçao ==2:
    import mundo3
    mundo3.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')

