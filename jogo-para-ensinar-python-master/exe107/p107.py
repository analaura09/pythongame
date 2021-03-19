from exe107 import moeda

p = float(input('digite o preço: R$'))
print(f'a metade de R${p} é R${moeda.metade(p)}')
print(f'o dobro de R${p} é R${moeda.dobro(p)}')
print(f'aumentando 10%, temos R${moeda.aumentar(p, 10)}')
