cont=('zero','um','dois','tres','quatro',
      'cinco', 'seis','sete','oito','nove',
      'dez','onze','doze','treze', 'cartoze',
      'quinze','dezesseis','dezessete','dezoito',
      'dezenove','vinte')
while True:
    num =int(input('digite um numero entre 0 e 20:'))
    if 0 <= num <= 20:
        break
    print('tente novmente', end='')
print(f'voce digitou o numero {cont[num]}')
