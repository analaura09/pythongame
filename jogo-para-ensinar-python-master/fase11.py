while True:
    print('======================================')
    print('=== BEM VINDO A FASE 11 DO MUNDO 1 ===')
    print('=== OS DESAFIOS DESSA FASE SAO ===')
    print('essa fase é direcionada a aplicar cores no terminal')
    print('o modelo é (\033[o style;text;backm)')
    print('STYLE \n0 - sem estilo \n1 - estilo negrito \n4 - sublinhado \n7 - negativo')
    print('TEXT \n30 - branco \n31 - vermelho \n32 - verde \n33 - amarelo \n34 -azul \n35 - margenta \n36 - ciano \n37 - cinza ')
    print('BACK \n40 - fundo cinza \n41 - fundo vermelho \n42 - fundo verde \n43 - fundo amarelo \n44 azul \n45 - margenta \n46 - ciano \n47 - cinza')
    opçao1 = str(input('digite 1 para voltar para o mundo 1 \nou digite 2 para voltar para o menu dos mundos:'))
    if opçao1 == 1:
        import mundo1
        mundo1.run()
    else:
        import menu
        menu.run()
