while True:
    print('======================================')
    print('=== BEM VINDO A FASE 21 DO MUNDO 3 ===')
    print('=== OS DESAFIOS DESSE MUNDO SAO ===')
    print('101. funçoes para votaçao \n102. funçao para fatorial')
    print('103. ficha do jogador \n104. validando entrada de dados em python')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 101 a 106)?'))
    if opçao == 101:
        import p101
        p101.run()
    if opçao == 102:
        import p102
        p102.run()
    if opçao == 103:
        import p103
        p103.run()
    if opçao == 104:
        import p104
        p104.run()
    if opçao == 105:
        import p105
        p105.run()
    if opçao == 106:
        import p106
        p106.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 3 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo3
        mundo3.run()
    else:
        import menu
        menu.run()
