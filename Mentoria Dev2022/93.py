def Contador(início, fim, passe):
    for i in range(início, fim, passe):
        print(i, end= " >> ")
    print('FIM')

Contador(4, 20, 3)