print('Vamos realizar o cálculo do seu desconto')
preco = float(input('Digite o valor do produto:'))
off = preco*5/100
total = preco-off
print(f'Valor do produto:   R${preco}')
print(f'Valor do desconto: -R${off:.2f}')
print(f'Total:              R${total:.2f}')