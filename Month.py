kuu = int(input("Sisesta kuu number: "))
if kuu == 12:
    print("talv")
else:
    if kuu == 1 or kuu == 2:
        print('talv')
    else:
        if kuu > 2 and kuu < 6:
            print("kevad")
        elif kuu < 9 and kuu > 5:
            print('suvi')
        else:
            print("sügis")





