print('\033[32m-=-=-=-LOJAS SANTIAGO-=-=-=-')
pre = int(input('Preço das compras: \033[32mR$ \033[m'))
print('\033[32m-=-=\033[m'*7)
print('''
(1) Á VISTA DINHEIRO/CHEQUE
(2) Á VISTA NO CARTÃO
(3) EM ATÉ 2X NO CARTÃO
(4) 3X OU MAIS NO CARTÃO
''')
fp = int(input('\033[32mForma de pagamento -> \033[m'))
print('')
if fp == 1:
    print('A forma de pagamento escolhida foi á vista dinheiro/cheque, você '
          'receberá um desconto de 10%, ou seja... só pagará \033[4;32mR${:.2f}\033[m!'.format(pre - (pre*0.10)))

elif fp == 2:
    print('A forma de pagamento escolhida foi á vista no cartão, você terá um desconto de 5%, ou seja... só ' 
          'pagará \033[4;32mR${:.2f}\033[m!'.format(pre - (pre*0.05)))

elif fp == 3:
    print('A forma de pagamento escolhida foi em até 2x no cartão, dessa forma você paga o valor normal!')

elif fp == 4:
    print('A forma de pagamento escolhida foi de 3x ou mais no cartão, terá que pagar 20% de juros, ou '
          'seja... \033[4;32mR${:.2f}\033[m!'.format(pre+(pre*0.20)))

else: print('\033[31mOpção invalida, tente novamente!')