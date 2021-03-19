from random import choice

pc = [0,1,2,3,4,5,6,7,8,9,10]
jogador = cont = 0
escolha = ''

print('=+='*5,'Jogo do PAR ou IMPAR','=+='*5)
while True:
    pc_escolha = choice(pc)
    jogador = int(input('Digite um numero: '))
    while escolha != 'P' and escolha != 'I':
        escolha = str(input('Ecolha PAR ou IMPAR[P/I]: ')).upper().strip()[0]
    resu = (jogador + pc_escolha) % 2
    if escolha == 'P' and resu == 0:
        print('=+='*15)
        print(f'Voce escolheu PAR')
        print(f'O PC escolheu {pc_escolha}')
        print(f'Voce escolheu {jogador}')
        print('Deu PAR. Voce Venceu!')
        print('=+=' * 15)
        cont += 1
    elif escolha == 'P' and resu == 1:
        print('=+=' * 15)
        print(f'Voce escolheu PAR')
        print(f'O PC escolheu {pc_escolha}')
        print(f'Voce escolheu {jogador}')
        print('Deu IMPAR. o Computador Venceu!')
        print(f'Parabens voce venceu o PC {cont} Vezes' if cont > 0 else f'Voce não venceu o PC nenhuma vez :(')
        print('=+=' * 15)
        break
    if escolha == 'I' and resu == 1:
        print('=+=' * 15)
        print(f'Voce escolheu IMPAR')
        print(f'O PC escolheu {pc_escolha}')
        print(f'Voce escolheu {jogador}')
        print('Deu IMPAR. Voce Venceu!')
        print('=+=' * 15)
        cont += 1
    elif escolha == 'I' and resu == 0:
        print('=+=' * 15)
        print(f'Voce escolheu IMPAR')
        print(f'O PC escolheu {pc_escolha}')
        print(f'Voce escolheu {jogador}')
        print('Deu PAR. o Computador Venceu!')
        print(f'Parabens voce venceu o PC {cont} vezes'if cont > 0 else f'Voce não venceu o PC nenhuma vez :(')
        print('=+=' * 15)
        break
    jogador = int(input('Digite um numero: '))
