import run()

saudaçao = "Olá, Mundo!"
print(saudaçao)

opçao = int(input('deseja repetir esse exercicio[1] \ndeseja voltar para o mundo 1[2] \ndeseja sair do jogo[3]'))
if opçao == 1:
    import p1
    p1.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
