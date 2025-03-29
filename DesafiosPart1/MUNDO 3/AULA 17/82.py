l1 = list()
l2 = list()
l3 = list()

while True:
    l1.append(int(input('Digite um número: ')))
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont in 'N':
        break

for i, v in enumerate(l1):
    if v % 2 == 0:
        l2.append(v)
    elif v % 2 == 1:
        l3.append(v)

print(f'Lista Completa: {l1}')
print(f'Somente Pares: {l2}')
print(f'Somente Impares: {l3}')