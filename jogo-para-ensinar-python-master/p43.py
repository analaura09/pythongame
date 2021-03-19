peso = float(input('digite o seu peso(KG):'))
alt = float(input('digite a sua altura(M):'))
imc = peso/(alt**2)
if imc < 18.5:
    print('voce esta ABAIXO do peso!')
if 18.5<= imc < 25:
    print('voce esta no peso ideal!')
if 25 <= imc < 30:
    print('voce esta com SOBREPESO!')
if 30 <= imc < 40:
    print('voce esta com OBESIDADE!')
if imc > 40:
    print('voce esta com OBESIDADE MORBIDA!')
