arv = int(input('Palun sisestage siia üks täisarv: '))

if arv % 3 == 0 and arv % 5 == 0:
   print('FizzBuzz')
elif arv % 5 == 0:
   print('Buzz')
elif arv % 3 == 0:
   print('Fizz')
else:
   print(arv)