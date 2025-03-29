dicionario = dict()
lista = list()
media = soma = 0
while True:
    dicionario.clear()
    dicionario["nome"] = str(input('Nome: '))
    while True:
        dicionario["sexo"] = str(input('Sexo[M/F]: ')).upper()[0]
        if dicionario['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dicionario["idade"] = int(input('Idade: '))
    soma += dicionario['idade']
    lista.append(dicionario.copy())
    while True:
        resp = str(input('Quer continuar[S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print(f'A) Foram cadastradas {len(lista)} pessoas na lista')
print(f'B) A média de idade do grupo é de {soma / len(lista)}')
print(f'C) Lista com todas as mulheres: ', end='')
for d in lista:
    if d['sexo'] in 'Ff':
        print(f'{d["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for d in lista:
    if d['idade'] >= media:
        print('    ', end='')
        for k, v in d.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRADO >>')
