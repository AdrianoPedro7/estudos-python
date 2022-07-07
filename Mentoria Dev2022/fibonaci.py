n = int(input('Quantidade de sequência: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} {t2}', end=' ')
while cont <= n:
    t3 = t1+t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    cont+=1

for i in range(0, 10):
    t3 = t1+t2
    print(f'{t3}', end=' ')
    t1 = t2
    t2 = t3
    cont+=1


def fibonacci(posicao):
    if posicao <= 1:
        return posicao
    else:
        return fibonacci(posicao -1) + fibonacci(posicao -2)
a = int(input('Digite a posição par o valor: '))
res = fibonacci(a)
print(f'NA posição {a} o valor é {res}')