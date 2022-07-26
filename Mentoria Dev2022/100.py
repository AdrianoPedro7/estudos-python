def Media(a, b):
    c = a + b
    return c / 2


def Situacao(c):
    if c < 4:
        print("Reprovado")
    elif 4 < c < 7:
        print("Recuperação")
    else:
        print("Aprovado")


Situacao(Media(5,9))
