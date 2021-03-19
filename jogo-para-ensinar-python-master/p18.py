import run()
import math
angulo = float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(angulo))
print("O angulo de {} tem seno de {:.2f}".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print("O angulo de {} tem cosseno de {:2f}".format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:2f}'.format(angulo,tangente))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p18
    p18.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
