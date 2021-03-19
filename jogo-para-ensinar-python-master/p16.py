import run()
numero = float(input(' Digite um valor: '))
print(' O valor digitado foi {} ea sua porção inteira é {}'.format(numero,int(numero)))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p16
    p16.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
