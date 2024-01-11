from random import sample

def bingo():
    while True:

        järjend = sample(range(1, 11), 3)

        if not (1 in järjend and 2 in järjend and 3 in järjend):
            break

    lisand = sample(range(11, 21), 2)
    järjend.extend(lisand)

    return järjend

print(bingo())