ficha = {}

ficha['nome'] = str(input('nome: '))
anoN = int(input('ano de nascimento: '))
ficha['idade'] = 2019 - anoN
cart = int(str(input('carteira de trabalho (0 não tem )')))
if cart != 0:
    ficha['carteira'] = cart
    ficha['contratação'] = int(input('ano de contração: '))
    ficha['salario'] = int(input('qual o seu salario: '))
    aposentadoria = ficha['contratação'] + 35
    tempo = aposentadoria - 2019
    ficha['ano'] = tempo + ficha['idade']

    for k, v in ficha.items():
        print(f'{k} tem o valor {v}')
