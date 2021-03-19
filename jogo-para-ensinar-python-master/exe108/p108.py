from exe108 import moeda

p = float(input('digite o preço: R$'))
print(f'a metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}')
print(f'o dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')
