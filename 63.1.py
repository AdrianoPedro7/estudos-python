x = media = pares = 0
menor = 9999

while True:
    idade = int(input(f'Digite um número: '))
    x += 1
    media += idade
    if idade % 2 == 0:
        pares += 1
    elif idade < menor:
        menor = idade
    parada = input('Deseja continuar? (S/N) ').upper()
    while parada != 'S' and  parada != 'N':
        print('Responda apenas S ou N')
        parada = input('Deseja continuar? (S/N) ').upper()[0]
    if parada == 'N':
        break


print(f'A soma do grupo foi:  {media} ')
print(f'O menor número digitado foi: {menor}')
print(f'A média de idade do grupo foi: {media / x}')
print(f'A quantidade de numeros pares foi:  {pares} ')