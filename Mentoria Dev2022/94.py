
def Fibonacci(num):
    termoUm = 0
    termodois = 1
    print(termodois, end=' >> ')
    for i in range(0, num-1):
        termoTres = termoUm + termodois
        termoUm = termodois
        termodois = termoTres
        print(termoTres, end=' >> ')

    print("FIM")

Fibonacci(9)