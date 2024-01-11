from time import sleep
import random as r

print('Kangelane soovib ületada silda, Troll on ees ja küsib tolli. Kangelane keeldub ning mõõk tuleb tupest välja.')

t_elu = 100
k_elu = 100

while t_elu > 0 and k_elu > 0:
    t_elu -= r.randint(0, 5)
    k_elu += r.randint(0, 2)
    k_elu -= r.randint(0, 7)

    print(f'Trollil on alles {t_elu} elupunkti.')
    print(f'Kangelasel on alles {k_elu} elupunkti.')

    sleep(0)

if t_elu > k_elu:
    print('Troll kaitses oma silda.')

else:
    print('Kangelane sai trollist jagu ja ületas silla.')