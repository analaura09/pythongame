import run()

real = float(input(' Quanto dinheiro voce tem? '))
dolar = real/ 3.27
print(' Com R${} voce pode comprar U${}'.format(real,dolar))
opçao = int(input('deseja repetir esse exercicio[1] \ndeseja voltar para o mundo 1[2] \ndeseja sair do jogo[3]'))
if opçao == 1:
    import p10
    p10.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')

