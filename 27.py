nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print(f'Sua média foi: {media:.1f}')

if media <= 4.9:
    print('REPROVADO')
if media >= 5 and media < 7:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')

