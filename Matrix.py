def võitja(maatriks):
    tulemus = {'O': 0, 'X': 0}

    for i in range(4):
        for j in range(4):
            if i + 2 < 4:
                if (maatriks[i][j] == maatriks[i + 1][j] == maatriks[i + 2][j] == 'X') or (maatriks[i][j] == maatriks[i + 1][j] == maatriks[i + 2][j] == 'O'):
                    tulemus[maatriks[i][j]] += 1
            if j + 2 < 4:
                if (maatriks[i][j] == maatriks[i][j + 1] == maatriks[i][j + 2] == 'X') or (maatriks[i][j] == maatriks[i][j + 1] == maatriks[i][j + 2] == 'O'):
                    tulemus[maatriks[i][j]] += 1
            if i + 2 < 4 and j + 2 < 4:
                if (maatriks[i][j] == maatriks[i + 1][j + 1] == maatriks[i + 2][j + 2] == 'X') or (
                        maatriks[i][j] == maatriks[i + 1][j + 1] == maatriks[i + 2][j + 2] == 'O'):
                    tulemus[maatriks[i][j]] += 1
            if i - 2 >= 0 and j + 2 < 4:
                if (maatriks[i][j] == maatriks[i - 1][j + 1] == maatriks[i - 2][j + 2] == 'X') or (
                        maatriks[i][j] == maatriks[i - 1][j + 1] == maatriks[i - 2][j + 2] == 'O'):
                    tulemus[maatriks[i][j]] += 1

    return tulemus

seis = [[' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ']]

seis_1 = [['X', 'X', 'X', ' '],
          [' ', 'O', ' ', ' '],
          [' ', ' ', 'O', ' '],
          [' ', ' ', ' ', 'O']]

seis_2 = [['O', ' ', ' ', 'X'],
          [' ', 'O', 'X', ' '],
          [' ', 'X', 'O', ' '],
          ['X', ' ', ' ', 'O']]

seis_3 = [['O', ' ', 'O', 'X'],
          ['O', 'O', 'X', 'X'],
          ['O', 'X', 'O', ' '],
          ['X', 'X', 'X', 'O']]

vastus = võitja(seis)
vastus_1 = võitja(seis_1)
vastus_2 = võitja(seis_2)
vastus_3 = võitja(seis_3)

print(vastus)
print(vastus_1)
print(vastus_2)
print(vastus_3)