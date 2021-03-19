while True:
    print('=====================================')
    print('=== BEM VINDA A FASE 9 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('22. analisando um texto \n23. separando os digitos de um numero \n24. primeiras letras de um texto \n25. procurando string \n26. primeira e ultima ocorrencia \n27. primeiro e ultimo nome')
    opçao = int(input('Qual desafio você escolhe(digite um numero de 22 a 27)?'))
    if opçao == 22:
        import p22
        p22.run()
    if opçao == 23:
        import p23
        p23.run()
    if opçao == 24:
        import p24
        p24.run()
    if opçao == 25:
        import p25
        p25.run()
    if opçao == 26:
        import p26
        p26.run()
    if opçao == 27:
        import p27
        p27.run()
