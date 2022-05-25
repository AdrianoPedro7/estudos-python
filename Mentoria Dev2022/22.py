'''from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print(f'Ainda faltam {18-idade} para se alistar')
else:
    print(f'Já se passaram {idade-18} anos para se alistar')'''

ano = int(input('Digite o ano de nascimento: '))
idade = 2022-ano
if idade < 18:
    print(f'Ainda faltam {18-idade} anos para se alistar')
else:
    print(f'Já se passaram {idade-18} anos para se alistar')