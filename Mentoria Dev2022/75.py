vetorIndice = []
vetor = []
termoUm = 0
termodois = 1



vetor.append(termodois)
for i in range(1, 16):
    termoTres = termoUm + termodois
    termoUm = termodois
    termodois = termoTres
    vetor.append(termoTres)

print(vetor, end='')
print()
for c, v in enumerate(vetor):
    vetorIndice.append(c)

    #print(f'{c}', end='   ')
print(f'{vetorIndice}' , end='')