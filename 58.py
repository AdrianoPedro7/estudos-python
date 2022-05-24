media = 0
alunos = 0
while True:
    print('Digite "999" para sair ')
    notas = float(input('Digite uma nota: '))
    if notas == 999:
        break
    elif notas != 999:
        media += notas
        alunos+=1

print(f'A média foi : {media/alunos}')
print(f'A Soma de todas as notas foi: {media}')
print(f'A quantidade de alunos da turma é: {alunos}')