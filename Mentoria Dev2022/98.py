def SuperSomador(a, b):
    n = 0
    for i in range(a, b+1):
        n += i
        print(i, end=' ')

    print(f'A soma é igua a: {n}')



SuperSomador(1, 6)
SuperSomador(15, 19)
