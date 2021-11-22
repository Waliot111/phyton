import math

a = int(input('Kérem a másodfokú egyenlet főegyütthatóját:'))
a = float(a)
while a== 0:
    print('Ez nem lesz másodfokú egyenlet')
    a= input('Kérem a konsans tagot')
    a= float(a)
b= int(input('Kérem a másodfokú:'))
c= int(input('Kérem a konstans tagot')
d= b*b-4*a*c
print(d)
if d >= 0:
    x1 = (-b+math.sqrt(d)/2*a)
    x2 = (-b-math.sqrt(d)/2*a)
    print(x1)
    print(x2)
    print('Nnics valós megoldás.')

else: 
    x1 = (-b+math.sqrt(d)/2*a)
    x2 = (-b-math.sqrt(d)/2*a)
    print(x1)
    print(x2)
    print('Van valós megoldás.')

        