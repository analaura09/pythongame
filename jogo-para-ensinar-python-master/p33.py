def run()
    n1 = int(input(' Digite um valor: '))
    n2 = int(input(' Digite outro valor: '))
    n3 = int(input(' Digite outro valor: '))
    list=[n1,n2,n3]
    print(list)
    print('o maior numero é {} e o menor numero é {}'.format(list[2], list[0]))
    
    opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
    if opçao == 1:
        import p33
        p33.run()
    if opçao ==2:
        import mundo1
        mundo1.run()
    if opçao == 3:
        print('Obrigada por jogar! Volte sempre :)')