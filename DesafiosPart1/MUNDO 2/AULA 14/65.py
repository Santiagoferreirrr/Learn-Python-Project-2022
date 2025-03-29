cont = maior = menor = somanum = medianum = 0
resp = 'S'

while resp != 'N':
    num = int(input('Digite um número: '))
    somanum += num
    cont += 1
    medianum = somanum / cont

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('\033[32mDeseja continuar [S/N]? \033[m')).upper().strip()[0]


print('Você digitou {} números e a média foi {}'.format(cont, medianum))
print('O maior valor é {} e o menor é {}'.format(maior, menor))