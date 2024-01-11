def loe_andmed(sõne):
    andmed = r'C:\Users\37259\Desktop\\' + sõne + '.txt'
    järjend = []

    with open(andmed, 'r', encoding = 'UTF-8') as tekst:
        read = tekst.read().splitlines()

        for i in read:
            rida = ''.join(i)
            rida_2 = rida.split(';')
            rida_2 = [int(i) if i.isdigit() else i for i in rida_2]

            for i in rida_2:
                rida_3 = ''.join(i)
            järjend.append(rida_3)

        return järjend

def riik(rida):
    rida_2 = rida.split(',')

    return rida_2[0]

def summa(rida):
    rida_2 = rida.replace(' ', '').split(',')
    rida_2 = [int(i) for i in rida_2 if i.isdigit()]

    return sum(rida_2)

sisend = input('Palun kirjutage siia failinimi: ')
andmed = loe_andmed(sisend)
võitja_riik = riik(andmed[0])
kokku = summa(andmed[0])

for i in andmed[1:]:
    if summa(i) > kokku:
        kokku = summa(i)
        võitja_riik = riik(i)

print(f'Võitja on {võitja_riik} kogusummaga {kokku}')