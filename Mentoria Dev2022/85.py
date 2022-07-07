vetorNome = []
vetorSexo = []
vetorSalario = []
indice = []

for i in range(0, 2):
    nome = (input('Digite o nome: '))
    vetorNome.append(nome)
    sexo = (input('Digite o sexo: '))
    vetorSexo.append(sexo)
    salario = int(input('Digite o Salario: '))
    vetorSalario.append(salario)

for i in vetorSalario:
    if i > 5000:
        indice.append(i)

print(i)


