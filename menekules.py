bulizok_szama = int(input("A hazibuliban resztvevok szama: "))
rendorok_szama = int (input("A remdorok szama: "))
print()

if rendorok_szama == 0: 
    print("Minden bulizo megmenekult!")
else:
    elkapottak_szama = 0
    
    for i in range (1, rendorok_szama + 1):
        elkapottak_szama += i

    if elkapottak_szama < bulizok_szama:
        elmenekultek_szama = bulizok_szama - elkapottak_szama
        print(elkapottak_szama, "bulizot elkaptak,", elmenekultek_szama, "pedig elmmenekult.")
    else:
        print("Ajaj, mindenkit elkaptak")