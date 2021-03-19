import run()
salario = float(input(' Digite o valor do seu salário: '))
aumento = salario * (15/100)
total = salario + aumento
print(' O seu salário com o aumento vai ser de {}R$'.format(total))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p13
    p13.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
