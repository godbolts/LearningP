def failist_järjendisse(sõne):
    asukoht = r'C:\Users\37259\Desktop\\' + sõne + '.txt'
    bingo_arvud = []

    with open(asukoht, 'r', encoding='UTF-8') as tekst:
        for rida in tekst:
            bingo = rida.strip().split('\n')
            bingo_2 = ''.join(bingo)
            bing = bingo_2.split()
            bing = [int(i) for i in bing]
            bingo_arvud.append(bing)

    return bingo_arvud

def on_bingo_tabel(tabel):
    esimene = False
    teine = False
    kolmas = False
    neljas = False
    viies = False
    esimene_tulp = [tabel[0][0], tabel[1][0], tabel[2][0], tabel[3][0], tabel[4][0]]
    teine_tulp = [tabel[0][1], tabel[1][1], tabel[2][1], tabel[3][1], tabel[4][1]]
    kolmas_tulp = [tabel[0][2], tabel[1][2], tabel[2][2], tabel[3][2], tabel[4][2]]
    neljas_tulp = [tabel[0][3], tabel[1][3], tabel[2][3], tabel[3][3], tabel[4][3]]
    viies_tulp = [tabel[0][4], tabel[1][4], tabel[2][4], tabel[3][4], tabel[4][4]]

    if min(esimene_tulp) > 0 and max(esimene_tulp) < 16:
        esimene = True

    if min(teine_tulp) > 15 and max(teine_tulp) < 31:
        teine = True

    if min(kolmas_tulp) > 30 and max(kolmas_tulp) < 46:
        kolmas = True

    if min(neljas_tulp) > 45 and max(neljas_tulp) < 61:
        neljas = True

    if min(viies_tulp) > 60 and max(viies_tulp) < 76:
        viies = True

    if esimene and teine and kolmas and neljas and viies:
        return True
    else:
        return False

tabel = failist_järjendisse('s')

print(on_bingo_tabel(tabel))