from time import sleep
print('\033[35m-=-' * 11)
print('APROVADOR DE EMPRÉSTIMO BANCÁRIO!')
print('-=-' * 11)
sleep(1)
vc = float(input('\033[mQual o valor da casa? R$'))
sal = float(input('Qual o valor do seu salário? R$'))
an = int(input('Em quantos anos quer pagar a casa? '))
print('\033[34mANALISANDO...')
sleep(3)

prest = (vc // an) // 12

sal1 = 0.30 * sal

print('\033[33mPara pagar uma casa de R${:.2f} a prestação será de R${:.2f} reais!'.format(vc, prest))

if prest <= sal1:
    print('\033[32mEmprestimo Aprovado, CONGRATULATIONS!!!!!!!!!!! Aqui está o seu dinheiro!')

elif sal1 < prest:
    print('\033[31mPEEEEEEEEM, Emprestimo Negado')