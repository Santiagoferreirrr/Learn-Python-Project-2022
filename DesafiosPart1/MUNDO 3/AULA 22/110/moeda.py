def aumentar(p=0, taxa=0, formato =False):
    res = p + (p * taxa/100)
    return res if formato is False else moeda(res)


def metade(p=0, formato=False):
    res = p/2
    return res if formato is False else moeda(res)


def dobro(p=0, formato=False):
    res = p*2
    return res if not formato else moeda(res)


def diminuir(p=0, taxa=0, formato=False):
    res = p - (p * taxa/100)
    return res if formato is False else moeda(res)

def moeda(p = 0, moeda = "R$", formato=False):
    return f'{moeda}{p:>8.2f}'.replace('.', ',')


def resumo(p=0, taxaa=10, taxar=5):
    print("="*30)
    print("RESUMO DO VALOR".center(30))
    print("="*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p,True)}')
    print(f'Metade do preço: \t{metade(p,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(p, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(p, taxar, True)}')
    print('-'*30)
