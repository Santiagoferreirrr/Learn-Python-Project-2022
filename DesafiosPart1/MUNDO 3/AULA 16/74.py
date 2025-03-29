from random import randint

tup = (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10))

print('Listagem de números: ', end='')

for t in tup:
    print(f'{t}', end=' ')

print(f'\nO maior valor sorteado foi {max(tup)}')
print(f'O menor valor sorteado foi {min(tup)}')
