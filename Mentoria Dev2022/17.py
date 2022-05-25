print('Limite de velocidade 80km/h')
vel = int(input('Qual a sua velocidade atual? '))
multa = (vel - 80)*5
if vel > 80:
    print('Você foi multado por ultrapassar o limite de velocidde')
    print(f'Você deverá pagar o valor de R${multa:.2f}')
