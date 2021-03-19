l1 = int(input(' Digite o primeiro lado:'))
l2 = int(input(' Digite o segundo lado:'))
l3 = int(input(' Digite o terceiro lado:'))

if l1 < (l2+l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('É possivel formar um triangulo!')
    elif l1 == l2 or l1 == l3 or l3 == l2:
        print('esse triangulo é um triangulo isoceles!')
    elif l1 == l2 == l3:
        print('esse triangulo é um triangulo equilatero!')
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print('esse triangulo é um triangulo escaleno')
else:
    print(' Nao é possivel formar um triangulo!')

elif l1 == l2 or l1 == l3 or l3 == l2:
    print('esse triangulo é um triangulo isoceles!')
elif l1 == l2 == l3:
    print('esse triangulo é um triangulo equilatero!')
elif l1 != l2 and l2 != l3 and l1 != l3:
    print('esse triangulo é um triangulo escaleno')
