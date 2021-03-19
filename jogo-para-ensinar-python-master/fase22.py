while True:
    print('======================================')
    print('=== BEM VINDO A FASE 22 DO MUNDO 3 ===')
    print('=== OS DESAFIOS DESSE MUNDO SAO ===')
    print('107. Exercitando módulos em Python \n108. Formatando Moedas em Python')
    print('109. Formatando Moedas em Python \n110. Formaatando Moedas em Python')
    print('111. Transformando módulos em pacotes \n112. Entrada de dados monetários')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 107 a 112)?'))
    if opçao == 107:
        import p107
        p107.run()
    if opçao == 108:
        import p108
        p108.run()
    if opçao == 109:
        import p109
        p109.run()
    if opçao == 110:
        import p110
        p110.run()
    if opçao == 111:
        import p111
        p111.run()
    if opçao == 112:
        import p112
        p112.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 3 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo3
        mundo3.run()
    else:
        import menu
        menu.run()
