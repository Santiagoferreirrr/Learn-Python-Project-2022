from time import sleep

a1 = input ('\033[32mDigite algo: ')
print('ANALISANDO...')
sleep(2)
print('\033[35mO tipo primitivo desse valor é' , type(a1))
sleep(1)
print('Tem espaços?', a1.isspace())
sleep(1)
print('É um número?', a1.isnumeric())
sleep(1)
print('É alfabético?', a1.isalpha())
sleep(1)
print('É alfanúmerico?' ,a1.isalnum())
sleep(1)
print('Está em maiúsculas?', a1.isupper())
sleep(1)
print('Está em minusculas?', a1.islower())
sleep(1)
print('Está capitalizada?', a1.istitle())
sleep(2)
print('FIM')