def metade(m):
    return ("R${:.2f}".format(m/2))

def dobro(m):
    return ("R${:.2f}".format(m*2))

def aumento(m, p):
    return ("R${:.2f}".format((m*0.10) + m))

def reduzir(m, p):
    return ("R${:.2f}".format(m - (m*0.13)))

def moeda(m):
    return ("R${:.2f}".format(m))