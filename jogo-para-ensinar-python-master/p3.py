import run()
numero1 = int(input (" Digite um valor: "))
numero2 = int(input (" Digite outro numero: "))
soma = numero1 + numero2
print (" A soma entre",numero1, "e",numero2, "é igual a ",soma)

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p3
    p3.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
