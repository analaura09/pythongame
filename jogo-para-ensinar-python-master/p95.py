 controle=0
 nome=[]
 numero=[]
 total=0
 lista=list()
while True:
    nome.append(input('Digite o nome do jogador: '))
    numero.append(int(input("Digite a quantidade de partidas: ")))
    gols = []
    total = 0
    for i in range(0,numero[controle]):
        gols.append(int(input(f"Digite quantos gols foram feitos na partida {i + 1}: ")))
        for cont in gols:
            total += cont #total.append(cont1) resultado = {'id':controle, 'nome': nome[controle], 'gols': gols, 'total': total} lista.append(resultado)
            print(lista) sair=input("Deseja parar (S/N): ").strip().upper()[0] if sair in 'SN': break print("Responda S ou N") if sair == "S": print(lista) break controe += 1 aux=0 while True: key=int(input("Digite o id do jogador a ser msotrado(999 para sair): ")) if key == 999: break else: if int(len(lista) -1) >= key: print("Levantamento do jogador {}".format(lista[key]['nome'])) for i, j in e
