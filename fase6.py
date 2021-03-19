while True:
    print('=====================================')
    print('=== BEM VINDO A FASE 6 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('3. somando numeros \n4. analisando variaveis')
    opçao = int(input('Qual fase você escolhe(digite o numero 3 ou 4)?'))
    if opçao == 3:
        import p3
        p3.run()
    else:
        import p4
        p4.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 1 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo1
        mundo1.run()
    else:
        import menu
        menu.run()
