import run()
def fatorial(num, show=False):
    f = 1
    for c in range(num,0,-1):
        if show:
            print(c,end='')
        if c > 1:
            print(' x ' , end='')
        else:
            print(' = ', end ='')
        f *= c
    return f
print(fatorial(5,show=True))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo3? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p102
    p102.run()
if opçao ==2:
    import mundo3
    mundo3.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')

