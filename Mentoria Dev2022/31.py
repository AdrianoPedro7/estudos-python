from random import randint
itens = ( 'Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
if jogador > 2:
    print('Jogada inválida')
else:
    print(f' O computador escolheu {itens[computador]}')
    print(f' O jogador escolheu {itens[jogador]}')
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        else:
            print('O JOGADOR VENCE')

    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        else:
            print('EMPATE')
