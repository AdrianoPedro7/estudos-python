vetor = []
mediaAlunos = 0


for i in range(0, 10):
    notas = int(input('Digite uma nota: '))
    vetor.append(notas)

print(f'A media é : {sum(vetor)/len(vetor)}')

print(f'A maior nota digitada foi : {max(vetor)}')

for c, v in enumerate(vetor):
    if v > (sum(vetor)/len(vetor)):
        mediaAlunos+=1
        if v == max(vetor):
            print(f'A maior nota está na posição: {c}')

print(f'A quantidade de alunos acima da média da turma é : {mediaAlunos}')