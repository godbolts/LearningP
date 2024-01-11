import math as ma

al = float(input('Palun sisestage kolnurga külg a: '))
bd = float(input('Palun sisestage kolnurga külg b: '))
ce = float(input('Palun sisestage kolnurga külg c: '))
uhik = str(input('Palun lisage siia mõõtühik: ')) + '²'

def kolmnurga_pindala_külgede_järgi(a, b, c):
    p = (a + b + c)/2
    pindala = ma.sqrt(p*(p-a)*(p-b)*(p-c))
    return pindala

vastus = kolmnurga_pindala_külgede_järgi(al, bd, ce)

print(vastus, uhik)