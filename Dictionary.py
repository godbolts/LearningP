tekst_1 = input('Palun sisestage siia esimese faili nimi: ')
tekst_2 = input('Palun sisestage siia teise faili nimi: ')
esimene_fail = r'C:\Users\37259\Desktop\\' + tekst_1 + '.txt'
teine_fail = r'C:\Users\37259\Desktop\\' + tekst_2 + '.txt'
andmed_üks = []
andmed_kaks =[]

with open(esimene_fail, 'r') as nimed:
    for r in nimed:
        a = r.replace('\n', '')
        andmed_üks.append(a)

with open(teine_fail, 'r') as nimed_2:
    for r in nimed_2:
        a = r.replace('\n', '')
        andmed_kaks.append(a)

sõnaraamat = {andmed_üks[0]: int(andmed_kaks[0]), andmed_üks[1]: int(andmed_kaks[1]), andmed_üks[2]: int(andmed_kaks[2]),
              andmed_üks[3]: int(andmed_kaks[3]), andmed_üks[4]: int(andmed_kaks[4])}

uuendatud_sõnaraamat = sorted(sõnaraamat)
väljastatav = r'C:\Users\37259\Desktop\võitjad.txt'

with open(väljastatav, 'w') as uus:
    for andmed in uuendatud_sõnaraamat:
        uus.write(andmed + '\n')