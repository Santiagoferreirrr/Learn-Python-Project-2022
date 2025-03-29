print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)


t = int(input('Primeiro termo: '))
r = int(input('Razão: '))

d = t + (10-1) * r

for x in range(t , d + r, r):
    print('-> {} '.format(x), end='')
print('THE END')