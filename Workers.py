def loe_andmed(sõne):
    andmed = r'C:\Users\37259\Desktop\\' + sõne + '.txt'
    järjend = []

    with open(andmed, 'r', encoding = 'UTF-8') as tekst:
        read = tekst.read().splitlines()

        for i in read:
            rida = ''.join(i)
            rida_2 = rida.split(';')
            rida_2 = [int(i) if i.isdigit() else i for i in rida_2]
            järjend.append(rida_2)

        return järjend

def parim_töötaja(andmed, kuu):
    esimene = andmed[0][kuu]
    teine = andmed[1][kuu]
    kolmas = andmed[2][kuu]

    if esimene > teine and esimene > kolmas:
        return andmed[0][0]
    elif teine > esimene and teine > kolmas:
        return andmed[1][0]
    else:
        return andmed[2][0]

andmed = loe_andmed('töötajad')

print(parim_töötaja(andmed, 5))