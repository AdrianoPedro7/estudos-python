'''resposta = ''
while resposta != 'sim':
    resposta = input('Deseja terminar ? ')

for i in range(1, 11):
if i == 6:
    print('saiu do loop')
    break
else:
    print(i, end=' ')
    '''

while True:
    i = input('Digite "s" para sair: ')
    if i == 's':
        print('Acabou o loop!')
        break


