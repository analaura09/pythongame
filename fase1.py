import webbrowser
while True:
    print('=====================================')
    print('=== BEM VINDO A FASE 1 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('esse desafio é uma introduçao do seu curso de python!')
    print('aqui esta o link para esse video: ')
    webbrowser.open('\nhttps://www.youtube.com/watch?v=S9uPNppGsGo&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6')
    opçao = str(input('digite 1 para voltar para o mundo 1 \ndigite 2 para voltar para o menu dos mundos: '))
    if opçao == 1:
        import mundo1
        mundo1.run()
    if opçao == 2:
        import menu
        menu.run()

