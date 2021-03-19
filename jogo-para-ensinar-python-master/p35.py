def run():
l1 = int(input(' Digite o primeiro lado:'))
l2 = int(input(' Digite o segundo lado:'))
l3 = int(input(' Digite o terceiro lado:'))

if l1 < (l2+l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('É possivel formar um triangulo!')
else:
    print(' Nao é possivel formar um triangulo!')

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p35
    p35.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')    
