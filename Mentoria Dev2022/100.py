def Media(a, b):
    c = a + b
    return c/2
primeiroNumero = int(input("Informe o primeiro numero: "))
segundoNumero = int(input("Informe o segundo numero: "))
print(f'A média é: {Media(primeiroNumero, segundoNumero)}')


def Situacao():
    if Media() < 4:
        return