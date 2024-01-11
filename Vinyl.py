class Plaat:
    def __init__(self, nimi, žanr, ilmumisaasta):
        self.nimi = nimi
        self.žanr = žanr
        self.ilmumisaasta = ilmumisaasta

    def __str__(self):
        return f'{self.nimi}, {self.žanr}, {self.ilmumisaasta}'

class Rock(Plaat):
    def __init__(self, nimi, ilmumisaasta):
        super().__init__(nimi, 'Rock', ilmumisaasta)
    def maksumus(self, arv):
        hind = 2.5
        maksumus = arv * hind
        return maksumus

class Pop(Plaat):
    def __init__(self, nimi, ilmumisaasta):
        super().__init__(nimi, 'Pop', ilmumisaasta)
    def maksumus(self, arv):
        hind = 1.7
        maksumus = arv * hind
        return maksumus

class Klassika(Plaat):
    def __init__(self, nimi, ilmumisaasta):
        super().__init__(nimi, 'Klassika', ilmumisaasta)
    def maksumus(self, arv):
        hind = 2.9
        maksumus = arv * hind
        return maksumus

class Plaadilaenutus:
    def __init__(self):
        self.järjend = []

    def lisa(self, plaat):
        self.järjend.append(plaat)

    def kuva(self):
        for plaat in self.järjend:
            print(f'{plaat.nimi},  {plaat.žanr}, {plaat.ilmumisaasta}')

    def laenuta(self):
        palju = float(input('Mitu eurot on sul plaatide laenutamiseks? '))
        print('-------------------------\nRockmuusika plaatide laenutus maksab 2.5 eurot päevas.\n'
              'Popmuusika plaatide laenutus maksab 1.7 eurot päevas.\n'
              'Klassikalise muusika plaatide laenutus maksab 4.9 eurot päevas.\n'
              '-------------------------\nK - kuva laenutuses olevad plaadid\n'
              'L <plaadi_nimi> <päevade_arv> - laenuta antud nimega plaat nii mitmeks päevaks\n'
              'T <plaadi_nimi> <plaadi_žanr> <plaadi_ilmumisaasta> - tagasta plaat\n'
              'V - välju laenutusest')

        while True:
            print(f'-------------------------\nRaha jääk on {palju} eurot.')
            sisend = input('Sisesta käsk. ')
            if sisend == 'K':
                self.kuva()
            elif sisend.startswith('L '):
                tükeldatud = sisend.split(' ', 2)
                if len(tükeldatud) == 3:
                    nimi = tükeldatud[1]
                    päevade_arv = int(tükeldatud[2])
                    for plaat in self.järjend:
                        if plaat.nimi == nimi:
                            hind = plaat.maksumus(päevade_arv)
                            if palju >= hind:
                                palju -= hind
                                self.järjend.remove(plaat)
                            else:
                                print('Pole küllalt raha.')
                                break
                else:
                    print('Pole laenutuses')
            elif sisend.startswith('T '):
                    tükeldatud = sisend[2:].split(' ')
                    ilmumisaasta = int(tükeldatud[-1])
                    žanr = tükeldatud[-2]
                    if tükeldatud != 'Rock' or tükeldatud != 'Pop' or tükeldatud != 'Klassika':
                        nimi = tükeldatud[0] + ' ' + tükeldatud[1]
                    else:
                        nimi = tükeldatud[0]
                    if žanr == 'Rock':
                        kogumik = Rock(nimi, ilmumisaasta)
                        pl.lisa(kogumik)
                        print(f'Plaat {nimi} tagastatud,')
                    if žanr == 'Pop':
                        kogumik = Pop(nimi, ilmumisaasta)
                        pl.lisa(kogumik)
                        print(f'Plaat {nimi} tagastatud,')
                    if žanr == 'Klassika':
                        kogumik = Klassika(nimi, ilmumisaasta)
                        pl.lisa(kogumik)
                        print(f'Plaat {nimi} tagastatud,')
            elif sisend == 'V':
                break

pl = Plaadilaenutus()

nevermind = Rock("Nevermind", 1991)
thriller = Pop("Thriller", 1982)
sümfoonia = Klassika("Sümfoonia nr 40", 1788)

pl.lisa(nevermind)
pl.lisa(thriller)
pl.lisa(sümfoonia)
pl.laenuta()