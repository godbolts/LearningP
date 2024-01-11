class Tõukeratas:
    def __init__(self, firma_nimi, a_tasu, saja_h, sõidukaugus):
        self.firma_nimi = firma_nimi
        self.a_tasu = a_tasu
        self.saja_h = saja_h
        self.sõidukaugus = sõidukaugus

    def sõidu_hind(self, pikkus):
        if pikkus > self.sõidukaugus:
            tasu = 1000
        else:
            tasu = self.a_tasu + (self.saja_h * (pikkus * 10))
        return tasu  # Return the calculated price

    def sõida(self, pikkus):
        self.sõidukaugus -= pikkus
        if self.sõidukaugus < 0:
            self.sõidukaugus = 0

    def lae(self, kilo_arv):
        self.sõidukaugus += kilo_arv

class Laenutus:
    def __init__(self):
        self.rattad = []

    def lisa(self, ratas):
        self.rattad.append(ratas)

    def kuva_valik(self, pikkus):
        for ratas in self.rattad:
            hind = ratas.sõidu_hind(pikkus)
            print(f'Nimi: {ratas.firma_nimi}, sõidu hind: {hind}')

    def laenuta(self, nimi, pikkus):
        for ratas in self.rattad:
            if ratas.firma_nimi.strip().lower() == nimi.strip().lower():
                if ratas.sõidukaugus >= pikkus:
                    hind = ratas.sõidu_hind(pikkus)
                    ratas.sõida(pikkus)
                    print(f'Laenutatud {ratas.firma_nimi} sõidu hind: {hind}')
                else:
                    print('Distants ületab sõidukaugust.')
                return
        print('Sellist firmat ei ole.')

    def lae_tõukeratast(self, nimi, kilo_arv):
        for ratas in self.rattad:
            if ratas.firma_nimi.strip().lower() == nimi.strip().lower():
                ratas.lae(kilo_arv)
                return
        print('Sellist firmat ei ole.')

ln = Laenutus()

bolt = Tõukeratas("Bolt", 1.5, 0.1, 20)
tuul = Tõukeratas("Tuul", 1, 0.15, 18)
bird = Tõukeratas("Bird", 0, 0.3, 34)

ln.lisa(bolt)
ln.lisa(tuul)
ln.lisa(bird)

ln.laenuta("Bolt", 3)