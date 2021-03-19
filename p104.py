import run()
def leiaInt(leia):
    n = input(Leia)
    while not n.isnumeric():
        print('\033[31mErro! Digite um número inteiro válido\033[0;0m')
        n = input(Leia)
        op = int(n)
        return op
    n = leiaInt('Digite um número: ')
    print(f'Você acabou de digitar o numero {n}.')
    
opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo3? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p104
    p104.run()
if opçao ==2:
    import mundo3
    mundo3.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
