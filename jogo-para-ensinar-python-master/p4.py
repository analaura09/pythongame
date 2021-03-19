algo = input (" digite algo: ")
print (" O tipo primitivo desse valor é ", type(algo))
print (" Só tem espaços? ", algo.isspace())
print (" É um numero? ", algo.isnumeric())
print (" É alfabético? ", algo.isalpha())
print (" É alfanumerico? ", algo.isalnum())
print (" Esta em maiusculo?", algo.isupper())
print (" Esta em minusculo? ", algo.islower())
print (" Estar capitalizada? ", algo.istitle())

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p4
    p4.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')