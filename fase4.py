while True:
    print('=====================================')
    print('=== BEM VINDO A FASE 4 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSE MUNDO SAO ===')
    print('1. Deixando tudo pronto \n2. Resposta ao usuario')
    opçao = int(input('qual desafio você escolhe(digite o numero 1 ou 2)?'))
    if opçao == 1:
        import p1
        p1.run()
    else:
        import p2
        p2.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 1 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo1
        mundo1.run()
    else:
        import menu
        menu.run()
