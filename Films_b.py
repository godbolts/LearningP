def loetleFilmid(a):
    esimene_fail = r'C:\Users\37259\Desktop\filmid.txt'
    andmed_üks = {}
    with open(esimene_fail, 'r', encoding = 'UTF-8') as nimed:
       for r in nimed:
           tükk = r.strip().split('-')
           if len(tükk) == 2:
               filmid, žanr = tükk[0].strip(), tükk[1].strip()
           andmed_üks[filmid] = žanr
    vastus = []
    for filmid, žanr in andmed_üks.items():
        if žanr == a:
            vastus.append(filmid)

def lisaFilm(nimi, tüüp):
    esimene_fail = r'C:\Users\37259\Desktop\filmid.txt'
    with open(esimene_fail, 'a', encoding='UTF-8') as nimed:
        uus_rida = f'{nimi} - {tüüp}'
        nimed.write(uus_rida + '\n')

def kustutaFilm(nimi):
    esimene_fail = r'C:\Users\37259\Desktop\filmid.txt'
    with open(esimene_fail, 'r', encoding = 'UTF-8') as asi:
        read = asi.readlines()
    uued_read = []
    for rida in read:
        if nimi not in rida:
            uued_read.append(rida)
    with open(esimene_fail, 'w', encoding='UTF-8') as nimed:
        nimed.writelines(uued_read)


