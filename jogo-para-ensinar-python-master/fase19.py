while True:
    print('======================================')
    print('=== BEM VINDO A FASE 19 DO MUNDO 3 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('90. dicionario em python \n91. jogo de dados em python \n92. cadastro de trabalhador em python')
    print('93. cadastro de jogador de futebol \n94. unindo dicionarios e listas')
    print('95. aprimorando os dicionarios')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 90 a 95)?'))
    if opçao == 90:
        import p90
        p90.run()
    if opçao == 91:
        import p91
        p91.run()
    if opçao == 92:
        import p92
        p92.run()
    if opçao == 93:
        import p93
        p93.run()
    if opçao == 94:
        import p94
        p94.run()
    if opçao == 95:
        import p95
        p95.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 3 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo3
        mundo3.run()
    else:
        import menu
        menu.run()
