def erinevad(sõne):
    esimene = sõne.strip('.!?,').lower()
    nimekiri = esimene.split(' ')
    vastus = list(set(nimekiri))
    return vastus

nimi = input('Palun sisestage siia esimese faili nimi: ')
fail = r'C:\Users\37259\Desktop\\' + nimi + '.txt'
andmed = []

with open(fail, 'r') as nimed:
    for r in nimed:
        a = r.replace('\n', '')
        andmed.append(a)

unique_words_per_line = [erinevad(tekst) for tekst in andmed]

with open(fail, 'w', encoding = 'UTF-8') as asi:
    for unique_words in unique_words_per_line:
        asi.write(' '.join(unique_words) + '\n')