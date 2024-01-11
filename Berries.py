class Mari:
    def __init__(self, nimetus, kogus):
        self.nimetus = nimetus
        self.kogus = kogus  # kilogrammides

    def __str__(self):
        return f'{self.nimetus}, {self.kogus}'

class Maasikas(Mari):
    def maksumus(self, ujuv):
        hind = 9.0
        maksumus = ((ujuv / 1000.0) * hind)
        return maksumus

    def mitu_marja(self, ostetavad):
        return ostetavad * 125

class Mustikas(Mari):
    def maksumus(self, ujuv):
        hind = 12.0
        maksumus = ((ujuv / 1000.0) * hind)
        return maksumus

    def mitu_marja(self, ostetavad):
        return ostetavad * 425

class Vaarikas(Mari):
    def maksumus(self, ujuv):
        hind = 11.0
        maksumus = ((ujuv / 1000.0) * hind)
        return maksumus

    def mitu_marja(self, ostetavad):
        return ostetavad * 260

class Marjapood:
    def __init__(self):
        self.järjend = []

    def lisa(self, mari):
        self.järjend.append(mari)

    def kuva(self):
        for mari in self.järjend:
            print(f'{mari.nimetus} ja  {mari.kogus}')

    def pood(self):
        print('Tere tulemast marjapoodi!\n'
              'Poes on olemas järgmised marjad:\n'
              'Maasikas - 10 kg\nMustikas - 7 kg\nVaarikas - 4.5 kg\n'
              '-------------\nSaad anda järgmisi käske:\nK - kuva poes olevad marjad ja nende kogused\n'
              'O <marja_nimi> <kogus_grammides> - osta marju kindlas koguses\nL - lahku poest)')
        palju = float(input('Mitu eurot sul on? '))
        while True:
            print(f'-------------------------\nRaha jääk on {palju} eurot.')
            sisend = input('Sisesta käsk. ')
            if sisend == 'K':
                self.kuva()
            elif sisend.startswith('O '):
                tükeldatud = sisend.split(' ', 2)
                nimi = tükeldatud[1].strip().lower()
                kogus = float(tükeldatud[2]) / 1000
                hind = 0.0
                for mari in self.järjend:
                    if nimi == mari.nimetus:
                        hind = mari.maksumus(kogus)
                for mari in self.järjend:
                    leidsin_nime = False
                    piisavalt_raha = False
                    piisavalt_kogust = False
                    if mari.nimetus == nimi:
                        leidsin_nime = True
                    if hind <= palju:
                        piisavalt_raha = True
                    if mari.kogus >= kogus:
                        piisavalt_kogust = True
                if leidsin_nime and piisavalt_raha and piisavalt_kogust:
                    for mari in self.järjend:
                        palju = palju - hind
                        mari.kogus = mari.kogus - kogus
                        ostetud = mari.mitu_marja(kogus)
                        print(
                            f'{mari.nimetus.capitalize()} läks sulle maksma {hind} eurot ja kokku said {ostetud * 1000} marja')
                if not leidsin_nime:
                    print('Sellist marja poes ei ole!')
                if not piisavalt_raha:
                    print('Sul pole piisavalt raha!')
                if not piisavalt_kogust:
                    print(f'Marja {nimi.capitalize()} pole piisavalt')
            elif sisend == 'L':
                break
            else:
                print('Selline käsk ei ole lubatud')

maasikas = Maasikas('Maasikas', 10)
mustikas = Mustikas('Mustikas', 7)
vaarikas = Vaarikas('Vaarikas', 4.5)

pood = Marjapood()
pood.lisa(maasikas)
pood.lisa(mustikas)
pood.lisa(vaarikas)

pood.pood()