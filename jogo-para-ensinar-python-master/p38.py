import run()
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
   print('O segundo valor é maior')
else:
    print("Os dois valores sao iguais")

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p38
    p38.run()
if opçao ==2:
    import mundo2
    mundo2.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')