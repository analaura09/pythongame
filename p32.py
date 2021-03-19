def run():
    ano = int(input('Digite um ano: '))
    bissexto = ano % 4
    if bissexto == 0:
        print(' O ano {} é um ano bissexto!'.format(ano))
    else:
        print(' O ano {} é um ano nao bissexto'.format(ano))
    
    opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
    if opçao == 1:
        import p32
        p32.run()
    if opçao ==2:
        import mundo1
        mundo1.run()
    if opçao == 3:
        print('Obrigada por jogar! Volte sempre :)')