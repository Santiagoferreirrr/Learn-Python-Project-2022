soma = 0
cont = 0

for x in range(1, 7):
    n = int(input('Digite o {} valor -> '.format(x)))
    if n % 2 == 0:
        cont += 1
        soma += n

print('Você informou {} números PARES e a soma deles foi {}'.format(cont, soma))