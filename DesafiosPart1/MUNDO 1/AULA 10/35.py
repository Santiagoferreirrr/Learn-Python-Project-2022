# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

from time import sleep
print('\033[35m-=-' * 21)
print('Você precisa formar um triangulo, digite abaixo 3 retas(em cm)')
print('-=-' * 21)
sleep(2)

rtA = int(input('\033[36mDigite uma reta em cm: '))
rtB = int(input('Digite uma outra reta em cm: '))
rtC = int(input('Digite uma outra reta em cm: '))

v1 = (rtB - rtC)
v2 = (rtA - rtC)
v3 = (rtA - rtB)

if rtA < rtB + rtC and rtB < rtA + rtC and rtC < rtA + rtB:
    print('\033[32mTriangulo formado!')

#if v1 < rtA < rtB + rtC:
    #print('Verdadeira')

#    if v2 < rtB < rtA + rtC:
        #print('Verdadeira')

#        if v3 < rtC < rtA + rtB:
#            print('Triangulo formado!')

else: print('\033[31mImpossivel formar um triangulo com os valores dados!')
