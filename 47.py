'''x = 0
for n in range(450, -1, -50):
    print(n)
    x = x + n

print(f'A soma é: {x}')'''


x = 500
y = 0
while x > 0:
    x -= 50
    print(x)
    y += x
print(f'A soma é: {y}')