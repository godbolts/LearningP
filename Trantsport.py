class Auto:
    def __init__(self, automärgi_nimi, läbisõit, kütusekulu, kütusetüüp):
        if kütusetüüp not in ['bensiin', 'diisel']:
            raise ValueError('Vale kütusetüüp! peab olema kas bensiin või diisel')
        self.automärgi_nimi = automärgi_nimi
        self.läbisõit = läbisõit #Kilomeetrites
        self.kütusekulu = kütusekulu  #100 kilomeetri kohta
        self.kütusetüüp = kütusetüüp

    def kütuse_maksumus(self, t_pikkus):
        if t_pikkus <= 0:
            return 'Teekonna pikkus on vigane, kas null või negatiivne.'
        b_hind = 1.9
        d_hind = 1.8
        if self.kütusetüüp == 'bensiin':
            info = t_pikkus * (self.kütusekulu / 100)
            hind = b_hind * info
        elif self.kütusetüüp == 'diisel':
            info = t_pikkus * (self.kütusekulu / 100)
            hind = d_hind * info
        return round(hind, 2)

class Lennuk:
    def __init__(self, nimi, maksimum, keskmine, kütusekulu):
        self.nimi = nimi
        self.maksimum = maksimum
        self.keskmine = keskmine  # km/h
        self.kütusekulu = kütusekulu  # 100 reisija kohta

class Reis:
    def __init__(self, lennuk, sihtkoht, pikkus, piletid):
        self.lennuk = lennuk
        self.sihtkoht = sihtkoht
        self.pikkus = pikkus
        self.piletid = piletid

    def reisi_kestus(self):
        kestus = self.pikkus / self.lennuk.keskmine
        return f'Reisi kestus on {int(kestus * 60)} minutit.'

    def vabu_kohti(self):
        kohad = self.lennuk.maksimum - self.piletid
        if kohad < 0:
           raise ValueError('Kohti ei saa miinuses olla')
        elif kohad == 0:
            return 'Kõik kohad on täis'
        else:
            return f'Vabade kohtade arv reisile sihtkohta Madrid on {kohad}.'

    def osta_pilet(self):
        ajutine = self.piletid + 1
        if ajutine > self.lennuk.maksimum:
            raise ValueError('Lennukis pole piisavalt kohti.')
        ajutine_2 = self.lennuk.maksimum - ajutine
        if ajutine_2 < 0:
            return 'Kahjuks kohad on täis.'
        else:
            self.piletid += 1
            return 'Pilet ostetud.'

    def reisi_kütusekulu(self):
        kütus = (self.pikkus / 100) * self.lennuk.kütusekulu * (self.piletid / 100)
        return f'Kütusekulu lendamiseks sihtkohta Madrid on {int(kütus * 100)} liitrit.'

boeng = Lennuk("Boeing-767", 123, 800, 4)
hisp = Reis(boeng, "Madrid", 3500, 110)

print(hisp.reisi_kestus())
print(hisp.vabu_kohti())
print(hisp.osta_pilet())
print(hisp.vabu_kohti())
print(hisp.reisi_kütusekulu())