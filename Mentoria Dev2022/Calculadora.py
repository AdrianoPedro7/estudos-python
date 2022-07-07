def fat(n):
    if (n <= 1):
        return 1
    else:
        return n * fat(n - 1)


def soma(a, b):
    c = a + b
    return c


def subtrair(a, b):
    c = a - b
    return c


parada = 100
primeiroNumero = 3333
segundoNumero = 3333
c = 0

while parada != 0:
    menu = int(
        input(
            " usuario, o que vc deseja fazer? \n"
            + " 1: somar dois numeros \n"
            + " 2: diminuir dois numeros \n"
            + " 3: fatorial de um numero \n"
            + " 0: para sair \n : "
        )
    )

    if menu == 1:
        primeiroNumero = int(input("informe o primeiro numero: "))
        segundoNumero = int(input("informe o segundo numero: "))
        print(
            f"\n O resultado da Soma dos numeros {primeiroNumero} e {segundoNumero} é: {soma(primeiroNumero, segundoNumero)} \n\n")

    elif menu == 2:
        primeiroNumero = int(input("informe o primeiro numero: "))
        segundoNumero = int(input("informe o segundo numero: "))
        print(
            f"\n O resultado da Subtração dos numeros {primeiroNumero} e {segundoNumero} é: {subtrair(primeiroNumero, segundoNumero)} \n\n")

    elif menu == 3:
        primeiroNumero = int(input("informe o numero: "))
        print(f"\n O resultado do fatorial do numero {primeiroNumero} é: {fat(primeiroNumero)} \n\n")

    elif menu != 0:
        print("\n informe uma opcao valida \n\n")

    parada = menu

print(
    "\n\n-------------------------------\n"
    + "Programa finalizado com sucesso \n"
    + "-------------------------------\n\n"
)

# TESTES:
# print(f"fatorial: {fat(3)}")
# print(f"soma: {soma(3, 2)}")
# print(f"diminuir: {subtrair(5,3)}")
# print(f"O resultado de C é: {c}")