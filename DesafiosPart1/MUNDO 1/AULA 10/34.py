# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = int(input('\033[35mDigite seu salário: \033[32mR$'))

if sal > 1250:
    print('\033[32mSeu novo salário será no valor de R${:.2f}'.format((sal * 0.1) + sal))

if sal <= 1250:
    print('\033[32mSeu novo salário será no valor de R${:.2f}'.format((sal * 0.15) + sal))