class Sõiduk:
    def __init__(self, mark, hind, kütusekulu):
        self.mark = mark
        self.hind = hind
        self.kütusekulu = kütusekulu  # Kilomeetri kohta

    def __str__(self):
        return f'{self.mark}, {self.hind}, {self.kütusekulu}'


class Veoauto(Sõiduk):
    def sõidu_maksumus(self, teepikkus):
        kütus = 1.8
        maksumus = kütus * (teepikkus * (self.kütusekulu / 100))
        return f'Tartu-Tallinna vahemaa läbimiseks kulub {round(maksumus, 1)} eurot.'

    def hobujõud(self):
        hobujõud = 500
        return f'Veoautol on {hobujõud} hobujõudu.'


class Sõiduauto(Sõiduk):
    def sõidu_maksumus(self, teepikkus):
        kütus = 1.9
        maksumus = kütus * (teepikkus * (self.kütusekulu / 100))
        return f'Tartu-Tallinna vahemaa läbimiseks kulub {round(maksumus, 1)} eurot.'

    def hobujõud(self):
        hobujõud = 180
        return f'Sõiduautol on {hobujõud} hobujõudu.'


class Mootorratas(Sõiduk):
    def sõidu_maksumus(self, teepikkus):
        kütus = 1.85
        maksumus = kütus * (teepikkus * (self.kütusekulu / 100))
        return f'Tartu-Tallinna vahemaa läbimiseks kulub {round(maksumus, 1)} eurot.'

    def hobujõud(self):
        hobujõud = 85
        return f'Mootorrattal on {hobujõud} hobujõudu.'


class Garaaž:
    def __init__(self):
        self.järjend = []

    def lisa_sõiduk(self, sõiduk):
        self.järjend.append(sõiduk)

    def kuva(self):
        for sõiduk in self.järjend:
            print(f'{sõiduk.mark}, hind {sõiduk.hind} eurot, kütusekulu 100 km kohta {sõiduk.kütusekulu} liitrit')

            if hasattr(sõiduk, 'hobujõud'):
                hobujõud = sõiduk.hobujõud()
                print(hobujõud)

            if hasattr(sõiduk, 'sõidu_maksumus'):
                maksumus = sõiduk.sõidu_maksumus(186)
                print(maksumus)


gr = Garaaž()
asukoht = r'C:\Users\37259\Desktop\sõidukid.txt'
with open(asukoht, 'r', encoding='UTF-8') as toores:
    for rida in toores:
        tükeldatud = rida.replace('\n', '').split(' - ')
        tükeldatud = [osad.split(', ') for osad in tükeldatud]
        nimi = tükeldatud[0][0]
        mark = tükeldatud[1][0]
        hind = int(tükeldatud[1][1])
        kütusekulu = float(tükeldatud[1][2])
        if nimi == 'Veoauto':
            veoauto = Veoauto(mark, hind, kütusekulu)
            gr.lisa_sõiduk(veoauto)
        elif nimi == 'Sõiduauto':
            sõiduauto = Sõiduauto(mark, hind, kütusekulu)
            gr.lisa_sõiduk(sõiduauto)
        else:
            mootorratas = Mootorratas(mark, hind, kütusekulu)
            gr.lisa_sõiduk(mootorratas)

gr.kuva()