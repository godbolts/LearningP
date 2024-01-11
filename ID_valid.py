def tõestus(isikukood):
    pikkus = False
    sugu = False
    aasta = True
    kuu = False
    päev = False

    if len(isikukood) == 11:
        pikkus = True

    if 2 < int(isikukood[0]) < 7:
        sugu = True

    a_aasta = isikukood[1:3]

    if a_aasta[0] == 0:
        a_aasta = a_aasta[1]

    a_aasta = int(a_aasta)

    if isikukood[0] == '5' or isikukood[0] == '6' and a_aasta > 23:
        aasta = False

    a_kuu = isikukood[3:5]

    if a_kuu[0] == 0:
        a_kuu = a_kuu[1]

    a_kuu = int(a_kuu)

    if a_kuu <= 12:
        kuu = True

    a_päev = isikukood[5:7]

    if a_päev[0] == 0:
        a_päev = a_päev[1]

    a_päev = int(a_päev)

    if a_päev <= 31:
        päev = True

    if pikkus and sugu and aasta and kuu and päev:
        return 'õige'
    else:
        return 'vale'

def mat_tõestus(isikukood):
    arvud = [int(isikukood[0]), int(isikukood[1]), int(isikukood[2]), int(isikukood[3]), int(isikukood[4]), int(isikukood[5]),
             int(isikukood[6]), int(isikukood[7]), int(isikukood[8]), int(isikukood[9])]
    i_aste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    ii_aste = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    korrutis = [a * b for a, b in zip(arvud, i_aste)]
    s_summa = sum(korrutis)//11

    if s_summa < 10:
        kontroll = s_summa
    elif s_summa == 10:
        t_korrutis = [a * b for a, b in zip(arvud, ii_aste)]
        t_summa = sum(t_korrutis)//11

        if t_summa < 10:
            kontroll = t_summa
        else:
            kontroll = 0
            print('Katki')
    else:
        kontroll = 0

    if kontroll == int(isikukood[10]):
        vastus = 'õige'
    else:
        vastus = 'vale'

    return vastus

sisestus = input('Palun sisestage kontrollimiseks isikukood: ')
vastus = tõestus(sisestus)
vastus_2 = mat_tõestus(sisestus)

print(f'See isikukood onesimese testi järgi {vastus} ja teise testi järgi {vastus_2}')
