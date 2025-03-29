maisde18 = hom = mul = 0

while True:
    print('=='* 12)
    print('  CADASTRE UMA PESSOA')
    print('==' * 12)
    id = int(input('Idade: '))

    sx = ' '
    while sx not in 'MF':
        sx = str(input('Sexo[M/F]:')).upper().strip()[0]

    print('\033[32mPESSOA CADASTRADA COM SUCESSO!\033[m')

    if id >= 18:
        maisde18 += 1

    if sx == 'M':
        hom += 1

    if sx == 'F' and id < 20:
        mul += 1

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]

    if cont == 'N':
        break
print('')
print(f'Ao total foram cadastradas {maisde18} pessoas com mais de 18 anos!')
print(f'Ao todo temos {hom} Homens cadastrados')
print(f'E temos {mul} Mulheres com menos de 20 anos')

