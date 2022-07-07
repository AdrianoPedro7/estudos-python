class Pilha:
    def __init__(self):
        self.pilha = []

    def empilha(self, e):
        self.pilha.append(e)

    def topo(self):
        return self.pilha[len(self.pilha) - 1]

    def desempilha(self):
        if not self.vazia():
            return self.pilha.pop()
        else:
            print('a pilha esta vazia')

    def tamanho(self):
        return len(self.pilha)

    def vazia(self):
        return self.tamanho() == 0

    def verificaParentes(self):
        pilha = Pilha()
        for i in self:
            if i == '(':
                pilha.empilha(i)
            else:
                if pilha.vazia():
                    return False
                else:
                    pilha.desempilha()

        if pilha.vazia():
            print('Está correto')
        else:
            print('Está incorreto')

Pilha.verificaParentes('((()))')



