'''vetor = [1]
for i in range(0, 51, 5):
    vetor = i
    print(f'[{vetor}]', end='')





    def formatar(valor, tamanho):
    return f'{valor:> {tamanho}}'

vetor = []
for i in range(0, 51, 5):
    vetor.append(i)

if vetor:
    indice = []
    valor = []
    for c, v in enumerate(vetor):
        tamanho = max(len(str(c)), len(str(v))) + 2
        indice.append(formatar(c, tamanho))
        valor.append(formatar(v, tamanho))

print(f'Indice:', ','.join(indice) )
print(f'Valor: '  , ','.join(valor) )

'''
vetor = []
for i in range(0, 51, 5):
    vetor.append(i)
print(vetor, end='   ')
print()
for c, v in enumerate(vetor):
    print(f' {c} ', end=' ')