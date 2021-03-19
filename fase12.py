while True:
    print('======================================')
    print('=== BEM VINDO A FASE 12 DO MUNDO 2 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('36. aprovando emprestimos \n37. conversor de bases numeriocas \n38. comparando numeros')
    print('39. alistamento militar \n40. aquele classio da media \n41. classificando atletas')
    print('42. analisando triangulos v2.0 \n43. indice de massa corporal \n44. gerenciador de pagamentos \n45. GAME: pedra, papel e tesoura')
    print('0 - sair')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 36 a 45)?'))
    if opçao == 36:
        import p36
        p36.run()
    if opçao == 37:
        import p37
        p37.run()
    if opçao == 38:
        import p38
        p38.run()
    if opçao == 39:
        import p39
        p39.run()
    if opçao == 40:
        import p40
        p40.run()
    if opçao == 41:
        import p41
        p41.run()
    if opçao == 42:
        import p42
        p42.run()
    if opçao == 43:
        import p43
        p43.run()
    if opçao == 44:
        import p44
        p44.run()
    if opçao == 45:
        import p45
        p45.run()
    if opçao == 0:
        Break
    opçao1 = str(input('digite 1 para voltar para o mundo 2 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo2
        mundo2.run()
    else:
        import menu
        menu.run()
