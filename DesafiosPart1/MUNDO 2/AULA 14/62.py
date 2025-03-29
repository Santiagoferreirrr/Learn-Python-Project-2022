print('='*25)
print('   10 TERMOS DE UMA PA')
print('='*25)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('')
print('Progressão finalizada com {} termos mostrados'.format(total))