def transponeeriK(maatriks):
    read = len(maatriks)
    col = len(maatriks[0])
    trans = [[0] * read for _ in range(col)]

    for i in range(read):
        for j in range(col):
            trans[col - j - 1][read - i - 1] = maatriks[i][j]

    return trans

maatriks_i = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
maatriks_ii = [[1, 2], [3, 4], [5, 6], [7, 8]]
maatriks_iii = [[4, 31, 67, 99]]

print(transponeeriK(maatriks_i))
print(transponeeriK(maatriks_ii))
print(transponeeriK(maatriks_iii))