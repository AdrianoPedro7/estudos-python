x = 0
media = 0
mediaAlt = 0
b = 0
c = 0
d = 0

while x < 7:
    altura = float(input(f'{x+1} Digite sua altura: '))
    peso = float(input(f'{x+1} Digite seu peso: '))
    x += 1
    mediaAlt += altura

    if altura > 190 and peso > 100:
        d+=1
        if peso > 90:
            b += 1
    elif altura < 160 and peso < 50:
        c+=1


print(f'A média de altura do grupo foi: {mediaAlt/7:.2f}')
print(f'Mais que 90 kg {b}')
print(f'Tem menos que 50kg e menos 1.60m: {c}')
print(f'Tem mais que 90kg e mais 1.90m:  {d}')