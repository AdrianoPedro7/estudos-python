


from random import randint
x = 0
y = 0
w = 0
while w < 20:
    num = randint(0, 10)
    w += 1
    print(num, end=' ')
    if num > 5:
        x += 1
    elif num % 3 == 0:
        y += 1


print(f'''
São {x} os números maiores que 5''')
print(f'São {y} os números que podem ser divididos por 3 ')