while True:
    print('======================================')
    print('=== BEM VINDO A FASE 17 DO MUNDO 3 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('78. maior e menor valores na lista \n79. valores unicos em uma lista \n80. lista ordenada sem repetiçoes')
    print('81. extraindo dados de uma lista \n82. dividindo valores em varias listas \n83. validando expressoes matematicas')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 78 a 83)?'))
    if opçao == 78:
        import p78
        p78.run()
    if opçao == 79:
        import p79
        p79.run()
    if opçao == 80:
        import p80
        p80.run()
    if opçao == 81:
        import p81
        p81.run()
    if opçao == 82:
        import p82
        p82.run()
    if opçao == 83:
        import p83
        p83.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 3 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo3
        mundo3.run()
    else:
        import menu
        menu.run()
