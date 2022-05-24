x = media = pares = 0

while True:
    idade = int(input(f'Digite a sua idade: '))
    x += 1
    media += idade
    if idade % 2 == 0:
        pares += 1
    parada = input('Deseja continuar? ').upper()

    if parada == 'NÃO':
        break