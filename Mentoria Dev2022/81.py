vetor = []
maior = []
maiorIdade = []

for i in range(0, 8):
    idade = int(input('Digite uma idade: '))
    vetor.append(idade)

print(f'A media de idade é : {sum(vetor)/len(vetor)}')
print(f'A maior idade é : {max(vetor)}')

for c, v in enumerate(vetor):
    if v > 25:
        maior.append(c)
        if v == max(vetor):
            maiorIdade.append(c)
print(f'As posições que temos pessoas com mais de 25 anos são: ')
print(maior)
print(f'A posição da pessoa com maior idade está na posição: {maiorIdade} ')