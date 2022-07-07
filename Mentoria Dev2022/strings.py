'''texto = 'até cubanos roma'
print(texto[::-1])'''

'''nom = input('Digite uma palavra: ')
if nom == nom[::-1]:
    print('É palindromo')
else:
    print('Não é palindromo')'''


'''nom = input('Digite uma palavra: ')
pali = nom == nom[::-1]
print(f'A palavra {nom}é uma palindromo? {pali}')'''

palavra = input('Palavra: ')
x = 0
troca = ''
while x < len(palavra):
    if palavra[x] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[x]
    x += 1
print(troca)