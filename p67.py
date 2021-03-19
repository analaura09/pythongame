print ("~~~~~~~~~ Desafio 67, tabuada v3.0 ~~~~~~~~~")

while True:
    n=int(input("Qual tabuada você quer ver: "))
    if n < 0:
        break
    print (" ")
    for c in range (1, 11):
        print ("{} x {} = {}".format(n, c, n*c))
