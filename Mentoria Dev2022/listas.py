'''lista = [6, 8, 7, 5]
x = 0
y = 0
while y < len(lista):
     x = x + lista[y]
     y += 1
print(x)
print(x/len(lista))'''

lista = []
x = 0
y = 0
while x <= 3:
     lista.append(float(input(f'{x+1} Nota: ')))
     y = y + lista[x]
     x = x + 1
print(f'Média {lista} é igual a {y/4}')