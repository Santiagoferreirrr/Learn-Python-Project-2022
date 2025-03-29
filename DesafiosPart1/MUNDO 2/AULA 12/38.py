print('\033[33m=X=' * 7)
print('COMPARADOR DE NUMBERS')
print('=X=' * 7)
print('')
num1 = int(input('\033[mDigite um número -> '))
num2 = int(input('Digite outro número -> '))
print('')
if num1 > num2:
    print('\033[35mO primeiro valor é maior')

elif num1 < num2:
    print('\033[36mO segundo valor é maior')

elif num1 == num2:
    print('\033[31mNão existe valor maior, os dois são iguais')