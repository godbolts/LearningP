import matplotlib.pyplot as plt
import statistics as s


class Õpilane:
    def __init__(self, nimed, sugu, keskmine, lemmikaine):
        if sugu not in ['M', 'N']:
            raise ValueError('Sugu peab olema kas M või N')
        self.nimed = nimed
        self.sugu = sugu
        self.keskmine = keskmine
        self.lemmikaine = lemmikaine

    def õpilane(self):
        return self.nimed, self.sugu, self.keskmine, self.lemmikaine


class Kool:
    def __init__(self, kooli_nimi):
        self.kooli_nimi = kooli_nimi
        self.õpilane = []

    def lisa_kooli(self, õpilane):
        self.õpilane.append(õpilane)

    def kuva_info(self):
        print(self.kooli_nimi)
        for i in self.õpilane:
            print(Õpilane.õpilane(i))

    def õppeainete_graafik(self):
        lemmikained = [õpilane.lemmikaine for õpilane in self.õpilane]
        lemmikaine_loend = list(set(lemmikained))
        loend_kogus = [lemmikained.count(lemmikaine) for lemmikaine in lemmikaine_loend]

        plt.figure(figsize=(10, 6))
        plt.bar(lemmikaine_loend, loend_kogus)
        plt.xlabel('Õppeained')
        plt.ylabel('Mitme õpilase lemmikaine')
        plt.title('Lemmikõppeainete graafik')
        plt.xticks(rotation=45)
        plt.show()

    def keskmine_hinne(self):
        m_arv = 0
        n_arv = 0
        m_kesk = []
        n_kesk = []
        for õpilane in self.õpilane:
            if õpilane.sugu == 'M':
                m_arv += 1
                m_kesk.append(õpilane.keskmine)
            elif õpilane.sugu == 'N':
                n_arv += 1
                n_kesk.append(õpilane.keskmine)
        m_k = s.mean(m_kesk)
        n_k = s.mean(n_kesk)
        return f'Meessoost õpilasi on kokku {m_arv} ning nende keskmine hinne on {m_k}\nNaissoost õpilasi on kokku {n_arv} ning nende keskmine hinne on {n_k}'


kl = Kool('Tartu Kesklinna Gümnaasium')
asukoht = r'C:\Users\37259\Desktop\õpilased.txt'
with open(asukoht, 'r', encoding='UTF-8') as toores:
    for rida in toores:
        tükeldatud = rida.replace('\n', '').split(' ')
        if tükeldatud[1] != 'M' and tükeldatud[1] != 'N':
            nimi = ' '.join(tükeldatud[0:2])
        else:
            nimi = tükeldatud[0]
        for i in tükeldatud:
            if i == 'M' or i == 'N':
                sugu = i
        for i in tükeldatud:
            if i.replace('.', '', 1).isdigit():
                keskmine = float(i)
        if not tükeldatud[-2].replace('.', '', 1).isdigit():
            lemmikaine = ' '.join(tükeldatud[-2:])
        else:
            lemmikaine = tükeldatud[-1]
        õpi = Õpilane(nimi, sugu, keskmine, lemmikaine)
        kl.lisa_kooli(õpi)

print(kl.kuva_info())
print(kl.õppeainete_graafik())
print(kl.keskmine_hinne())