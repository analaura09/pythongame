while True:
    print('======================================')
    print('=== BEM VINDO A FASE 18 DO MUNDO 3 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('84. lista composta e analise de dados \n85. listas com pares e impares \n86. matriz em python')
    print('87. mais sobre matriz em python \n88. palpites para a mega sena \n89. boletim com listas compostas')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 84 a 89)?'))
    if opçao == 84:
        import p84
        p84.run()
    if opçao == 85:
        import p85
        p85.run()
    if opçao == 86:
        import p86
        p86.run()
    if opçao == 87:
        import p87
        p87.run()
    if opçao == 88:
        import p88
        p88.run()
    if opçao == 89:
        import p89
        p89.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 3 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo3
        mundo3.run()
    else:
        import menu
        menu.run()
