import random
import string

def suurväike(sõne):
    ümber_pööratud = ''
    kirjavahemärgid = string.punctuation

    for täht in sõne:
        if täht.islower():
            ümber_pööratud += täht.upper()
        elif täht.isupper():
            ümber_pööratud += täht.lower()
        elif täht in kirjavahemärgid:
            ümber_pööratud += random.choice(kirjavahemärgid)
        else:
            ümber_pööratud += täht

    return ümber_pööratud

tekst = input('Palun sisestage siia failinimi: ')
faili_nimi = r'C:\Users\37259\Desktop\\' + tekst + '.txt'

with open(faili_nimi, 'r+') as tekstifail:
    andmed = tekstifail.read()
    uus_andmed = suurväike(andmed)
    tekstifail.seek(0)
    tekstifail.write(uus_andmed)

    print(uus_andmed)