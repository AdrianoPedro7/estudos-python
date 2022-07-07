'''vetor = [1]
for a in range(1):
    vetor[a] = 999
    for b in range(0,8):
        print(vetor,end=' ')
print()
for c in range(0, 9):
    print(f'{c}', end='')'''
indice = []
vetor = []
num = 999
for a in range(0, 8):
    vetor.append(num)
print(vetor, end=' ')
print()

for c, v in enumerate(vetor):
    indice.append(c)
    print(f' [{c}]', end=' ')
print()
print(indice)




