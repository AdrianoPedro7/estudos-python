x = 0
y = 0
media = 0
homem = 0
mulher = 0
maior = 0
mediaH = 0

while x < 5:
    idade = int(input(f'Digite a sua idade: '))
    sexo = str(input(f'Digite seu sexo(M/F): ')).upper()
    x += 1
    media += idade
    if sexo == 'M':
            homem+=1
            mediaH+=idade
    else:
            mulher+=1




print(f'A média de idade do grupo foi: {media/5}')
print(f'Tivemos {homem} homens cadastrados')
print(f'Tivemos {mulher} mulheres cadastradas')
print(f'A média de idade do grupo de homens foi: {mediaH/homem:.2F}')
