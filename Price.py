def auto_hind(hind, aastad):
    if aastad == 0:

        return round(hind, 2)

    else:
        aastad -= 1

        return auto_hind((hind * 0.8), aastad)

print(auto_hind(10000.0, 6))