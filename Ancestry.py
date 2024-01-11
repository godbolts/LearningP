def on_eellane(sõnastik, e_nimi, t_nimi):
    eelane = False
    for nimi, vanem in sõnastik.items():
        if nimi == e_nimi:
            if t_nimi == vanem[0] or t_nimi == vanem[1]:
                eelane = True
                break
    return eelane

asukoht = r'C:\Users\37259\Desktop\sugupuu.txt'
e_nimi = input('Palun sisestage esimene nimi: ')
t_nimi = input('Palun sisestage teine nimi: ')
sugupuu = {}

vastus = on_eellane(sugupuu, e_nimi, t_nimi)
if vastus:
    pos_neg = 'on'
    sugulus = 'vanem'
else:
    for nimi, vanem in sugupuu.items():
        if on_eellane(sugupuu, e_nimi, nimi):
            pos_neg = 'on'
            sugulus = 'vanavanem'
            break
    else:
        pos_neg = 'ei ole'
        sugulus = 'suguluses'

with open(asukoht, 'r', encoding='UTF-8') as andmed:
    for rida in andmed:
        tükk = rida.strip().split(':')
        u_tükk = tükk[1].replace(' ', '').split(',')
        tervik = [tükk[0], u_tükk]
        nimi = tervik[0]
        isa = tervik[1][0]
        ema = tervik[1][1]
        sugupuu[nimi] = isa, ema

print(f'{e_nimi} {pos_neg} {t_nimi}i {sugulus}.')