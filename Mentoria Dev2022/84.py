vetor = []

for i in range(0, 2):
    pessoa = {'Nome': input('Nome: '), 'Idade': int(input('Idade: '))}
    vetor.append(pessoa.copy())


for i in vetor:
    if i['Idade'] < 18:
        for e in i.values():
            print(e, end=" ")