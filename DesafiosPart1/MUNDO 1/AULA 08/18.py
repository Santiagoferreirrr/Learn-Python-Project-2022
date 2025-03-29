import math
ag = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(ag))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ag, s))
c = math.cos(math.radians(ag))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ag, c))
t = math.tan(math.radians(ag))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ag, t))
