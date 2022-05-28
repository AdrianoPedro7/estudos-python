galera = []
pessoa = {}
menoridadeF = 999
maiorIdade = res = homem = mulher = soma = 0


while res != 'N':
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
    galera.append(pessoa.copy())
    res = input('Deseja continuar? (S/N) ').upper()[0]
    while res != 'S' and  res != 'N':
        print('Responda apenas S ou N')
        res = input('Deseja continuar? (S/N) ').upper()[0]


print()
print('A pessoa que teve maior idade foi:')
for i in galera:
    for v in i.values():
        if i['Idade'] > maiorIdade:
            maiorIdade = i['Idade']
for i in galera:
    if i['Idade'] == maiorIdade:
        for k in i.values():

            print(k, end=' ')

print()
print('A mulher que teve menor idade foi:')
for i in galera:
    for v in i.values():
        if i['Sexo'] == 'F' and i['Idade'] < menoridadeF:
            menoridadeF = i['Idade']
for i in galera:
    if i['Idade'] == menoridadeF:
        for e in i.values():
            print(e, end=' ')
print()

print(f'A média de idade do grupo foi: {soma/len(galera):5.2f} anos')
print(f'A quantidade de homens maiores de 30 anos foi: {homem}')
print(f'A quantidade de mulheres menores de 18 anos foi: {mulher}')