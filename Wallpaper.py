import math as ma

pikkus = float(input('Palun sisesta oma ruumi pikkus: '))
laius = float(input('Palun sisesta oma ruumi laius: '))
korgus = float(input('Palun sisesta oma ruumi kõrgus: '))
tap_korgus =float(input('Palun sisesta kui kõrged on tapeedi paanid: '))
tap_laius =float(input('Palun sisesta kui laiad on tapeedi paanid: '))

u_moot = pikkus*2 +laius*2
seina_laius = u_moot/tap_laius
seina_pikkus = tap_korgus/korgus
arv = ma.ceil(round(seina_laius/seina_pikkus, 2))

print(f'On vaja osta {arv} rulli tapeeti.')
