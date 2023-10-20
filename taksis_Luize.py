pasazieri=int(input('Cik pasažierus vēlaties pārvadāt? (ievadi ciparu )')) #1)int funkcija, lietotājs ievada veselu skaitli
if pasazieri > 4 : #Datu pārbaude
    print('Vēlamais pasažieru skaits pārsniedz limitu.')
elif pasazieri<0: #Datu pārbaude
    print('Ievadiet pareizus datus!')
    exit()
laiks= int(input('Ievadiet laiku kādā vēlaties lai taksometrs jūs uzņem?(Laiku rakstīt veselās stundās 0-24)'))
if  laiks>24 or laiks<0: #Datu pārbaude
    print('Ievadiet pareizus datus')
    exit() #1)int
stavvieta= int(input('Vai dzelzceļa stacijā atrodas kāds taksometrs norādītajā stāvvietā? (1=ja, ne=0)')) #lietotājs ievada prasīto atbildi, Jā vai Nē
if stavvieta<0 or stavvieta>1: #Datu pārbaude
    print('Ievadiet pareizus datus!')
    exit()
gaidisana1= int(input('Vai Jums būs nepieciešams gaidīšanas laiks?(Ievadiet veselu skaitli, ja nebūs nepieciešama, ievadiet 0)')) #1)int 
if gaidisana1>100: #Šī ir mana papildus īpašā opcija
    print('Šis taksometrs nav paredzēts gaidīšanai kas pārsniedz 100 minūtes')
    exit()
elif gaidisana1<0: #Datu pārbaude
    print('Ievadiet pareizus datus!')
    exit()
if gaidisana1>0:
    gaidisana=0.15*gaidisana1
elif gaidisana1==0:
    gaidisana='nav'
attalums=int(input('Ievadiet attālumu no dzelzceļa stacijas līdz Jūsu mājām!(Vadiet veselus skaitļus km)')) #1)int
if attalums>100: #Šī ir mana papildus īpašā opcija
    print('Atvainojiet, šis taksometrs nenodas tālāk par 100 kilometriem')
    exit()
if attalums<0 and attalums>100:
    print('Ievadiet pareizus datus')
    exit()
#Pārbaude vai datu ievade bija pareizA

if pasazieri<0 or laiks<0 or stavvieta<0 or stavvieta>1 or laiks>24 or gaidisana1<0 or attalums<0 :
    print('Ievadiet pareizus datus!')
    exit()

#Aprēķini

noligsana= stavvieta
if stavvieta==1:
    noligsana= 1.20 
elif stavvieta==0:
    noligsana= 1.20+2.40 
if laiks>6>0:
    cena= noligsana+attalums*0.87
elif laiks<24>6:
    cena= noligsana+attalums*0.47
if gaidisana1==0:
    kopsumma= cena
elif gaidisana1>0:
      kopsumma= cena+gaidisana1*0.15
else:
    kopsumma= cena

#Datu formatējums

noligsana2=round(noligsana,2)
cena2=round(cena,2)
gaidisana2=round(gaidisana1,2)
kopsumma2=round(kopsumma,2)
import math 

print('\n\t *****Taksometra čeks*****')
print('\t --Kopsumma par nolīgšanu un izsaukumu: ', noligsana2, 'eiro')
print('\t --Nobraukuma maksa: ', cena2, 'eiro')
print('\t --Maksa par gaidīšanu ',gaidisana2, 'eiro')
print('\n\t --- Kopsumma:', kopsumma2, 'eiro' )


