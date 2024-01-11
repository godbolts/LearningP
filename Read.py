def poisse_ja_tüdrukuid(järjend: list) -> tuple:
    poisse = 0
    tüdrukuid = 0

    for nimi in järjend:
        if nimi[-1] == 'P':
            poisse += 1
        elif nimi[-1] == 'T':
            tüdrukuid += 1
        else:
            continue
    vastus = (poisse, tüdrukuid)
    return vastus

print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))