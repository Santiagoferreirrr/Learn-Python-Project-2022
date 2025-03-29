fra = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(fra.count('A')))
print('A letra "A" aparece primeiro na posição {}'.format(fra.find('A')+1))
print('A letra "A" aparece por ultimo na posição {}'.format(fra.rfind('A')+1))