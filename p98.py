#Exercicio 98
from time import sleep

def contagem(begin, end, como):
    print("-=-=-" * 15)
    print(f"contagem de {begin} ate {end} em {como}")
    print()
    if end > begin:
        for c in range(begin, end, como):
            print(f"{c},",end='', flush=True)
            sleep(0.5)
        print(c + como)
    else:
        for i in  range(begin, end, -como):
            print(f"{i},",end='', flush=True)
            sleep(0.5)
        print(i - como)
    print("-=-=-" * 15)


#Programa Principal
comeca = 1
termina = 10
como = 1
contagem(comeca, termina, como)
inicio = 10
fim = 1
passo = 2
contagem(inicio, fim, passo)
print("Sua vez de Personalisar a Lista: ")
print()
while True:
    a = int(input("inicio: "))
    b = int(input("fim: "))
    c = int(input("como chegar: "))
    contagem(a, b, c)

    while True:
        q = str(input("Quer continuar? [S|N]")).upper().strip()
        if q == "S":
            break
        if q == "N":
            break
    if q == "N":
        break 
