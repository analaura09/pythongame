print('-='*20)
print('Digite quantos valores quiser para obter sua média')
print('-='*20)
sair = 'N'
cont = soma = maior = menor = 0
while sair in 'Nn':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        menor = num
        maior = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    sair = str(input('Deseja sair?[S/N] '))
media = soma / cont
print('A média entre os valores foi de {}\nO maior valor foi {} e o menor {}'.format(media, maior, menor))
print('Fim')
