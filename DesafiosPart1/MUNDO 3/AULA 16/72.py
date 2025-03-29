n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
     'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
     'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
     'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
     'Dezenove', 'Vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print ('Tente novamente. ', end= '')

    print(f'Você digitou o número {n[num]}')

    cont = str(input('Quer continuar[S/N]:')).upper().strip()[0]
    if cont == 'N':
        break
print('===== FIM DO PROGRAMA =====')


