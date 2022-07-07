'''k  = 1
fat = 1
n = int(input('Digite um número:  '))
while k <= n:
    fat = fat*k
    k = k + 1
print(f'fat({n}) = {fat}')'''


soma = 0
n = 0
while True:
    x = int(input('n (zero sai): '))
    if x == 0:
        break
    else:
        n = n + 1
    soma = soma + x
print(f'Soma: {soma/n}')