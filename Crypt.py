def krüpti_sõne(tekst):
    vastus = ''
    for täht in tekst:
        if täht in ascii_lowercase:
            indeks = (ascii_lowercase.index(täht) + 3) % 26
            vastus += ascii_lowercase[indeks]
        elif täht in ascii_uppercase:
            indeks = (ascii_uppercase.index(täht) + 3) % 26
            vastus += ascii_uppercase[indeks]
        else:
            vastus += täht
    return vastus

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

tekstid = []
esimene_fail = r'C:\Users\37259\Desktop\s.txt'

with open(esimene_fail, 'r', encoding = 'UTF-8') as asi:
    for r in asi:
        a = r.replace('\n', '')
        tekstid.append(a)
krüptitud_tekstid = [krüpti_sõne(tekst) for tekst in tekstid]

with open(esimene_fail, 'w', encoding = 'UTF-8') as asi:
    for krüptitud_tekst in krüptitud_tekstid:
        asi.writelines(krüptitud_tekst + '\n')