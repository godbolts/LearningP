def muutja(a):

    if not a:
        raise ValueError('Tühi sõne ei saa olla täisarv')

    täisarv = 0
    negatiivne = False

    if a[0] == '-':
        negatiivne = True
        a = a[1:]

    for sümbol in a:
        if '0' <= sümbol <= '9':
            numbriline_väärtus = ord(sümbol) - ord('0')
            täisarv = täisarv * 10 + numbriline_väärtus
        else:
            raise ValueError(f'Vigane sõne: {a} sisaldab mittenumbrit')

    if negatiivne:
        täisarv = -täisarv

    return täisarv

a = muutja('22')
print(a)