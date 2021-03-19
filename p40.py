print ("            Desafio 40              ")
print ("OBS. as notas digitas deverão ser digitada de forma como está o exemplo. \nExemplo: 6.8")
print (" ")

n1=float(input("Digite a primeira nota:"))
n2=float(input("Digite a segunda nota: "))

media=(n1+n2)/2

if media < 5.0:
    print ("Reprovado!")
elif media == 5.0 or media >= 6.9:
    print ("Recuperação!")
else:
    print ("Aprovado!")
print ("Sua média foi {:.1f}".format(media))
