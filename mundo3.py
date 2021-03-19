def run():
    print('==================================')
    print('=== BEM VINDO AO MUNDO 3- FOGO ===')
    print('=== AS FASES DESSE MUNDO SAO ===')
    print('16. tuplas \n17. listas(parte 1) \n18. listas(parte 2) \n19. dicionarios \n20. funçoes(parte 1)')
    print('21. funçoes(parte 2) \n22. Modulos e pacotes')
    print('23. <voltar para o menu dos mundos>')
    opçao = int(input('qual fase voce escolhe(digite um numero de 16 a 22)?'))
    if opçao == 16:
        import fase16
        fase16.run()
    if opçao == 17:
        import fase17
        fase17.run()
    if opçao == 18:
        import fase18
        fase18.run()
    if opçao == 19:
        import fase19
        fase19.run()
    if opçao == 20:
        import fase20
        fase20.run()
    if opçao == 21:
        import fase21
        fase21.run()
    if opçao == 22:
        import fase22
        fase22.run()
    if opçao == 23:
        import menu
        menu.run()
run()