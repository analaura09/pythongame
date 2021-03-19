jogador = dict()
par=list()
jogador['nome'] = input('nome do jogador: ')
tot = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,tot):
    par.append(int(input(f'   quantos gols na partiida {c}?')))
jogador['gols'] = par[:]
jogador['total'] = sum(par)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador['gols']):
    print(f'    => na partida {i}, fez {v} gols')
print(f'foi um total de {jogador["total"]} gols')
