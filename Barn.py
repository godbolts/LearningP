class Taluloom:
    def __init__(self, nimetus, kaal, vanus):
        self.nimetus = nimetus
        self.kaal = kaal
        self.vanus = vanus

    def toit(self):
        arv = round((self.kaal* 0.2), 2)
        return arv

    def pesu(self):
        if self.vanus <= 5:
            return 1
        elif  5 < self.vanus <= 10:
            return 3
        else:
            return 5

class Hobune(Taluloom):
    def hääl(self):
        print('Hiii!')

class Siga(Taluloom):
    def hääl(self):
        print('Röh-röhh.')

class Lammas(Taluloom):
    def hääl(self):
        print('Mää...')

hobune = Hobune('Täpi', 100, 7)
siga = Siga('Hort', 70, 2)
lammas = Lammas('Peet', 50, 11)

hobune.hääl()
print(siga.toit())
print(lammas.pesu())