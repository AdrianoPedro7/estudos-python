vetor = []
for i in range(0, 7):
    nome = input('Digite um nome: ')
    vetor.append(nome)
print(vetor)
vetorReverso = [num for num in reversed(vetor)]
print(vetorReverso)