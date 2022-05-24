km = int(input('Digite a distancia em Km que deseja percorrer: '))
if km < 200:
    print(f'O valor da viagem é de R${km*0.5:.2f}')
else:
    print(f'O valor da viagem é de R${km*0.45:.2f}')
