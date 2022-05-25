peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso/(alt * alt)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

print(f'Imc é de: {imc:.1f}')
