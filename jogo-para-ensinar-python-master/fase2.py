while True:
    import webbrowser
    print('=====================================')
    print('=== BEM VINDO A FASE 2 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('Esse desafio faz parte da introduçao a python!')
    webbrowser.open('\nhttps://www.youtube.com/watch?v=Mp0vhMDI7fA&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=2')
    opçao = str(input('digite 1 para voltar para o mundo 1 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao == 1:
        import mundo1
        mundo1.run()
    else:
        import menu
        menu.run()
