def loe_failist(failinimi):
    järjend = []
    asukoht = r'C:\Users\37259\Desktop\\' + failinimi + '.txt'

    with open(asukoht, 'r', encoding='UTF-8') as toores:
        for rida in toores:
            tükeldatud = rida.strip().split(';')
            järjend.append(tükeldatud)

    return järjend

def kes_võitis(järjend):
    järjekord = []

    for i in järjend:
        number = i.count('V')
        järjekord.append(number)
    suurim = max(järjekord)
    suurim_index = (järjekord.index(suurim)) + 1

    return suurim_index

järjend = loe_failist('hokiturniir')
vastus = kes_võitis(järjend)

print(f'Turniiri võitis {vastus}. võistkond.')