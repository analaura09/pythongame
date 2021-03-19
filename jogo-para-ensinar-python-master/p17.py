import run()
from math import hypot
catetop = float(input(' Digite o comprimento do cateto oposto: '))
catetoa = float(input(' Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(catetop, catetoa)
print(' A hipotenusa vai medit {:,2f}'.format(hipotenusa))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p17
    p17.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
