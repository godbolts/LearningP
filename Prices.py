def teisendaja(andmed):
    uued_hinnad = {}

    for i in range(0, len(andmed), 2):
        t_nimi = andmed[i].strip()
        try:
            t_hind = float(andmed[i + 1])
        except:
            print(f'Ei saanud teisendada {t_nimi}, hinnaga {andmed[i + 1]} ')
            continue
        uus_hind = round(t_hind - 0.01, 2)
        if uus_hind < 0.01:
            print(f'{t_nimi} hinna teisendamine ei õnnestunud.')
        else:
            uued_hinnad[t_nimi] = uus_hind
            print(f'{t_nimi} hinna teisendamine õnnestus.')

    return uued_hinnad

faili_nimi = r'C:\Users\37259\Desktop\hinnad.txt'
väljastatav = r'C:\Users\37259\Desktop\uued_hinnad.txt'

with open(faili_nimi, 'r') as tekstifail, open(väljastatav, 'w') as uus:
    andmed = tekstifail.read().splitlines()
    uued_hinnad = teisendaja(andmed)
    puhas = ''

    for t_nimi, t_hind in uued_hinnad.items():
        puhas += f'{t_nimi}\n{t_hind:.2f}\n'

    uus.write(puhas)
    print("Uued hinnad on salvestatud faili", väljastatav)