grupo = []
pessoa = {}
maioridadeF = 999
maiorIdade = homem = mulher = soma = 0
while True:
    pessoa.clear()
    pessoa = {'Nome': input('Nome: '), 'Idade': int(input('Idade: ')), 'Sexo': input('Sexo: (M/F) ').upper()[0]}
    soma+=pessoa['Idade']
    if pessoa['Idade'] > 30 and pessoa['Sexo'] == 'M':
        homem+=1
    elif pessoa['Idade'] < 18 and pessoa['Sexo'] == 'F':
        mulher+=1
    while pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
        print('Digite apenas M ou F')
        pessoa = {'Sexo': input('Sexo: (M/F) ').upper()[0]}
    grupo.append(pessoa.copy())
    res = input('Deseja continuar? (S/N) ').upper()[0]
    while res != 'S' and  res != 'N':
        print('Responda apenas S ou N')
        res = input('Deseja continuar? (S/N) ').upper()[0]
    if res == 'N':
        break

print()
print('A pessoa que teve maior idade foi:')
for i in grupo:
    for v in i.values():
        if i['Idade'] > maiorIdade:
            maiorIdade = i['Idade']
for i in grupo:
    if i['Idade'] == maiorIdade:
        for k in i.values():

            print(k, end=' ')

print()
print('A mulher que teve maior idade foi:')
for i in grupo:
    for v in i.values():
        if  i['Idade'] < maioridadeF:
            maioridadeF = i['Idade']
for i in grupo:
    if i['Idade'] == maioridadeF:
        for e in i.values():
            print(e, end='')
print()

print(f'A média de idade do grupo foi: {soma/len(grupo):5.2f} anos')
print(f'A quantidade de homens maiores de 30 anos foi: {homem}')
print(f'A quantidade de mulheres menores de 18 anos foi: {mulher}')