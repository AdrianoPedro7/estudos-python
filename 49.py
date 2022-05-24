'''x = 0
y = 0
for n in range(1, 7):
    num = int(input(f'{n} Número: '))
    if num % 2 == 0:
        x += 1
    else:
        y += 1

print(f'O total de números par foi: {x}')
print(f'O total de números impar foi: {y}')'''

x = 0
y = 0
w = 0
while w < 6:
    z = num = int(input(f'{w+1} Número: '))
    w += 1
    if num % 2 == 0:
        x += 1
        
    else:
        y += 1
        

print(f'O total de números pares foi: {x}')
print(f'O total de números pares foi: {y}')