import random

szam1 = float(input("adjon meg egy számot"))
szam2 = random.randrange(10,50)
SZAM3 = 5
szamok2 = {}
szamok2.add(5)
szamok2.add(6)
szamok2.add(7)

szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)
if szam1 % 2 == 0:
    print("páros")
else:
    print("Páratlan")
print(szam1, szam2)
wr = open("jozsi.txt","w")
wr.write()
wr.write("\n szam4")
wr.close



my_list=[1,2,3,4,5,"abc","def"]
with open('your_file.txt', 'w')as file:
    for item in my_list:
        file.write("%s\n" % item)

f = open("your_file.txt")
tartalom = f.read()
print(tartalom)
f.close()