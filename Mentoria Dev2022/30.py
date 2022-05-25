a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

if a < b + c and b < c + a and c < b + a:
    print('É uma triangulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Não pode ser um triangulo, pois um dos lados é maior que a soma dos outros dois ')