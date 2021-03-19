ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
limite = ptermo + 10 * razao
for p in range(ptermo,limite,razao):
    print('{}'.format(p), end=' - ')
print('FIM!')
