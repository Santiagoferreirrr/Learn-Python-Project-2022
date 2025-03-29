valores = []

while True:
    val = int(input('Digite um valor: '))

    if val not in valores:
        valores.append(val)
        print('\033[32mNúmero cadastrado com sucesso...\033[m')
    else:
        print('Valor já existente! Não vou adicionar...')

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
valores.sort()
print(f'Valores digitados: {valores}')

