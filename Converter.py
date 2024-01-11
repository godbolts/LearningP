asukoht = r'C:\Users\37259\Desktop\valuutad.txt'
andmed = {}

with open(asukoht, 'r', encoding='UTF-8') as read:
    for rida in read:
        kogum = rida.strip().split('\t')
        lühend = kogum[0]
        kurss = [float(i) if i.replace('.', '', 1).isdigit() else i for i in kogum[2:]]
        andmed[lühend] = kurss[0]

    andmed['EUR'] = 1.0000

def konverter(lähte, siht, kogus, valuutad):

    if lähte in valuutad and siht in valuutad:
        val_lähte = valuutad[lähte]
        val_siht = valuutad[siht]
        muudetud = kogus * (val_siht / val_lähte)

    return  muudetud

print(konverter('PLN', 'USD', 100, andmed))