col = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro',
       'São Paulo', 'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport',
       'Portuguesa', 'Atlético Paranaense', 'Vitória')

print(f'Lista de times do Brasileira 2013: {col}')
print('-=' * 100)
print(f'Os 5 primeiros colocados são {col[:5]}')
print('-=' * 100)
print(f'Os últimos 4 colocados da tabela são {col[-4:]}')
print('-=' * 100)
print(f'Times em ordem alfabética: {sorted(col)}')
print('-=' * 100)
print(f'O cruzeiro está na {col.index("Cruzeiro") +1}ª Posição! ')