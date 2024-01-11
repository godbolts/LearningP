import datetime

def vahe(e_aaaa, e_kk, e_pp, t_aaaa, t_kk, t_pp):
    e_aeg = datetime.date(e_aaaa, e_kk, e_pp)
    t_aeg = datetime.date(t_aaaa, t_kk, t_pp)
    arv = e_aeg - t_aeg
    return arv

print(vahe(2018, 10, 25, 2018, 9, 1))