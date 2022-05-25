nome = input('Digite seu nome: ')
sexo = input('Qual o seu sexo (M/F) ? ')
valor = float(input('Digite o valor da compra: '))
off1 = valor * 5 / 100
off2 = valor * 13 / 100
if sexo == 'M':
    print(f'Olá {nome} o valor total de sua compra com desconto foi de R${valor - off1:.2f}')
else:
    print(f'Olá {nome} o valor total de sua compra com desconto foi de R${valor - off2:.2f}')
