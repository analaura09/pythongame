# Desafio 63 - Sequência de Fibonacci v1.0
print ("Desafio 63, Sequência de Fibonacci v1.0")

n=int(input("Quantos números você quer mostrar: "))
t1=0
t2=1

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("{} → {}".format(t1, t2), end='')
cont=2
while cont < n:
    t3= t1+ t2
    print (" → {}".format(t3), end='')
    t1= t2
    t2= t3
    cont+=1
print ("→ Fim")