import random as r

first = r.randint(0, 100)

while True:
    print(first)
    awn = input('Kas see on arv mis te mõtlesite? (jah/ei): ')

    if awn == 'jah':
        print('Palun.')
        break
    div = input('Kas teie arv oli väiksem või suurem kui pakutud? (kirjutage palun väiksem/suurem): ')

    if div == 'väiksem':
        first = r.randint(0, first)
    elif div == 'suurem':
        first = r.randint(first, 100)