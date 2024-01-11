def euro(arv):
    if arv > 100:
        sõne = str(arv)

        if len(sõne) == 3:
            if sõne[0] == '1' and sõne[1] == '0':
                print(f'{sõne[0]} euro ja {sõne[2]} sent')
            elif sõne[0] == '1':
                print(f'{sõne[0]} euro ja {sõne[1:]} senti')
            elif sõne[1] == '0' and sõne[2] == '1':
                print(f'{sõne[0]} eurot ja {sõne[2]} sent')
            else:
                print(f'{sõne[0]} eurot ja {sõne[1:]} senti')

        else:
            if sõne[2] == '1' and sõne[1] == '0':
                print(f'{sõne[-1]} eurot ja {sõne[2]} sent')
            else:
                print(f'{sõne[-1]} eurot ja {sõne[1:]} senti')

    elif arv == 100:
        print('1 euro')
    elif arv > 1:
        print(f'{arv} senti')
    elif arv == 1:
        print('1 sent')
    elif arv == 0:
        print('Tühi')
    else:
        print('Sellest ei tule isegi senti')

print(euro(99))