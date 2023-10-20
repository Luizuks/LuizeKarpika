veikals=int(input('Kādā veikalā jūs iepērkaties? (rimi=1, top=2, maxima=3, vesko=4 un bazars=5): '))
if veikals==2 or veikals==3:
    karte=input('Vai jums ir klienta karte? (jā=j, nē=n): ')
elif veikals==4:
    daudzums_viss=int(input('Cik preces vēlaties pirkt:'))
while True:
    produkti=input('Ievadiet produktu nosaukumu kādu vēlaties iegādāties: ')
    cena=int(input('Ievadiet produkta cenu: '))
    daudzums=int(input('Ievadiet produkta daudzumu: '))
    stop=input('Vai ir nopirkts viss kas ir sarakstā:(jā=j, nē=n): ')
    if stop=='j':
        break
        
    if veikals==1:
        produkti= cena*daudzums
        kopsumma1=produkti-0.3
        kopsumma=kopsumma1
    elif veikals==2 and karte=='j':
        produkti=cena*daudzums
        kopsumma1=produkti-0.4
        kopsumma=kopsumma1
    elif veikals==2 and karte=='n':
        produkti=cena*daudzums
        kopsumma1=produkti
        kopsumma=kopsumma1
    elif veikals==3 and karte=='j':
        produkti=cena*daudzums
        kopsumma1=produkti-0.5
        kopsumma=kopsumma1
    elif veikals==3 and karte=='n':
        produkti=cena*daudzums
        kopsumma1=produkti-0.2
        kopsumma=kopsumma1
    elif veikals==4 and daudzums_viss>= 3:
        produkti=cena*daudzums
        kopsumma1=produkti-0.3
        kopsumma=kopsumma1
    elif veikals==4 and daudzums_viss<3 and daudzums_viss>0:
        produkti=cena*daudzums
        kopsumma1=produkti
        kopsumma=kopsumma1
    elif veikals==5:
        produkti=cena*daudzums
        kopsumma1=produkti-0.5
        kopsumma=kopsumma1


print('\n\t *******Čeks*******')
print('\n\t Cenas par produktiem:')
if daudzums>1:
    print('\n\t ', produkti, cena,'eiro', '\n\tDaudzums ir', daudzums, '\n\tKopsumma ir',produkti*cena*daudzums, 'eiro')
elif daudzums==1:
    print('\n\t ', produkti, cena,'eiro', '\n\tKopsumma ir',produkti*cena,'eiro')
print('\n\tKopsumma apmaksai:', kopsumma, 'eiro')

