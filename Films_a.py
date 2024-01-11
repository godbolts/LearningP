import films_b as f

def töötleKäsk(tähis, järjend = None):
    if tähis == 'K':
        vastus = f.loetleFilmid(järjend)
        return True, vastus
    elif tähis == 'L':
        nimi = järjend[1]
        tüüp = järjend[0]
        f.lisaFilm(nimi, tüüp)
        return True
    elif tähis == 'V':
        f.kustutaFilm(järjend)
        return True
    elif tähis == 'E':
        return False
    else:
        return False

sisestus = input()
tähis = sisestus[0].upper()

if len(sisestus) > 1:
    järjend_1 = sisestus[2:].split()
    esimene_osa = järjend_1[0]
    teine_osa = ' '.join(järjend_1[1:])
    järjend = [teine_osa] if esimene_osa == 'L' else [esimene_osa, teine_osa]
else:
    järjend = []

while True:
    vastus = töötleKäsk(tähis, järjend)
    if not vastus:
        break