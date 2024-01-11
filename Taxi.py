def odavaim(kilomeetrid):
    kõigi_maksumus = []
    nimed = []

    for row in vastus:
        alustamine = row[1]
        sõitmine = kilomeetrid * row[2]
        kokku = alustamine + sõitmine
        nimed.append(row[0])
        kõigi_maksumus.append(kokku)

    väikseim = min(kõigi_maksumus)
    väikseim_intex = kõigi_maksumus.index(väikseim)
    kompanii = nimed[väikseim_intex]

    return kompanii

väljastatav = r'C:\Users\37259\Desktop\taksohinnad.txt'
a = ['Maksitaksi', 2.0, 0.6]
b = ['Sõps veab', 10, 0]
c = ['Waldo takso', 1.0, 1.0]
d = ['Bolt', 3.0, 1.0]
e = ['Bingo Auto', 4.0, 2.0]
f = ['Mesilased', 2.0, 1.0]
g = ['Veatavad', 10, 1]
nimekiri = [a, b, c, d, e, f, g]

with open(väljastatav, 'w') as tekstifail:
    for element in nimekiri:
        tekstifail.write(', '.join(map(str, element)) + '\n')
taksod = r'C:\Users\37259\Desktop\taksohinnad.txt'
vastus = []

with open(taksod, 'r') as andmed:
    for rida in andmed:
        sõnad = rida.split(',')
        name = sõnad[0].strip()
        numbrid = []
        for sõna in sõnad[1:]:
            try:
                numbrid.append(float(sõna.strip()))
            except ValueError:
                numbrid.append(None)
        rida = [name] + numbrid
        vastus.append(rida)

pikkus = float(input('Palun sisestage tee pikkus kilomeetrites: '))
print(f'Kõige odavam on {odavaim(pikkus)}')