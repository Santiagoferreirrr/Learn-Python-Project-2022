from time import sleep
print('-> Números pares de 0 a 50 <-')
sleep(2)
for x in range(2, 51, 2):
    print('-> {}'.format(x), end=' ')
print('FIM')