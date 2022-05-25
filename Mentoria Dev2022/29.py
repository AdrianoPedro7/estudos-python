nome = input('Digite seu nome: ')
anos = int(input('Quantos anos de empresa? '))
salario = float(input('Digite o valor de seu salário: '))

if anos <= 3:
    print(f' O funcionário {nome} terá o salário de RS {salario*3/100 +salario}')
elif anos > 3 and anos <= 10:
    print(f'O funcionário {nome} terá o salário de R$ {salario*12.5/100 +salario}')
else:
    print(f' O funcionário {nome} terá o salário de RS {salario*20/100 +salario}')