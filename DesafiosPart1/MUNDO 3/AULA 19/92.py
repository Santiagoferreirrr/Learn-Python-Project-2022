from datetime import date
atual = date.today().year

pessoa = {}

pessoa['Nome'] = str(input('Nome: '))
idade= int(input('Ano de nascimento: '))
pessoa['Idade'] = atual - idade
pessoa['Ctps'] = int(input('Carteira de trabalho(0 = não tem): '))

if pessoa['Ctps'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + (pessoa['Ano de contratação'] + 35) - atual

print('-=-'*20)

for k, v in pessoa.items():
    print(f'{k} -> {v}')