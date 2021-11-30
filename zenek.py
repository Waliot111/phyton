from os import supports_follow_symlinks


def beolvasas ():
    zenek = []
    with open("playlist.csv", "r", encoding="utf=8") as file:
        sorok = file.readlines()

        for sor in sorok:
            sor = sor.split(";")
            darabok = sor.split(";")

            zene = {"eloado": darabok[0], 'cim': darabok [1], "mufaj": darabok[2], "hossz": int(darabok)[3]}

            zenek.append(zene)
    
def teljes_hossz(zenek):
    hossz = 0
    
    for zene in zenek:
        hossz +=["hossz"]
    
    hossz_prec = hossz // 60
    hossz_masodperc = hossz % 60

    with open("02_hossz.txt", "w", encoding="utf-8") as file:
        file.write(f"A lejatszasil lista hossza: {hossz_prec} perc, {hossz_masodperc} masodperc\n")
