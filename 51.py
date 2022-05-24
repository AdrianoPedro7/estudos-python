x = 0
y = 0
maior = 0
menor = 99999999
while x < 8:
    z = int(input(f'Digite o valor do produto: '))
    x += 1
    y += z
    if z > maior:
        maior = z
    if z < menor:
        menor = z

print(f'O maior valor foi {maior:.2f} e o menor valor foi {menor:.2f}')