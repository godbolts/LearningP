class Raamat:
   def __init__(self, pealkiri, autor, lehekülje_arv, liik):
       self.pealkiri = pealkiri
       self.autor = autor
       self.lehekülje_arv = lehekülje_arv
       self.liik = liik

   def kuva_info(self):
       print(f'{self.pealkiri}, {self.autor}, {self.lehekülje_arv}, {self.liik}')

class Raamatukogu:
    def __init__(self):
        self.raamatud = []

    def lisa_raamat(self, raamat):
        self.raamatud.append(raamat)

    def kuva_raamatud(self):
        print("Raamatukogus olevad raamatud:")
        for raamat in self.raamatud:
            raamat.kuva_info()

    def laenuta_raamat(self, pealkiri):
        for raamat in self.raamatud:
            if raamat.pealkiri.strip().lower() == pealkiri.strip().lower():
                self.raamatud.remove(raamat)
                return raamat

        return None

rk = Raamatukogu()
asukoht = r'C:\Users\37259\Desktop\raamatud.txt'

with open(asukoht, 'r', encoding='UTF-8') as toores:
        for rida in toores:
            tükeldatud = rida.strip().split(',')
            pealkiri = tükeldatud[0]
            autor = tükeldatud[1]
            lehekülje_arv = int(tükeldatud[2])
            liik = tükeldatud[3]
            raamat = Raamat(pealkiri, autor, lehekülje_arv, liik)
            rk.lisa_raamat(raamat)

rk.kuva_raamatud()

while True:
    sisend = input('Sisesta raamatu pealkiri, mida sa laenutada soovid: ')
    if sisend == '':
        break
    laenutatud_raamat = rk.laenuta_raamat(sisend)
    if laenutatud_raamat is not None:
        print(f'Raamat "{sisend}" edukalt leitud!')
    else:
        print('Ei leidnud sellist raamatut, proovi uuesti!')