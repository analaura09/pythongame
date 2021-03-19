print('\033[31m{:§^20}\033[m'.format(' BEM VINDOS '))
valor = float(input('Digite o valor a ser pago: '))
print('''Escolha [1] para pagamaneto a \033[34mVISTA\033[m
        [2] para pagamento a \033[34mVISTA NO CARTÃO\033[m 
        [3] para pagamento \033[34m2X no CARTÃO\033[m
        [4]para pagamento \033[34m3X ou mais no CARTÃO\033[m''')
escolha = int(input('{:>15}'.format('Opção = ')))
print('A forma de pagamento foi',end = ' ')
if escolha == 1:
    print('a \033[36mVISTA\033[m.Voce tera 10% o valor final', end=' ')
    print('do produto é R${:.2f}'.format(valor - (valor * (10/100))))
elif escolha == 2:
    print(' a \033[36mVISTA NO CARTÃO\033[m. Voce tera 5% o valor final', end=' ')
    print('do produto é R${:.2f}'.format(valor - (valor * (5/100))))
elif escolha == 3:
    print(' a \033[36m2X no CARTÃO\033[m.',end = ' ' )
    print('do produto é de R${:.2f}'.format(valor))
    print('O valor das parcelas é de {:.2f}'.format(valor / 2))
elif escolha == 4:
    print(' a \033[36m3X ou mais no CARTÃO\033[m.')
    parcelas = int(input('Digite o numero de parcelas: '))
    if parcelas <=2:
        print('Por favor escolha outra opção do menu.')
    else:
        print('Voce pagara o produto dividido em {}X de R${:.2f}'.format(parcelas, valor / parcelas))
print()
print('\033[31m{:§^20}\033[m'.format(' FIM '))
 

