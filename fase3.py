while True:
    import webbrowser
    print('=====================================')
    print('=== BEM VINDO A FASE 3 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('esse desafio é uma introduçao do seu curso de python!')
    print('Segue abaixo o link do video:')
    webbrowser.open('https://www.youtube.com/watch?v=VuKvR1J2LQE&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=3 ')
    opçao = str(input('digite 1 para voltar para o mundo 1 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao == 1:
        import mundo1
        mundo1.run()
    else:
        import menu
        menu.run()
