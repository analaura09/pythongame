num = (int(input('digite um numero: ')),
       int(input('digite outro numero:')),
       int(input('digite mais um numero:')),
       int(input('digite o ultimo numero:')))
print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3)+1}ª posiçao')
else:
    print('o valor 3 nao foi digitado em nenhuma posiçao')
print('o valor 3 nao foi digitado foram', end='')
for n in num:
    if n % 2 ==0:
        print(n, end=' ')
