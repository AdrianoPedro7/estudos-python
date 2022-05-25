
x = 0
while x < 4:
    from random import randint
    computador = randint(1, 10)
    print('=' * 30)
    print('Digite um número entre 1 e 10')
    jogador = int(input('Qual o seu número? '))
    x+=1
    print(f'O número sorteado foi: {computador}')
    print(f'Você escolheu o número: {jogador}')
    print('=' * 30)
    if jogador == computador:
        print('')
        print('Você acertou!!!')
        break

    else:
        print('Você não acertou!!!')
        print('')






