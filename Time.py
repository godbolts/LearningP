import datetime

def päevade_arv(inter):
    kolm_üks = [1, 3, 5, 7, 8, 10, 12]
    kolm_kümme = [4, 6, 9, 11]
    today = datetime.date.today()
    year = today.year

    if inter in kolm_üks:
        print('Selles kuus on 31 päeva.')
    elif inter in kolm_kümme:
        print('Selles kuus on 30 päeva.')
    elif inter == 2:
        if year % 4 == and (year % 100 != 0 or year % 400 == 0):
            print('Selles kuus on 29 päeva.')
        else:
            print('Selles kuus on 28 päeva.')
    else:
        print('-1')

while True:
    nimekiri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    e = input('Sisesta kuu arv: ')
    if e == '':
        break
    try:
        a = int(e)
    except ValueError:
        print('Palun sisestage täisarv.')
        continue
    if a in nimekiri:
        päevade_arv(a)
    else:
        print('Kuu number peab jääma lõiku 1-12.')

print('Programm lõpetas töö.')