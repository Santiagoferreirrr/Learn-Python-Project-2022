vel = int(input('\033[32mDigite a velocidade do carro: '))

if vel > 80:
    print('\033[4;31mVocê foi multado!')
    print('\033[0;32mA multa vai custar R$7.00 por cada KM ultrapassado, ou seja, \033[4;31mvocê pagará R${:.2f}'.format((vel - 80) * 7))
else:
    print('\033[33mParabéns, você estava dentro do limite de velocidade, não fez mais que sua obrigação!')
