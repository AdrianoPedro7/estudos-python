termoUm = 0
termodois = 1
print(f'{termoUm} {termodois}', end=' ')

for i in range(0, 8):
    termoTres = termoUm + termodois
    termoUm = termodois
    termodois = termoTres

    print(f'{termoTres}', end=' ')