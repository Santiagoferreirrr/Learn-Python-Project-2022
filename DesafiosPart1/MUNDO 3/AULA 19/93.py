jogador = dict()
partidas = list()

jogador["Nome"] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for v, k in jogador.items():
    print(f'O campo {v} tem o valor {k}!')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')