grupo = []
pessoa = {}
totalmulheres = homemPeso = mediaPesoM = maiorPesoH =    0



for i in range(0, 8):
    pessoa = {'Sexo': input('Sexo: (M/F) ').upper()[0], 'Peso': int(input('Peso: '))}
    if pessoa['Sexo'] == 'M' and pessoa['Peso'] > 100:
        homemPeso += 1
        if pessoa['Peso'] > maiorPesoH:
            maiorPesoH = pessoa['Peso']


    elif pessoa['Sexo'] == 'F':
        totalmulheres += 1
        mediaPesoM += pessoa['Peso']


print(f'Foram cadastradas {totalmulheres} mulheres')
print(f'{homemPeso} tem o peso acima de 100Kg')
print(f'A média de peso das mulheres foi: {mediaPesoM/totalmulheres}Kg')
print (f'O maior peso entre os homes foi {maiorPesoH}Kg')