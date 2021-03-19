def run():
    print('== JOGO DO CURSO PYTHON BASICO ==')
    print('=-='*10)
    print('             MENU')
    print('=-='*10)
    print('== Os mundos desses jogos sao == ')
    print('1. mundo 1- FLORESTA TROPICAL \n2. mundo 2- FLORESTA DE GELO \n3. mundo 3- DESERTO')
    opçao = int(input('Qual mundo você escolhe(digite 1, 2 ou 3)?'))
    if opçao == 1:
        import mundo1
        mundo1.run()
    if opçao == 2:
        import mundo2
        mundo2.run()
    if opçao == 3:
        import mundo3
        mundo3.run()
run()
        
