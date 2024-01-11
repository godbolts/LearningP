import math as ma

def koogi_hind(nimi, moot):
   if nimi == 'šokolaadikook':
       pindala = ma.pi*moot**2
       hind = round((pindala*0.05), 2)
       return hind
   elif nimi == 'ploomikook':
       pindala = ma.pi * moot ** 2
       hind = round((pindala * 0.04), 2)
       return hind
   elif nimi == 'napoleoni kook':
       pindala = moot ** 2
       hind = round((pindala * 0.08), 2)
       return hind
   else:
       return -1

h = input('Sisesta koogi nimi: ').lower()
m = float(input('Sisesta koogi mõõt: '))

vastus = koogi_hind(h, m)

if vastus != (-1):
   print(vastus)
else:
   print('Sellist kooki pagarikoda ei valmista.')