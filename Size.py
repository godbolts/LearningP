import os.path as os

def faili_suurus(failinimi):
    tais = os.join(r"C:\Users\37259\Desktop", failinimi)
    suurus = os.getsize(tais)
    return suurus
def teisenda(baidid):
    if baidid < 1024:
        sone = str(baidid) + ' B'
        print(sone)
    elif baidid == 1024:
        print('1 KB')
    elif baidid < 1024*1024:
        k_baidid = round(baidid/(1024), 1)
        sone = str(k_baidid) + ' KB'
        print(sone)
    elif baidid == 1024*1024:
        print('1 MB')
    elif baidid < 1024*1024*1024:
        k_baidid = round(baidid/(1024*1024), 1)
        sone = str(k_baidid) + ' MB'
        print(sone)
    elif baidid == 1024*1024*1024:
        print('1 GB')
    elif baidid < 1024*1024*1024*1024:
        k_baidid = round(baidid/(1024*1024*1024), 1)
        sone = str(k_baidid) + ' GB'
        print(sone)
    elif baidid == 1024*1024*1024*1024:
        print('1 TB')
    elif baidid > 1024*1024*1024*1024:
        k_baidid = round(baidid/(1024*1024*1024*1024), 1)
        sone = str(k_baidid) + ' TB'
        print(sone)
    else:
        print('Midagi läks valesti, hea küsimus mis...')

nimi = str(input('Palun kirjutage siia failinimi: '))
suurus = faili_suurus(nimi)
teisenda(suurus)
i = 1

while i == 1:
    nimi = str(input('Palun kirjutage siia failinimi: '))
    if nimi == '':
        break
    suurus = faili_suurus(nimi)
    teisenda(suurus)