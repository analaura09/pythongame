while True:
    print('======================================')
    print('=== BEM VINDO A FASE 13 DO MUNDO 2 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('46. contagem regressiva \n47. contagem de pares \n48. soma impares multiplos de tres')
    print('49. tabuada V2.0 \n50. soma dos pares \n51. progressao aritmetica \n52. numeros primos \n53. detector de palindromo')
    print('54. grupo da maioridade \n55. maior e menor da sequencia \n56. analisador completo')
    opçao = int(input('qual desafio voce escolhe(digite um numero de 46 a 56)?'))
    if opçao == 46:
        import p46
        p46.run()
    if opçao == 47:
        import p47
        p47.run()
    if opçao == 48:
        import p48
        p48.run()
    if opçao == 49:
        import p49
        p49.run()
    if opçao == 50:
        import p50
        p50.run()
    if opçao == 51:
        import p51
        p51.run()
    if opçao == 52:
        import p52
        p52.run()
    if opçao == 53:
        import p53
        p53.run()
    if opçao == 54:
        import p54
        p54.run()
    if opçao == 55:
        import p55
        p55.run()
    if opçao == 56:
        import p56
        p56.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 2 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo2
        mundo2.run()
    else:
        import menu
        menu.run()
