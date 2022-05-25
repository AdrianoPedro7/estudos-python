horas = float(input('Digite quantas horas de academia: '))
if horas <= 10:
    print(f'Você teve a quantidade de {horas:.2f}Hrs com o total de {horas*2} pontos e receberá R${horas*0.10:.2f} ')
elif horas > 10 and horas <= 20:
    print(f'Você teve a quantidade de {horas:.2f}Hrs com o total de {horas*5} pontos e receberá R${horas*0.25:.2f} ')
else:
    print(f'Você teve a quantidade de {horas:.2f}Hrs com o total de {horas*10} pontos e receberá R${horas*0.50:.2f} ')