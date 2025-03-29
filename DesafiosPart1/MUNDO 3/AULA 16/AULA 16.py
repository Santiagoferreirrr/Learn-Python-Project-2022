'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

print(sorted(lanche)) #COLOCA EM ORDEM

##########################################################

for c in lanche:
    print(f'Eu vou comer {c}')

##########################################################

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

##########################################################

for pos, c in enumerate(lanche):
   print(f'Eu  vou comer {c} na posição {pos}')

print('Comi dmssss!')'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
del(c)
print(c)


