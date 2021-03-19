while True:
    print('======================================')
    print('=== BEM VINDO A FASE 15 DO MUNDO 2 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('66. varios numeros com flag \n67. tabuada V3.0 \n68. jogo do par ou impar')
    print('69. analise de dados do grupo \n70. estatisticas em produtos \n71. simulador de caixa eletronico')
    opçao = int(input('qual desafio voce esolhe(digite um numero de 66 a 71)?'))
    if opçao == 66:
        import p66
        p66.run()
    if opçao == 67:
        import p67
        p67.run()
    if opçao == 68:
        import p68
        p68.run()
    if opçao == 69:
        import p69
        p69.run()
    if opçao == 70:
        import p70
        p70.run()
    if opçao == 71:
        import p71
        p71.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 2 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo2
        mundo2.run()
    else:
        import menu
        menu.run()
