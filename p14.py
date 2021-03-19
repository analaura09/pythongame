import run()
celsius = float(input(' Informe a temperatura em celsius: '))
fareheid = 9 * celsius / 5 + 32
print(' A temperatura de {}ºC corresponde a {}ºF'.format(celsius, fareheid))
opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p14
    p14.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
