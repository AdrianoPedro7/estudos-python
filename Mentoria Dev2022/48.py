'''x = 0
for n in range(1, 8):
    int(input(f'{n} Número: '))
    x = x + n
print(f'A Soma é: {x}')'''


x = 0
y = 0
while x < 7:
    z = int(input(f'{x+1} Número: '))
    x += 1
    y += z
    print(y)
print(f'A soma é: {y}')