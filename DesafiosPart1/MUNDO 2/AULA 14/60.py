'''from math import factorial #IMPORTANDO UMA BIBLIOTECA
num = int(input('Digite um número para calcular seu Factorial: '))
print('O factorial de {} é {}'.format(num, factorial(num)))

#########################################################################################
'''
num = int(input('Digite um número para calcular seu Factorial: ')) # UTILIZANDO O WHILE
c = num
f = 1
print('Caculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''
#########################################################################################

num = int(input('Digite um número para calcular seu Factorial: ')) #UTILIZANDO O FOR
c = num
f = 1
for x in range(num):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''