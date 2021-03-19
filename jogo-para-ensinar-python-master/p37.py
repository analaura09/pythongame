import run()
num = int(input('escreva um numero inteiro: '))
print('''escolha uma das bases para conversão:
[1] converter para binario
[2] converter para octal
[3]converter para hexadecimal''')
opção = int(input('sua opção: '))
if opção == 1:
    print('{} convertido para binario é igual a: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a: {}'.format(num, bin(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a: {}'.format(num, bin(num)[2:]))
else: print("opção invalida. tente again.")
      
opçao = int(input('deseja repetir esse exercicio?[1] \ndeseja voltar para o mundo1? [2] \ndeseja sair do jogo?[3]'))
if opçao == 1:
    import p37
    p37.run()
if opçao ==2:
    import mundo2
    mundo2.run()
if opçao == 3:
    print('Obrigada por jogar! Volte sempre :)')