sx = str(input('Seu sexo -> [M/F] ')).upper()[0].strip()

# while sx not in 'MmFf':          A FORMA QUE EU ESTAVA TENTANDO FAZER

while sx != 'M' and sx != 'F':
    print('\033[31mResposta invalida, tente novamente!\033[m')
    sx = str(input('Seu sexo -> [M/F] ')).upper()[0].strip()
print('\033[32mSexo registrado com sucesso!')