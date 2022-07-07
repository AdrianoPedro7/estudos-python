vetor = []
pares = 0
indice = []
for i in range(0, 10):
    numero = int(input('Digite um número: '))
    vetor.append(numero)

#print(vetor)

for c, v in enumerate(vetor):
    if v % 2 == 0:
        pares+=1
        indice.append(c)

print(f'Foram digitados {pares} números pares')
print(f'Nas posíções {indice}', end=' ')


