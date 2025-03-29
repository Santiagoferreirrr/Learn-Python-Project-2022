num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print('')
print('Foram digitados {} números e a soma de todos eles foi {}'.format(cont, soma))