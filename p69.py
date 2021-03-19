print ("~~~~~~~~~ Desafio 69, análise de dados do grupo ~~~~~~~~~")
dezoito = masculino = vinte = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Digite seu sexo? [F/M]')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Digite seu sexo? [F/M]')).strip().upper()[0]
    conti = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F':
        if idade >= 20:
            vinte += 1
    if conti == 'N':
        break
print ("O total de pessoa com mais ou igual a 18 anos: {}".format(dezoito))
print ("O total de pessoa do sexo masculino é : {}".format(masculino))
print ("O total de mulheres com 20 anos ou acima é: {}".format(vinte))