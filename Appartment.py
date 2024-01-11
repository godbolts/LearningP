import statistics as s
import random as r

class Inimene:
    def __init__(self, vanus, kuupalk):
        self.vanus = vanus
        self.kuupalk = kuupalk

class Hoone:
    def __init__(self, tüüp, kogupind):
        self.tüüp = tüüp
        self.kogupind = kogupind
        self.järjend = []

    def elanikud(self, arv):
        for i in range(arv):
            inimene = Inimene(r.randint(0, 100), r.randint(600, 6000))
            self.järjend.append(inimene)

    def __str__(self):
        return f'{self.tüüp}, {self.kogupind}, {self.järjend}'

    def keskmine_vanus(self):
        keskmine = round(s.mean([inimene.vanus for inimene in self.järjend]), 1)
        return keskmine

    def keskmine_palk(self):
        keskmine = round(s.mean([inimene.kuupalk for inimene in self.järjend]), 2)
        return keskmine

class Eramaja(Hoone):
    def ruutmeetri_hind(self):
        return 500000
    def elanikke_korrusel(self):
        arv = len(self.järjend)
        return arv
class Kortermaja(Hoone):
    def ruutmeetri_hind(self):
        return 5000000
    def elanikke_korrusel(self):
        arv = (len(self.järjend) // 9)
        return arv
class Ridaelamu(Hoone):
    def ruutmeetri_hind(self):
        return 3000000
    def elanikke_korrusel(self):
        arv = (len(self.järjend) // 2)
        return arv
class Hotell(Hoone):
    def ruutmeetri_hind(self):
        return 10000000
    def elanikke_korrusel(self):
        arv = (len(self.järjend) // 9)
        return arv

eramaja = Eramaja('Eramaja', 250)
kortermaja = Kortermaja('Kortermaja', 1500)
ridaelamu = Ridaelamu('Ridaelamu', 750)
hotell = Hotell('Hotell', 5000)

eramaja.elanikud(4)
kortermaja.elanikud(27)
ridaelamu.elanikud(10)
hotell.elanikud(45)

print(f'{eramaja.tüüp}:')
print(f'Keskmine vanus: {kortermaja.keskmine_vanus()}')
print(f'Ruutmeetri hind: {ridaelamu.ruutmeetri_hind()}')
print(f'Elanikke korrusel: {hotell.elanikke_korrusel()}')
print(f'Keskmine palk: {hotell.keskmine_palk()}')