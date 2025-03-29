not1 = float(input('Primeira nota: '))
not2 = float(input('Segunda nota: '))
print('')
med = (not1 + not2) / 2
print('Sua média foi -> {:.1f}'.format(med))
print('')
if med < 5:
    print('\033[31mREPROVADO!')

elif med >= 7:
    print('\033[32mAPROVADO!')

else: print('\033[33mRECUPERAÇÃO!')
