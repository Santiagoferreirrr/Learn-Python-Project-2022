'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário em Python. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação']= 'Reprovado'
print('-='*12)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
