def seosta_lapsed_ja_vanemad(laste_faili_nimi, nimede_faili_nimi):
    lapsed = r'C:\Users\37259\Desktop\\' + laste_faili_nimi + '.txt'
    nimed = r'C:\Users\37259\Desktop\\' + nimede_faili_nimi + '.txt'
    lapsed_andmed = {}
    nimede_andmed = {}

    with open(lapsed, 'r', encoding='UTF-8') as l_andmed, open(nimed, 'r', encoding='UTF-8') as n_andmed:
        for rida in l_andmed:
            andmed = rida.strip().split(' ')
            isikukood_vanem = andmed[0]
            isikukood_laps = andmed[1]

            if isikukood_laps in lapsed_andmed:
                lapsed_andmed[isikukood_laps].append(isikukood_vanem)
            else:
                lapsed_andmed[isikukood_laps] = [isikukood_vanem]

        for rida in n_andmed:
            andmed = rida.strip().split(' ')
            isikukood = andmed[0]
            nimi = ' '.join(andmed[1:])
            nimede_andmed[isikukood] = nimi

    sõnaraamat = {}

    for lapse_id in lapsed_andmed.keys():
        lapse_nimi = nimede_andmed.get(lapse_id, 'Laps ei ole leitud')
        vanema_ids = lapsed_andmed[lapse_id]
        vanema_nimed = [nimede_andmed.get(vanema_id, 'Vanem ei ole leitud') for vanema_id in vanema_ids]
        vanema_nimed = ', '.join(vanema_nimed)
        sõnaraamat[lapse_nimi] = vanema_nimed

    return sõnaraamat

tagastus = seosta_lapsed_ja_vanemad('lapsed', 'nimed')

for lapse_nimi, vanema_nimed in tagastus.items():
    print(f'{lapse_nimi}: {vanema_nimed}')