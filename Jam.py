def moos(suur, vaike, kogus):
    abs_suurte_arv = kogus // 5
    if suur <= abs_suurte_arv:
        suurte_arv = suur
    else:
        suurte_arv = abs_suurte_arv
    abs_vaikeste_arv = kogus - suurte_arv*5
    if vaike >= abs_vaikeste_arv:
        vaikeste_arv = abs_vaikeste_arv
    else:
        return -1
    return suurte_arv + vaikeste_arv

a = moos(5, 1, 9)

print(a)