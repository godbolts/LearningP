from time import time
import random

t_suurtäht = ['A',  'E',  'I',  'O', 'U',  'Õ', 'Ä', 'Ö', 'Ü']
k_suurtäht = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'Š', 'Z', 'Ž', 'T', 'V', 'W', 'X', 'Y']
t_väiketäht = [letter.lower() for letter in t_suurtäht]
k_väiketäht = [letter.lower() for letter in k_suurtäht]
numbrid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
n = 0
algus = time()

while n < 3:
    valik = random.choice(['suur täishäälik', 'suur kaashäälik', 'väike täishäälik', 'väike kaashäälik', 'number'])

    if valik == 'suur täishäälik':
        vastus = input(f'Palun sisesta {valik}: ')
        if vastus in t_suurtäht:
            n += 1
        else:
            n -= 1

    elif valik == 'suur kaashäälik':
        vastus = input(f'Palun sisesta {valik}: ')
        if vastus in k_suurtäht:
            n += 1
        else:
            n -= 1

    elif valik == 'väike täishäälik':
        vastus = input(f'Palun sisesta {valik}: ')
        if vastus in t_väiketäht:
            n += 1
        else:
            n -= 1

    elif valik == 'väike kaashäälik':
        vastus = input(f'Palun sisesta {valik}: ')
        if vastus in k_väiketäht:
            n += 1
        else:
            n -= 1

    elif valik == 'number':
        vastus = input(f'Palun sisesta {valik}: ')
        if vastus in numbrid:
            n += 1
        else:
            n -= 1

lõpp = time()
aeg_toor = lõpp - algus
aeg = round(aeg_toor, 1)

print(f'Harjutus võttis {aeg} sekundit aega.')