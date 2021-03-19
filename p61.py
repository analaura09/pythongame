print('gerador de PA')
print('=-'*10)
prim = int(input('primeiro termo: '))
razao= int(input('razao de PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} '. format(termo), end=' ')
    termo += razao
     cont += 1
print('FIM')
