while True:
    print('=====================================')
    print('=== BEM VINDO A FASE 8 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('16. quebrando um numero \n17. catetos e hipotenusa \n18. seno, cosseno e tangente')
    print('19. sorteando um item da lista \n20. sorteando uma ordem \n21. tocando um MP3 ')
    opçao = int(input('Qual desafio você escolhe(digite um numero de 16 a 21)?'))
    if opçao == 16:
        import p16
        p16.run()
    if opçao == 17:
        import p17
        p17.run()
    if opçao == 18:
        import p18
        p18.run()
    if opçao == 19:
        import p19
        p19.run()
    if opçao == 20:
        import p20
        p20.run()
    if opçao == 21:
        import p21
        p21.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 1 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo1
        mundo1.run()
    else:
        import menu
        menu.run()
