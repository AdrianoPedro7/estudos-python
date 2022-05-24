from random import randint
computador = randint(0,5)
print('Digite um número entre 0 e 5')
jogador = int(input('Qual o seu número? '))
while jogador > 5:
    print('Número inválido')
    print('Digite um número entre 0 e 5')
    jogador = int(input('Qual o seu número? '))
print('')
print('='*30)
print(f'O número sorteado foi: {computador}')
print(f'Você escolheu o número: {jogador}')
if jogador == computador:
    print('Você acertou!!!')
else:
    print('Você não acertou')


