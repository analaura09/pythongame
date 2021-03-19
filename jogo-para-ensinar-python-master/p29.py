import run()
velocidade = float(input('Qual a velocidade atual do seu carro? '))
if velocidade > 80:
    print('MULTADO! voce excedeuo limite permitido que é de 80km/h')
    multa = (velocidade - 80)* 7
    print('voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! dirija com segurança!')

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p29
    p29.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
