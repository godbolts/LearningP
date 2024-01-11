def esineb(väärtus, järjend, korda):
    esineb = False
    arv = 0

    for i in järjend:
        if väärtus == i:
            arv += 1
        if arv >= korda:
            esineb = True

    return esineb

print(esineb('a', ['a', 'b', 'a'], 3))