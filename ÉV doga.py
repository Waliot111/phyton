nev = input('Mi a neve')
gyerek = int(input('Hány éves maga'))

if gyerek < 13:
    minősítés ='Gyermek'
elif gyerek < 17:
    minősítés = 'Fiatalkorú'
elif gyerek < 23:
    minősítés = 'Ifjú'
elif gyerek < 69:
    minősítés = 'Felnőtt'
else:
    print: 'idős'
print(f'{név} maga {minősítés}')