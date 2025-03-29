while True:
    print('----' * 9)
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break
    print('----'*9)
    for x in range(1, 11):
        print(f'{tab} x {x} = {tab * x}')

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')



