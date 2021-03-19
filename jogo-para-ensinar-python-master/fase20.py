while True:
    print('======================================')
    print('=== BEM VINDO A FASE 20 DO MUNDO 3 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('96. funçao que calcula a area \n97. um print especial \n98. funçao de contador')
    print('99. funçao que descobre o maior \n100. funçoes para sortear e somar')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 96 a 100)?'))
    if opçao == 96:
        import p96
        p96.run()
    if opçao == 97:
        import p97
        p97.run()
    if opçao == 98:
        import p98
        p98.run()
    if opçao == 99:
        import p99
        p99.run()
    if opçao == 100:
        import p100
        p100.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 3 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo3
        mundo3.run()
    else:
        import menu
        menu.run()
