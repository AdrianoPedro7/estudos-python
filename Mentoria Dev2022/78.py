vetor = []
for i in range(0, 10):
    numero = int(input('Digite um número: '))
    vetor.append(numero)


print(vetor)


for c, v in enumerate(vetor):
    if v % 10 == 0:
        print(f'[{c}]', end=' ')
    else:
        print(c, end=' ')