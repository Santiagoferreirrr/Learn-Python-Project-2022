n1 = int(input ('\033[33mDigite um número: '))
n2 = int(input ('\033[34mDigite outro número: '))
s = n1 + n2
print('\033[mA soma entre \033[33m{} \033[me \033[34m{}\033[m é \033[35m{}\033[m!'.format(n1, n2, s))
