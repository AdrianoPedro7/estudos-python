val = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
num = int(input('Digite quantas prestações deseja pagar: '))
pres = (val/num)
if pres < sal*30/100:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')
print(f'Valor das parcelas: {pres}')


