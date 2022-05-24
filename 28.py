L = float(input('Digite a largura do terreno: '))
C = float(input('Ditite o comprimento do terreno: '))
area = (L + C) / 2
print(f'O terreno tem a area quadrada de {area} m²')

if area <= 100:
    print('TERRENO POPULAR')
elif area >= 100 and area < 500:
    print('TERRENO MASTER')
else:
    print('TERRENO VIP')