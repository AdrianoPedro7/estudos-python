media = 0
homem = 0
mulher = 0
maior = 0
mediaH = 0
x = 0

while True:
    idade = int(input(f'Digite a sua idade: '))
    sexo = str(input(f'Digite seu sexo(M/F): ')).upper()
    x += 1
    media += idade
    parada = input('Deseja continuar? ').upper()
    if sexo == 'M':
        homem+=1
        mediaH+=idade
        if parada == 'NÃO':
            break
    elif sexo == 'F':
        mulher+=1
        if parada == 'NÃO':
            break



print(f'A média de idade do grupo foi: {media/5}')
print(f'Tivemos {homem} homens cadastrados')
print(f'Tivemos {mulher} mulheres cadastrados')
print(f'A média de idade do grupo de homem foi: {mediaH/homem}')