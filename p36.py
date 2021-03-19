import run()
casa =  float(input('Valor da casa: R$'))
salário = float(input("salário de um comprador: R$"))
anos  = int(input('Quantos anos do financiamento?'))
prestaçao = casa /(anos * 12)
print("para pagar uma casa de R${:.2f} em {} anos" . format(casa,anos), end=' ')
print ('  prestaçao sera de R${:.2f}'.format(prestaçao))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p36
    p36.run()
if opçao ==2:
    import mundo2
    mundo2.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')