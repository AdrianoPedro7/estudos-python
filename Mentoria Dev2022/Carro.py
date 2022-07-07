class Carro:
    def __init__(self, marca, qtdportas, cor, combustivel, placa, velocidade, velocidadeTotal, marcha, marchaTotal):
        self.marca = marca
        self.qtdportas = qtdportas
        self.cor = cor
        self.combustivel = combustivel
        self.placa = placa
        self.velocidade = velocidade
        self.velocidadeTotal = velocidadeTotal
        self.marcha = marcha
        self.marchaTotal = marchaTotal


    def acelerar(self):
        if not self.velocidade == self.velocidadeTotal:
            self.velocidade = self.velocidade + 2
        else:
            print('Velocidade Máxima Atingida')
            print(self.velocidadeTotal)

    def freiar(self):
        if not self.velocidade == 0:
            self.velocidade = self.velocidade -2
        else:
            print('O carro chegou a 0 Km/H')

    def passarMarcha(self):
        if not self.marcha == self.marchaTotal:
            self.marcha = self.marcha +1
        else:
            print('O carro chegou a marcha total')

    def reduzirMarcha(self):
        if not self.marcha == 0:
            self.marcha = self.marcha -1
        else:
            print('O carro chegou a marcha 0 ')





carro1 = Carro('Ford', '4','Preto', 'flex', 'SDM-5504', 4, 180, 1, 6)

print(carro1.marcha)
carro1.passarMarcha()
print(carro1.marcha)
carro1.reduzirMarcha()
print(carro1.marcha)
carro1.reduzirMarcha()
print(carro1.marcha)
carro1.reduzirMarcha()








