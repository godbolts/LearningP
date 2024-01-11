def saab_lennata(l_nimi, s_nimi, sõnastik):
    visited = set()
    stack = [l_nimi]

    while stack:
        current_location = stack.pop()
        if current_location == s_nimi:
            return True
        if current_location in sõnastik and current_location not in visited:
            visited.add(current_location)
            stack.extend(sõnastik[current_location])

    return False

lennud = {
    'Pariis' : {'London', 'Berliin', 'Nice'},
    'London' : {'Berliin', 'Pariis'},
    'Berliin' : {'London', 'Pariis', 'Tallinn'},
    'Viin' : {'Madrid', 'Barcelona', 'Dublin'},
    'Tallinn' : {'Berliin'}
}

print(saab_lennata('Tallinn', 'Nice', lennud))