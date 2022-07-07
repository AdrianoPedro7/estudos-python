primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
soma = 0
final = (primeiroTermo + 10) * razao
for i in range(primeiroTermo, final, razao):
    soma += i
    print(i)

print(f'A soma é: {soma}')