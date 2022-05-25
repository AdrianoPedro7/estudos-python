print('Vamos cálcular o reajuste salarial')
salario = float(input('Digite o valor do seu salário:'))
aumento = salario*15/100
total = salario+aumento
print(f'Valor do salário atual:  R${salario}')
print(f'Valor do aumento :      +R${aumento:.2f}')
print(f'Salário com aumento:     R${total:.2f}')
