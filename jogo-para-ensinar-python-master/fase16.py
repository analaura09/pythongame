while True:
    print('======================================')
    print('=== BEM VINDO A FASE 16 DO MUNDO 3 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('72. numero por extenso \n73. tuplas com times \n74. maior e menor valores em tuplas')
    print('75. analise de dados em uma tupla \n76. lista de preços com tupla \n77. contando vogais em tupla')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 72 a 77)?'))
    if opçao == 72:
        import p72
        p72.run()
    if opçao == 73:
        import p73
        p73.run()
    if opçao == 74:
        import p74
        p74.run()
    if opçao == 75:
        import p75
        p75.run()
    if opçao == 76:
        import p76
        p76.run()
    if opçao == 77:
        import p77
        p77.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 3 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo3
        mundo3.run()
    else:
        import menu
        menu.run()
