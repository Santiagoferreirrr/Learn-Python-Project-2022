nome = str(input('\033[32mQual é o seu nome? '))
if nome == 'Santiago':
    print('\033[35mQue nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Ana' or nome == 'Paulo':
    print('\033[33mSeu nome é bem popular no Brasil!')

print('\033[32mTenha um bom dia, {}!'.format(nome))
