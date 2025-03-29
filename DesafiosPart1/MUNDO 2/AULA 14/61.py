print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)


t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

termo = t
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('THE END')