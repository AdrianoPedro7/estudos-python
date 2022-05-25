media = 0
menor = 0
cont = 0
x = 0

while True:
    idade = int(input(f'Digite uma idade: '))
    cont += x
    x += 1
    media += idade
    parada = input('Deseja continuar? ').upper()
    if idade < 21:
        menor+=1
        if parada == 'NÃO':
            break
    elif parada == 'NÃO':
            break





print(f'A média de idade do grupo foi: {media/cont}')
print(f'Tivemos {cont} idades digitadas')
print(f'Tivemos {menor} pessoas menores de 21 anos')
