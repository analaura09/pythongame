def run():
    salário = float(input("Qual o salário do funcionário? R$"))
    if salário <= 1250:
        novo = salário + (salário * 15 / 100)
    else: novo = + salário (salário * 10 / 100)
    print ('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário,novo))
    
    opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
    if opçao == 1:
        import p34
        p34.run()
    if opçao ==2:
        import mundo1
        mundo1.run()
    if opçao == 3:
        print('Obrigada por jogar! Volte sempre :)')