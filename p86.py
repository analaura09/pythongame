lista = []
print('\n')
for l in range(1,4) :
    for c in range (1,4) :
        lista.append(int(input(f'diga um valor para a posição({l},{c}) = ')))
print('=–'*21)
for p,n in enumerate(lista) :
    print(f' [{n:^5}]',end = '')
    if p == 2 :
        print('')
    elif p == 5 :
        print('')
print('\n')
