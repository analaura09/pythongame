val=[]
while True:
    val.append(int(input('digite um valor:')))
    resp=input('quer continuar? [S/N]')
    if resp in 'Nn':
        break
print('-='*30)
print(f'voce digitou {len(val)} elementos')
val.sort(reverse=True)
print(f'os valores em ordem decrescente sao {val}')
if 5 in val:
    print('o valor 5 faz parte da lista!')
else:
    print('o valor 5 nao foi encontrado na lista!')
