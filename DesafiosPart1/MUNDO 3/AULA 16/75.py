val = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))
print('-=' * 100)
print(f'Você digitou os valores {val}')
print('-=' * 100)
print(f'O valor 9 apareceu {val.count(9)} vezes')
print('-=' * 100)
if 3 in val:
    print(f'O valor 3 apareceu na {val.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print('-=' * 100)
print('Os valores pares digitados foram ',end= '')
for v in val:
    if v % 2 == 0:
        print(v, end= ' ')
print('-=' * 100)


