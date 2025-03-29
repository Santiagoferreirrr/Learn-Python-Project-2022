'''pessoas = {'nome': 'Santiago','sexo': 'M', 'idade': 19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys()) #CHAVES
print(pessoas.values()) #VALORES
print(pessoas.items()) #ITENS
pessoas['peso'] = 99 #ADICIONAR ALGO
del pessoas['sexo'] #DELETAR ALGO
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
