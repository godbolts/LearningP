def loe_sisse(failinimi):
    asukoht = r'C:\Users\37259\Desktop\\' + failinimi + '.txt'
    sõnastik = []

    with open(asukoht, 'r', encoding = 'UTF-8') as andmed:
        for rida in andmed:
            kontakt = {}
            esimene = rida.replace('\n', '').split(';')
            for element in esimene:
                järjend = element.split('=')
                kontakt[järjend[0]] = järjend[1]
            sõnastik.append(kontakt)

    return sõnastik

def kirjuta_faili(list, failinimi):
    asukoht = r'C:\Users\37259\Desktop\\' + failinimi + '.txt'

    with open(asukoht, 'w', encoding = 'UTF-8') as andmed:
        for element in list:
            for index, (key, value) in enumerate(element.items()):
                andmed.write('%s=%s' % ( key, value))
                if index < len(element) - 1:
                    andmed.write(';')

            andmed.write('\n')

järjend_sõnastikest = loe_sisse('kontaktid')

for i, sõnastik in enumerate(järjend_sõnastikest):
    print(f"{i}: {sõnastik}")

number = int(input('Palun sisestage siia järjekorra number millisele kontaktile te soovite lisada juurde andmeid: '))
võti = input('Palun kirjutage siia mis andmeid te soovite loetellu salvestada: ')
väärtus = input('Palun kirjutage siia mis nende andmete sisu on: ')

if number < len(järjend_sõnastikest) and võti and väärtus:
    järjend_sõnastikest[number][võti] = väärtus
else:
    print('Palun lisage mingeid andmeid')

kirjuta_faili(järjend_sõnastikest, 'kontaktid')