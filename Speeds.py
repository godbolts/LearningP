def summa(u, v):
    arv = (u + v) / (1 + ((u * v) / (299792458/1000)**2))
    return arv

a = float(input('Esimese keha kiirus vaatleja suhtes on: '))
b = float(input('Teise keha kiirus vaatleja suhtes on: '))
c = float(input('Kolmanda keha kiirus vaatleja suhtes on: '))
d = float(input('Neljanda keha kiirus vaatleja suhtes on: '))

arvutus_1 = summa(a, b)
arvutus_2 = summa(arvutus_1, c)
arvutus_3 = summa(arvutus_2, d)

print(f'Kiiruste summa on {arvutus_3} km/s')