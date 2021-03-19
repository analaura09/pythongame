while True:
    print('======================================')
    print('=== BEM VINDO A FASE 10 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('28. jogo da adivinhaçao v1.0 \n29. radar eletronico \n30. par ou impar \n31. custo da viagem \n32. ano bissexto \n33. maior e menor valores \n34. aumentos multiplos \n35. analisando triangulo v1.0')
    opçao = int(input('Qual desafio você esolhe(digite um numero de 28 a 35)?'))
    if opçao == 28:
        import p28
        p28.run()
    if opçao == 29:
        import p29
        p29.run()
    if opçao == 30:
        import p30
        p30.run()
    if opçao == 31:
        import p31
        p31.run()
    if opçao == 32:
        import p32
        p32.run()
    if opçao == 33:
        import p33
        p33.run()
    if opçao == 34:
        import p34
        p34.run()
    if opçao == 35:
        import p35
        p35.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 1 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo1
        mundo1.run()
    else:
        import menu
        menu.run()
        