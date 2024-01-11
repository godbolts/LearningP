import math as ma

pikkus = float(input('Palun sisesta oma ruumi pikkus: '))
laius = float(input('Palun sisesta oma ruumi laius: '))
korgus = float(input('Palun sisesta oma ruumi kõrgus: '))
varvi_pudel =float(input('Palun sisesta kui suured on värvipurgid: '))

pind = 2*(pikkus*korgus) + 2*(laius*korgus)
liitrid = pind/8
arv = ma.ceil((liitrid / varvi_pudel))

print(f'On vaja osta {arv} purki värvi.')