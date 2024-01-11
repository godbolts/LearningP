fail = open(r'C:\Users\37259\Desktop\Kup.txt', encoding = "UTF-8")

with fail:
   eesnimi = fail.readline().strip()
   perenimi = fail.readline().strip()
   sund = fail.readline().strip()
   surm = fail.readline().strip()

min = 31*'-'
tuhi = ' '
elem = int((30 - len(eesnimi + perenimi))/2)*' '

print(f'+{min}+')
print(f'|{elem}{eesnimi} {perenimi}{elem}|')
print(f'|{31*tuhi}|')
print(f'|    {sund} - {surm}    |')
print(f'|{31*tuhi}|')
print(f'+{min}+')

fail.close()