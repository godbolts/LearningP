sünnid = r'C:\Users\37259\Desktop\sünnid.txt'
surmad = r'C:\Users\37259\Desktop\surmad.txt'
kuude_sõnaraamat = {}

with open(sünnid, 'r', encoding = 'UTF-8') as sünnifail, open(surmad, 'r', encoding = 'UTF-8') as surmadfail:
     sünni_read = sünnifail.read().splitlines()
     surma_read = surmadfail.read().splitlines()

if len(sünni_read) != len(surma_read):
    raise ValueError('Midagi on valesti pikkustega')

for i in range(0, len(sünni_read), 2):
    kuu = sünni_read[i]
    sünnid = int(sünni_read[i + 1])
    surmad = int(surma_read[i + 1])
    kuude_sõnaraamat[kuu] = [sünnid, surmad]

kokku = 0

for kuu in kuude_sõnaraamat:
    sünnid, surmad = kuude_sõnaraamat[kuu]
    summa = sünnid - surmad
    kokku += summa

    if summa > 0:
        print(f'{kuu} oli iive positiivne {summa} inimese võrra.')

print(f'Lisaks selle aja jooksul oli iive: {kokku}')