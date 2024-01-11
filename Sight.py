pikkused = [195, 167, 165, 190, 172, 182, 187, 189, 168, 174]
kaugeim_index = -1

for i in range(len(pikkused)):
    nahtud = False

    for j in range(i + 1, len(pikkused)):
        if pikkused[i] > pikkused[j]:
            nahtud = True
            break

    if nahtud:
        kaugeim_index = i

if kaugeim_index != -1:
    inimene_nr = kaugeim_index + 1
    kaugeim_pikkus = pikkused[kaugeim_index]
    print(f"Inimene nr {inimene_nr} pikkusega {kaugeim_pikkus} näeb kõige kaugemale.")
else:
    print("Ükski inimene ei näe kõige kaugemale.")