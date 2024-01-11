def kombinatsioon(e_mass, t_mass):
    tühi = set()
    for i in e_mass:
        for j in t_mass:
            tühi.add((i, j))

    return tühi

print(kombinatsioon({'♥','♦','♠','♣'}, {'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'}))