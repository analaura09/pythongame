def run():
    distancia = float(input("Qual a distancia da sua viagem? "))
    print("voce vai começar uma viagem de {}km".format(distancia))
    if distancia <= 200:
         preço = distancia *0.50
    else:
        preço = distancia * 0.45
    print(' O preço da sua passagem será de R${:.2f}'.format(preço)) 
    
    opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
    if opçao == 1:
        import p31
        p31.run()
    if opçao ==2:
        import mundo1
        mundo1.run()
    if opçao == 3:
        print('Obrigada por jogar! Volte sempre :)')