def loe_failist(nimi):
    asukoht = r'C:\Users\37259\Desktop\\' + nimi + '.txt'
    andmed = {}

    with open(asukoht, 'r', encoding='UTF-8') as read:
            for rida in read:
                kogum = rida.strip().split(';')
                kogum_2 = [int(i) if i.isdigit() else i for i in kogum]
                voor = kogum_2[0]
                punktid = kogum_2[1:]
                andmed[voor] = punktid

    return andmed

def leia_keskmine(sõnastik):
    kokku = []

    for key, punktid in sõnastik.items():
        kokku.append(punktid)
        lamendatud = [element for list in kokku for element in list]

    e_keskmine = (sum(lamendatud) / len(lamendatud))
    keskmine = round(e_keskmine, 1)

    return keskmine

sisend = input('Palun sisestage failinimi: ')
sõnastik = loe_failist(sisend)

for key, punktid in sõnastik.items():
    vooru_keskmine = round((sum(punktid) / len(punktid)), 1)
    print(f'{key}u keskmine on: {vooru_keskmine}')

keskmine = leia_keskmine(sõnastik)

print('Kõikide voorude keskmine tulemus on: ', keskmine)