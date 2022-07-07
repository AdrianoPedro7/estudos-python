def Maior(a, b, c):
    if a > b and a > c:
        return a

    elif b > a and b > c:
        return b

    else:
        return c


print(f'O número maior é: {Maior(8, 9, 8)}')
