import random

tömegek = []
for _ in range (20):
    tömegek.append(random.randint(1000,10000))
# kész a listánk
print(tömegek) #csak hogy könnyű legyen ellenőrizni

volt_nehez = False
nehez_szama=0
ossztomeg =0
nehezek_ossztomege = 0
for tömeg in tömegek:
    ossztomeg = ossztomeg + tömeg
    if tömeg > 9300:
        volt_nehez = True
        nehez_szama += 1 # nehe_szama= nehez_szama+1
        nehezek_ossztomege += tömeg
if volt_nehez:
    print('volt 9300 kilonál nehezebb jármű')

print(nehezek_ossztomege)
print(nehez_szama)