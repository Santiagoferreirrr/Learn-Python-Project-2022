num = []
maior = 0
menor = 0
for n in range(0, 5):
    num.append(int(input('Digite um valor para a posição {}: '.format(n))))

    if n == 0:
        maior = menor = num[n]

    else:
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]

print(f'Valores: {num}')
print(f'O maior valor digitado foi {maior} na posição ', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...',end=' ')

print(f'\nO menor valor digitado foi {menor} na posição ', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...',end=' ')