class Pessoa:
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.ativo = True

    def desativar(self):
        self.ativo = False


pessoa1 = Pessoa('Adriano', 'Masculino', '33')
print(pessoa1.nome)
