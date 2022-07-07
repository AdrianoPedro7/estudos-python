from random import randint

vetor = []
for i in range(0, 30):
        vetor.append(randint(0, 15))
numero = int(input('Digite o número que deseja consultar: '))
print(vetor)
for c, v in enumerate(vetor):
        if numero == v:
                print(f'O número foi encontrado na posicão: {c}')