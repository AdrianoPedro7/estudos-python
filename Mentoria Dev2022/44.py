'''inicio = int(input('Digite um ponto de partida: '))
fim = int(input('Digite um ponto de parada: '))
passo = int(input('Digite o salto dos números: '))

for n in range(inicio, fim, passo):
    print(n, end=' ')
print('Acabou!')'''

x = int(input('Digite início: '))
y = int(input('Digite o ponto de parada: '))
z = int(input('Digite o salto: '))
while x < y:
    print(x, end=' ')
    x += z
print('Acabou!')