'''inicio = int(input('Digite um ponto de partida: '))
fim = int(input('Digite um ponto de parada: '))
passo = int(input('Digite o salto dos números: '))
if inicio > fim:
    for n in range(inicio, fim-1, - passo):
        print(n, end=' ')
else:
    for n in range(inicio, fim+1, passo):
        print(n, end=' ')
print('Acabou!')

inicio = int(input('Digite um ponto de partida: '))
fim = int(input('Digite um ponto de parada: '))
passo = int(input('Digite o salto dos números: '))
if inicio > fim:
    inicio , fim = fim, inicio
    for n in range(inicio, fim+1, passo):
        print(n, end=' ')
else:
    for n in range(inicio, fim+1, passo):
     print(n, end=' ')
print('Acabou!')'''

x = int(input('Digite início: '))
y = int(input('Digite o ponto de parada: '))
z = int(input('Digite o salto: '))
if x > y:
    x, y = y, x
while x < y:
     print(x, end=' ')
     x += z
print('Acabou')