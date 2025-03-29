def área(larg, comp):
    print('-' * 30)
    print(f'{"CONTROLE DE TERRENOS":^30}')
    print('-'*30)
    larg = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    result = larg * comp
    print(f'\033[4mA área de um terreno {larg} x {comp} é de {result}m²')


área(0, 0)