nev = input('Mi a neve')
nev = int(input('Hány éves vagy'))

if nev < 3:
    minősítés ='Tyogyogó'
elif nev < 6:
    minősítés = 'Fiatalkorú'
elif nev < 14:
    minősítés = 'Felhőtechnológia a menzán'
elif nev < 18:
    minősítés = 'Big data a középiskolában'
else:
    print: 'nev'
print(f'{név} maga {minősítés}')