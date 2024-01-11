def sünnikuupäev(isikukood):
    kuude_sõnastik = {"01": "jaanuar", "02": "veebruar", "03": "märts", "04": "aprill", "05": "mai", "06": "juuni", "07": "juuli", "08": "august", "09": "september", "10": "oktoober", "11": "november", "12": "detsember"}
    esimene = int(isikukood[0])
    eelmine = False

    if esimene <= 4:
        eelmine = True
    aasta = int(isikukood[1:3])
    if eelmine:
        aasta = 1900 + aasta
    else:
        aasta = 2000 + aasta
    a_kuu = isikukood[3:5]
    kuu = kuude_sõnastik.get(a_kuu, 'Tundmatu kuu')
    päev = isikukood[5:7]

    return f'{päev}. {kuu} {aasta}'

print(sünnikuupäev('59609060267'))
#34501234215