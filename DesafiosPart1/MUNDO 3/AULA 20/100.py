from random import randint
numeros = []
def sorteia(num1, num2, num3, num4, num5):
    print(f'Os números sorteados foram -> {num1}-{num2}-{num3}-{num4}-{num5}')
    for n in range(0, 5):
        numeros.append(num1)
        numeros.append(num2)
        numeros.append(num3)
        numeros.append(num4)
        numeros.append(num5)

def somaPar(*par):
    somapar = 0
    for par in numeros:
        if par % 2 == 0:
            somapar += par
    print(f'A soma dos números pares é igual a -> {somapar}')


sorteia(randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))
somaPar(numeros)


'''from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print(' PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)'''