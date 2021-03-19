print('\033[0;33m*'*30)
print('Caixa 24 Horas!')
print('*'*30)
valor = float(input('\033[mQual valor deseja sacar ?: R$ '))
total = valor
notas = 0
while True:
    if total >= 50 :
        while total >= 50 :
            total -= 50
            notas += 1
        print(f'\033[0;34m{notas} Notas de R$ 50.00')
    notas = 0
    if total < 50 and total >= 20 :
        while total < 50 and total > 20 :
            total -= 20
            notas += 1
        print(f'{notas} Notas de R$ 20.00')
    notas = 0
    if total < 20 and total >=10 :
        while total < 20 and total > 10:
            total -= 10
            notas += 1
        print(f'{notas} Notas de R$ 10.00')
    notas = 0
    if total < 10 and total >= 1 :
        while total < 10 and total >= 1:
            total -= 1
            notas += 1
        print(f'{notas} Notas de R$ 1.00')
    if total == 0 :
        break
print('Tenha um Bom Dia!')
