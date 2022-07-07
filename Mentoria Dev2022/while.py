'''num = int(input('Digite um numero de parada: '))
x = 0
while x <= num:
    print(x)
    x = x + 2'''

'''n = 1
soma = 0
while n <= 10:
    x = int(input(f'{n} número: '))
    soma = soma + x
    n = n + 1
print(f'Soma: {soma}')'''



'''n = 1
fat = 1
num = int(input('informe um valor: '))
while n <= num:
    fat = fat * n
    n = n + 1
print(f'fat({num}) = {fat}')'''

soma = 0
while True:
    x = int(input('digite os numeros que deseja somar (digite zero para parar): '))
    if x == 0:
        break
    soma = soma + x
print(f'Soma: {soma}')
