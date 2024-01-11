def erinevad_sümbolid(sõne):
    vastus = [i for i in sõne]
    hulk = set(vastus)

    return hulk

def sümbolite_sagedus(sõne):
    sõnaraamat = {}

    for sümbol in sõne:
        if sümbol in sõnaraamat:
            sõnaraamat[sümbol] += 1
        else:
            sõnaraamat[sümbol] = 1

    return sõnaraamat

def grupeeri(sõne):
    täishäälikud = 'aeiouAEIOU'
    kaashäälikud = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    sõnaraamat = {'täishäälikud': {}, 'kaashäälikud': {}, 'muud': {}}

    for sümbol in sõne:
        if sümbol in täishäälikud:
            if sümbol in sõnaraamat['täishäälikud']:
                sõnaraamat['täishäälikud'][sümbol] += 1
            else:
                sõnaraamat['täishäälikud'][sümbol] = 1
        elif sümbol in kaashäälikud:
            if sümbol in sõnaraamat['kaashäälikud']:
                sõnaraamat['kaashäälikud'][sümbol] += 1
            else:
                sõnaraamat['kaashäälikud'][sümbol] = 1
        else:
            if sümbol in sõnaraamat['muud']:
                sõnaraamat['muud'][sümbol] += 1
            else:
                sõnaraamat['muud'][sümbol] = 1

    sõnaraamat['täishäälikud'] = sorted(sõnaraamat['täishäälikud'].items())
    sõnaraamat['kaashäälikud'] = sorted(sõnaraamat['kaashäälikud'].items())
    sõnaraamat['muud'] = sorted(sõnaraamat['muud'].items())

    return sõnaraamat

vastus_1 = erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente")
vastus_2 = sümbolite_sagedus("Hei hopsti, väikevend!")
vastus_3 = grupeeri("sõida tasa üle silla")

print(vastus_1)
print(vastus_2)
print(vastus_3)