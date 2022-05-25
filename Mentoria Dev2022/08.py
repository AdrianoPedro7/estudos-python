medida = float(input('Digite uma distanicia em metros:'))
km = medida/1000
hm = medida/100
dam = medida/10
mm = medida*1000
cm = medida*100
dm = medida*10
print(f'A distância de {medida}m corresponde a:\n{km}km  {hm}hm {dam}dam \n{dm}dm {cm}cm {dm}mm')
