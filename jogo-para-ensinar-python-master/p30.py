def run()
numero = int(input('Digite um numero: '))
par = numero % 2
if par == 0  :
    print('o numero {} é um numero par!'.format(numero))
else:
    print('o numero {} é um numero impar!'.format(numero))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p30
    p30.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')