def area(larg,comp):
    a=larg*comp
    print(f'a area de um terreno {larg} x {comp} é de {a}m²')
print('controle de terrenos')
print('-='*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
