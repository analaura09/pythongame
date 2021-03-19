from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
maior = 0
menor = 0
for c in range(len(numeros)):
    if c == 0:
        maior = numeros[0]
        menor = numeros[0]
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
print(f'Os numeros sorteados foram {numeros}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
 

