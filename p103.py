import run()
def ficha(jog='<desconhecido>', gol =0):
    print(f'o jogador {jog} fez {gol} gol(s) no campeonato')
n = input('nome do jogador:')
g = input('numeros de gols:')
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()== '':
    ficha(gol=g)
else:
    ficha(n,g)

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo3? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p103
    p103.run()
if opçao ==2:
    import mundo3
    mundo3.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
