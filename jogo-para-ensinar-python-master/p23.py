import run()
numero = int(input('Digite um numero: '))
unidade = numero //1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('O numero digitado foi {}'.format(numero))
print('O numero {} tem {} unidades'.format(numero,unidade))
print('O numero {} tem {} Dezenas'.format(numero, dezena))
print('O numero {} tem {} centenas'.format(numero,centena))
print('O numero {} tem {} unidades de milhas'.format(numero,milhar))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p23
    p23.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
