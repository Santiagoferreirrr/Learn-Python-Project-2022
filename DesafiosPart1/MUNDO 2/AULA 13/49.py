from time import sleep
print('====TABUADA====')
print('')
n = int(input('Número -> '))
print('')
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))
    sleep(0.3)
print('FIM')