'''for n in range (30, -1, -1):
    if n % 4 == 0:
        print(f'[{n}]', end=' ')
    else:
        print(n, end=' ')
print('Acabou!')'''

x = 31
while x > 1:
    x = x - 1
    if x % 4 == 0:
        print(f'[{x}]', end=' ')
    else:
        print(x, end=' ')
print('Acabou!')