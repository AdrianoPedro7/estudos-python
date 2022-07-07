vetor = []
for i in range(9, -1, -1):
    vetor.append(i)
print(vetor, end='  ')
print()
for c, v in enumerate(vetor):
    print(f' {c} ', end='')