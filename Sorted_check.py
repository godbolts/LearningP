def järgnevus(väärtus):
        return sorted(väärtus) == list(range(min(väärtus), max(väärtus) + 1))

print(järgnevus([1, 2, 3, 3, 5]))