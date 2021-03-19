from exe109 import moeda

p = float(input('digite o preço: R$'))
print(f'a metade de R${moeda.moeda(p)} é R${moeda.metade(p, True)}')
print(f'o dobro de R${moeda.moeda(p)} é R${moeda.dobro(p, True)}')
print(f'aumentando 10%, temos R${moeda.aumentar(p, 10, True)}')
print(f'reduzindo 13%, temos{moeda.diminuir(p,13, True)}')