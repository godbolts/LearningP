def info(isikukood):
    esimene = int(isikukood[0])
    eelmine = False

    if esimene <= 4:
        eelmine = True
    naine = False

    if esimene % 2 == 0:
        naine = True

    if naine:
        sugu = 'naine'
    else:
        sugu = 'mees'

    aasta = int(isikukood[1:3])

    if eelmine:
        aasta = 1900 + aasta
    else:
        aasta = 2000 + aasta

    pärast = False

    if aasta >= 2013:
        pärast = True

    kuu = isikukood[3:5]
    päev = isikukood[5:7]

    if pärast:
        sünnikoht = 'Teadmata'
    else:
        e_haigla_id = isikukood[-4:-1]
        if e_haigla_id[0] == '0':
            e_haigla_id = e_haigla_id[1:]
        if e_haigla_id[0] == '0':
            e_haigla_id = e_haigla_id[1:]
        haigla_id = int(e_haigla_id)
        if haigla_id in range(1, 10):
            sünnikoht = 'Kuressaare haigla'
        elif haigla_id in range(11, 19):
            sünnikoht = 'Tartu Ülikooli Naistekliinik'
        elif haigla_id in range(21, 150):
            sünnikoht = 'Ida-Tallinna keskhaigla või Pelgulinna sünnitusmaja'
        elif haigla_id in range(151, 160):
            sünnikoht = 'Keila haigla'
        elif haigla_id in range(161, 220):
            sünnikoht = 'Rapla haigla, Loksa haigla või Hiiumaa haigla'
        elif haigla_id in range(221, 270):
            sünnikoht = 'Ida-Viru keskhaigla'
        elif haigla_id in range(271, 370):
            sünnikoht = 'Maarjamõisa kliinikum või Jõgeva haigla'
        elif haigla_id in range(371, 420):
            sünnikoht = 'Narva haigla'
        elif haigla_id in range(421, 470):
            sünnikoht = 'Haapsalu haigla'
        elif haigla_id in range(471, 490):
            sünnikoht = 'Järvamaa haigla'
        elif haigla_id in range(491, 520):
            sünnikoht = 'Rakvere haigla või Tapa haigla'
        elif haigla_id in range(521, 600):
            sünnikoht = 'Valga haigla'
        elif haigla_id in range(601, 650):
            sünnikoht = 'Viljandi haigla'
        elif haigla_id in range(651, 700):
            sünnikoht = 'Lõuna-Eesti haigla või Põlva haigla'
        else:
            sünnikoht = 'Teadmata'

    return f'Lugesin välja järgneva info: \n\tsugu: {sugu}\n\tsünnikuupäev: {päev}.{kuu}.{aasta}\n\tsünnikoht: {sünnikoht}'

isikukoodid = r'C:\Users\37259\Desktop\N.csv'
vastus = []

with open(isikukoodid, 'r', encoding = 'UTF-8-sig') as andmed:
    for rida in andmed:
        sõnad = rida.replace('\n', '').split(',')
        vastus.append(sõnad)

for i in vastus:
    print(f'Eesnimi: {i[0]}\nPerenimi: {i[1]}\nIsikukood: {i[2]}\n{info(i[2])}\n---------------------------')