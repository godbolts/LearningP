punktid = int(input('Palun sisestage punktisumma, vahemikus 0-100: '))
hindamisviis = input('Palun sisestage hindamisviis(e/m): ')

if punktid < 0:
       print('Punktisumma peab jääma vahemikku 0–100')

elif hindamisviis == 'e':
   if punktid >= 90:
       print('A')
   elif punktid >= 80:
       print('B')
   elif punktid >= 70:
       print('C')
   elif punktid >= 60:
       print('D')
   elif punktid >= 50:
       print('E')
   else:
       print('F')

elif hindamisviis == 'm':
   if punktid >= 50:
       print('Arvestatud')
   elif punktid == 0:
       print('Ei käinud kohal.')
   else:
       print('Mitte arvestatud')

else:
   print('Vale hindamisviis, Sisestage kas e või m: ')