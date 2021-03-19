import run()
largura = float(input(' Digite a largura da parede: '))
altura = float(input(' Digite a altura da parede: '))
area = largura * altura
print (' Sua parede é de dimensão {} x {} e sua area é de {}m²'.format(largura, altura, area))
tinta = area/2
print(' Para pintar essa parede, você irá precisar de {}l de tinta',format(tinta))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p11
    p11.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
