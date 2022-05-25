nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

if media >= 7:
    print(f'Parabéns {nome}!!! \nVocê conseguiu um bom aproveitamento.')
else:
    print(f'{nome} infelizmente você vai precisar se esforçar')
print(f'Média: {media}')

