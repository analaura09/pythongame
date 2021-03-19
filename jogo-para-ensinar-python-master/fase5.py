while True:
    import webbrowser
    print('=====================================')
    print('=== BEM VINDO A FASE 5 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('Essa fase faz parte da sua introduçao do curso de python! ')
    print('Segue abaixo o link do video:')
    webbrowser.open('\nhttps://www.cursoemvideo.com/unit/python-aula-05-instalando-pycharm-qpython/?id=7180')
    opçao=int(input('digite 1 para voltar ao mundo 1/ ou digite 2 para voltar ao menu:'))
    if opçao == 1:
        import mundo1
        mundo1.run()
    if opçao == 2:
        import menu
        menu.run()
