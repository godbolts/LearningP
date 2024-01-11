temp = 90
toa_temp = 20
min = 0

while temp > toa_temp:
    vahe = temp - toa_temp
    alla = vahe * 0.19
    temp = temp - alla
    kraad = round(temp, 1)
    print(f'{kraad}° C')
    temp -= 0.19
    min += 1

print(f'Supi jahtumine võttis aega {min} minutit.')