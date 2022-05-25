notas = list()
for n in range(0, 2):
    notas.append(float(input('Digite uma nota:')))

nota = sum(notas)/len(notas)
print(f'A média entre {notas[0]} e {notas[1]} é igual a {nota}')