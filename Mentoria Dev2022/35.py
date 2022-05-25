carro = ('','Popular','Luxo')
print('''Opções de carro:
[1] Popular
[2] Luxo''')
car = int(input('Escolha o tipo de carro desejado: '))
if car < 1 or car > 2:
    print('Opção Inválida')
    print('Fim')
else:
    km = float(input('Quantos km foram percorridos? '))
    dia = float(input('Quantos dias foram usados? '))
    if car == 1:
        if km <= 100:
            print(f'O valor total foi de {(dia*90)+(km *0.20):.2f}')
        else:
            print(f'O valor total foi de {(dia * 90) + (km * 0.10):.2f}')
    else:
        if km <= 200:
            print(f'O valor total foi de {(dia * 150) + (km * 0.30):.2f}')
        else:
            print(f'O valor total foi de {(dia * 150) + (km * 0.25):.2f}')

