import run()
preço = float(input(' Digite o valor do produto: '))
desconto = preço * (5/100)
total = preço - desconto
print(' O novo preço com 5% de desconto é de {}R$'.format(total))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p12
    p12.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
