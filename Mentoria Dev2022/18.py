ano = int(input('Qual o seu ano de nascimento? '))
idade = 2022-ano
if idade > 18:
    print('Você poderá votar nas eleições desse ano')
else:
    print(f'Você ainda tem {idade} e não poderá votar nas eleições desse ano')