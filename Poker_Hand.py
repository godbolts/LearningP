from collections import Counter

def käsi(esimene, teine, kolmas, neljas, viies):
    sõnastik = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    mastid = [esimene[-1], teine[-1], kolmas[-1], neljas[-1], viies[-1]]
    sümbolid = [esimene[:-1], teine[:-1], kolmas[:-1], neljas[:-1], viies[:-1]]
    väärtused = [sõnastik.get(sümbol, 0) for sümbol in sümbolid]
    suurim = max(väärtused)
    suurim_intex = väärtused.index(suurim)
    kuninglik = True

    def järgnevus(väärtus):
        return sorted(väärtus) == list(range(min(väärtus), max(väärtus) + 1))

    def nelik(numbrid):
        loetud = Counter(numbrid)
        for num, count in loetud.items():
            if count >= 4:
                return True
        return False

    def kolmik(numbrid):
        loetud = Counter(numbrid)
        for num, count in loetud.items():
            if count >= 3:
                return True
        return False

    def paar(numbrid):
        loetud = Counter(numbrid)
        for num, count in loetud.items():
            if count >= 2:
                return True
        return False

    def maja(väärtused):
        loetud = Counter(väärtused)
        kolmik = False
        paar = False
        for num, count in loetud.items():
            if count == 3:
                kolmik = True
            elif count == 2:
                paar = True
        if kolmik and paar:
            return True

    def paarid(väärtused):
        loetud = Counter(väärtused)
        p_arv = 0
        for arv in loetud.values():
            if arv == 2:
                p_arv += 1
        if p_arv == 2:
            return True
        else:
            return False

    for arv in väärtused:
        if arv not in range(10, 15):
            kuninglik = False
            break

    if len(set(mastid)) == 1:
        if kuninglik:
            return 'Kuninglik mastirida'
        elif järgnevus(väärtused):
            return 'Järjestikune mastirida'
        else:
            return 'Mastirida'
    else:
        if nelik(väärtused):
            return 'Nelik'
        elif maja(väärtused):
            return 'Maja'
        elif järgnevus(väärtused):
            return 'Rida'
        elif kolmik(väärtused):
            return 'Kolmik'
        elif paarid(väärtused):
            return 'Kaks paari'
        elif paar(väärtused):
            return 'Üks paar'
        else:
            if suurim_intex == 0:
                kaart = esimene
            elif suurim_intex == 1:
                kaart = teine
            elif suurim_intex == 2:
                kaart = kolmas
            elif suurim_intex == 3:
                kaart = neljas
            else:
                kaart = viies
            return f'Kõrge kaart, milleks on {kaart}'


print(käsi('Q♥', 'K♥', 'J♥', 'A♥', '9♥'))

#♥♦♣♠