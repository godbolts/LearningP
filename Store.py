def loe_failist(failinimi):
    sõnaraamat = {}
    asukoht = r'C:\Users\37259\Desktop\\' + failinimi + '.txt'

    with open(asukoht, 'r', encoding='UTF-8') as toores:
        for rida in toores:
            tükeldatud = rida.strip().split(',')
            nimi, hind, värv = tükeldatud
            hind = float(hind)
            if nimi in sõnaraamat:
                andmed = sõnaraamat[nimi]
                andmed[värv] = hind
            else:
                andmed = {}
                andmed[värv] = hind
                sõnaraamat[nimi] = andmed

    return sõnaraamat

def müük(hinnakiri):
    print('Kaupluses on müügil järgmised tooted: ')

    for nimi, väärtused in hinnakiri.items():
        for värv, hind in väärtused.items():
            print(f'{nimi} - {hind}€ ({värv})')

    jooksev = 0.0

    while True:
        ostusoov = input('Sisesta ostusoov: ')
        if ostusoov == '':
            print(f'Tasuda tuleb {jooksev}€.')
            break
        värvus = input('Sisesta toote värvus: ')
        if ostusoov not in hinnakiri:
            print('Sellist toodet ei ole.')
            continue
        if värvus not in hinnakiri[ostusoov]:
            print('Sellise värvusega toodet ei ole.')
            continue
        hind = hinnakiri[ostusoov][värvus]
        jooksev += hind

        print(f'Jooksev summa on {jooksev}€.')

hinnakiri = loe_failist('hinnakiri')

müük(hinnakiri)