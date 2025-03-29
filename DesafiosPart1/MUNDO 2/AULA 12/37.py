from time import sleep
num = int(input('Digite um número inteiro: '))
print('LENDO...')
sleep(1)
print('''1 -> Binário
2 -> Octal
3 -> Hexadecimal''')
bc = int(input('Escolha qual será a base de conversão -> '))
sleep(1)

if bc == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif bc == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif bc == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('\033[31mOpção invalida, tente novamente!')