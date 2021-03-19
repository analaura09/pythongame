while True:
    print('=====================================')
    print('=== BEM VINDO A FASE 7 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('5. antecessor e sucessor \n6. dobro, triplo, raiz quadrada \n7. media aritimetica')
    print('8. conversor de medidas \n9. tabuada \n10. conversor de moedas \n11. pintando parede')
    print('12. calulando descontos \n13. reajuste salarial \n14. conversor de temperaturas')
    print('15. aluguel de carros')
    opçao = int(input('Qual desafio você escolhe(digite um numero de 5 a 15)?'))
    if opçao == 5:
        import p5
        p5.run()
    if opçao == 6:
        import p6
        p6.run()
    if opçao == 7:
        import p7
        p7.run()
    if opçao == 8:
        import p8
        p8.run()
    if opçao == 9:
        import p9
        p9.run()
    if opçao == 10:
        import p10
        p10.run()
    if opçao == 11:
        import p11
        p11.run()
    if opçao == 12:
        import p12
        p12.run()
    if opçao == 13:
        import p13
        p13.run()
    if opçao == 14:
        import p14
        p14.run()
    if opçao == 15:
        import p15
        p15.run()
    opçao1 = str(input('digite 1 para voltar para o mundo 1 ou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo1
        mundo1.run()
    else:
        import menu
        menu.run() 
