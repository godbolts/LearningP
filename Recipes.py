def failist_järjendisse(sõne):
    asukoht = r'C:\Users\37259\Desktop\\' + sõne + '.txt'
    retseptid = []
    with open(asukoht, 'r', encoding = 'UTF-8') as tekst:
        for rida in tekst:
            retsept = rida.strip().split('\n')
            retseptid.append(retsept)
    return retseptid

leitud = 0

print(f'Retseptid, milles on vaja maasikaid ja suhkrut:')

retseptid = failist_järjendisse('s')

for i in retseptid:
    if 'maasikad' in i[0] and 'suhkur' in i[0]:
        leitud += 1
        print(i[0])

if leitud == 0:
    print('Ei ole ühtegi sellist retsepti.')