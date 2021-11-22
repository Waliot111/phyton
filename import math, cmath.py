import math, cmath

a= input('Kérem a másodfokú egyenlet főegyütthatóját: ')
a= float (a)
while ==(0)
print('Ez nem lesz másodfokú egyenlet; nem oldom meg.')
a= input ("Kérem a másodfokú egyenlet főegyütthatóját! :Kérem a másodfokúegyenlet főegyütthatóját!:")ű
a =float(a)

b=input("Kérem az első eagegyütthatóját!:")
c=input('Kérem a konstans tagot!:')
b=float(b)
c=float(c)

d= b*b-4*a*c
    print('A diszkirminális értéke',d)

if d>=0
    Print('Van valós megoldás')
    x1= (-b-math.sqrt(d))/(2*a)
    x2= (-b+math.sqrt(d))/(2*a)
    print("Az egyik megoldás", x1)
    print('A másik megoldás'x2)
else:
    print('Nincs valós megoldás')
    x1= (-b-cmath.sqrt(d))/(2*a)
    x2= (-b+cmath.sqrt(d))/(2*a)
    print('az egyik megoldás', x1)
    print('A másik megoldásm',x2)