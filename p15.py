import run()
quilometros = float(input(' Quantos quilometros você percorreu? '))
dias = float(input(' Quantos dias voê alugou o carro? '))
totaldias = 60 * dias
totalkm = 0.15 * quilometros
total = totaldias + totalkm
print(' O preço total dos dias é de {}R$'.format(totaldias))
print(' O preço total dos km percorridos é de {}R$'.fomat(totalkm))
print(' O preço totala a pagar é de {}R$'.format(total))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p15
    p15.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
