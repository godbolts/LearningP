fail_tee = r'C:\Users\37259\Desktop\Kolm.txt'

with open(fail_tee, encoding="UTF-8") as fail:
   esimene = int(fail.readline().strip())
   teine = int(fail.readline().strip())
   kolmas = int(fail.readline().strip())
   neljas = int(fail.readline().strip())
   viies = int(fail.readline().strip())

arvud = [esimene, teine, kolmas, neljas, viies]
paaris = 0
mitu = 0
paaritu = 0
mitu_p = 0

for arv in arvud:
   if arv % 2 == 0:
       paaris += arv
       mitu += 1
   else:
       paaritu += arv
       mitu_p += 1

if mitu > mitu_p:
   print('Paarisarve on rohkem.')
elif mitu == mitu_p:
   print('Mõlemaid on võrdselt')
else:
   print('Paarituid arve on rohkem.')

print('Arvude summa on:', sum(arvud))
print('Paarisarvude summa on:', paaris)
print('Paaritute arvude summa on:', paaritu)