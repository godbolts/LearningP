aastatulu = float(input('Palun sisestage sisestage siia oma aastatulu, lubame, et me ei saada edasi Maksu- ja Tolliametile: '))

if aastatulu <= 6000:
   print('Teie maksuvaba tulu on sellel aastal: ', aastatulu)

elif 6000 < aastatulu <= 14400:
   print('Teie maksuvaba tulu on sellel aastal: 6000')

elif 14400 < aastatulu <= 25200:
   arv = 6000 - 6000/10800*(aastatulu - 14400)
   umar = round(arv, 2)
   print(umar)

elif aastatulu > 25200:
   print(float(0))