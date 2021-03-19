import run()
frase = str(input(' Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posiçao {}'.format(frase.find('A')+1)) 
print('A letra A aparece pela ultima vez na posiçao {}'.format(frase.rfind('A')-1))

opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p26
    p26.run()
if opçao ==2:
    import mundo1
    mundo1.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')
