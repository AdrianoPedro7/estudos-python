class Calculadora:
    def __init__(self, a,b) -> None:
        self.a=b
        self.b=b
    def somar(self):
        return self.a+self.b
    def subtrair(self):
        return self.a-self.b
    def multiplicar(self):
        return self.a*self.b
    def dividr(self):
        return self.a/self.b

c = Calculadora(5, 7)
print(c.somar())
print(c.multiplicar())