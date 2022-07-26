def Borda(borda):
    if borda == 1:
        print('+-------=======------+')
    elif borda == 2:
        print('~~~~~~~~:::::::~~~~~~~')
    elif borda == 3:
        print('<<<<<<<<------->>>>>>>')

def Gerador(txt, num, borda):
    Borda(borda)
    for i in range(0, num):
        print(txt)
    Borda(borda)


Gerador(' Aprendendo Portugol', 4, 2)





