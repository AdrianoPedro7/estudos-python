vetor = []

for a in range(0, 5):
    vetor.append(5)
    vetor.append(3)
print(vetor, end=' ')
print()
for c, v in enumerate(vetor):
    print(f'{c}', end='  ')