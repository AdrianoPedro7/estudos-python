x = 0
y = 0
maior18 = 0
menor5 = 0
maior = 0

while x < 10:
    z = int(input(f'Digite a sua idade: '))
    x += 1
    y += z
    #if z > maior:
        #maior = z
    if z < 5:
        menor5 += 1
    elif z > 18:
        maior18 += 1
        if z > maior:
            maior = z

print(f'A média de idade do grupo foi: {y/10}')
print(f'Tivemos {maior18} maiores de 18 anos')
print(f'Tivemos {menor5} menores de 5 anos')
print(f'A maior idade do grupo foi: {maior}')