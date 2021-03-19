while True:
    print('======================================')
    print('=== BEM VINDO A FASE 14 DO MUNDO 2 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('57. validaçao de dados \n58. jogo da adivinhaçao V2.0 \n59. criando um menu de opçoes')
    print('60. calculo do fatorial \n61. progressao aritmetica V2.0 \n62. super progressao aritmetica V3.0')
    print('63. sequencia de fibonacci V1.0 \n64. tratando varios valores V1.0')
    print('65. maior e menor valores')
    opçao = int(input('qual desafio voce escollhe(digite um numero de 57 a 65)?'))
    if opçao == 57:
        import p57
        p57.run()
    if opçao == 58:
        import p58
        p58.run()
    if opçao == 59:
        import p59
        p59.run()
    if opçao == 60:
        import p60
        p60.run()
    if opçao == 61:
        import p61
        p61.run()
    if opçao == 62:
        import p62
        p62.run()
    if opçao == 63:
        import p63
        p63.run()
    if opçao == 64:
        import p64
        p64.run()
    if opçao == 65:
        import p65
        p65.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 2 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo2
        mundo2.run()
    else:
        import menu
        menu.run()
