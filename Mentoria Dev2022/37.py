
val = float(input('Digite seu salário atual: '))
tem = int(input('Digite quanto tempo tem de empresa: '))
print('''[1] Feminino
[2] Masculino ''')
gen = int(input('Digite seu gênero: '))
if gen < 1 or gen > 2:
    print('Opção inválida')
    print('Fim')
else:
    if gen == 1:
        if tem < 15:
            print(f'Seu novo salário é de: R$ {(val*5/100)+val:.2f}')
        elif tem >= 15 and tem < 20:
            print(f'Seu novo salário é de: R$ {(val*12/100)+val:.2f}')
        else:
            print(f'Seu novo salário é de: R$ {(val * 23/ 100) + val:.2f}')

    else:
        if tem < 15:
            print(f'Seu novo salário é de: R$ {(val*3/100)+val:.2f}')
        elif tem >= 15 and tem < 20:
            print(f'Seu novo salário é de: R$ {(val*13/100)+val:.2f}')
        else:
            print(f'Seu novo salário é de: R$ {(val * 25/ 100) + val:.2f}')
