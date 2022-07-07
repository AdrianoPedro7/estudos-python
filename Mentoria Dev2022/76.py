from random import randint

vetor = []
for i in range(0, 7):
        vetor.append(randint(0, 999))
print(vetor)
vetorReverso = [num for num in reversed(vetor)]
print(vetorReverso)


