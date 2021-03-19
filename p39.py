from datetime import date
print ("------------ Desafio 39, alistamento militar -----------")
atual=date.today().year

nasci=int(input("Em que ano você nasceu? "))

idade= atual - nasci

print ("Você nasceu no ano de {} e tem {} anos".format(nasci, idade))

if idade == 18:
    print ("Você precisa se alistar esse ano.")
elif idade > 18:
    print ("Você deveria ter se alistado a {} ano/anos.".format(idade-18))
elif idade < 18:
    print ("Você não precisa se alistar agora, você {} ano/anos para se alistar.".format(18-idade))
