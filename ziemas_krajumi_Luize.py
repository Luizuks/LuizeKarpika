aboli=float(input('Kāds ir šī gada ābolu ražas daudzums (Ievadīt tikai skaitļus kg)?'))
if aboli<0:
    print('Ievadiet pareizus datus.')
cukurs= int(input('Kādu cukuru izmantosiet? (parasto=0, ievarijuma=1)'))
mcukurs= input('Vai mājās ir cukurs? (j/n)')
mudens= input('Vai mājās ir udens? (j/n)')
mcitrons= input('Vai mājās ir citrons? (j/n)')
mmandeluek= input('Vai mājās ir mandeļu ekstrakts? (j/n)')
mkanelis= input('Vai mājās ir kanēlis? (j/n)')

#izmaksas
cukurs1=1.20#
cukurs_iev=1.50#
udens=1
citrons=0.5
man_ek= 1
kanelis=0.62

#aprēķini 
import math 
if mcukurs=='j' and cukurs==0 or cukurs==1:
   izmaksas=(udens+citrons+man_ek+kanelis)*aboli
   print(izmaksas)
elif mudens=='j' and cukurs==0:
   izmaksas=(citrons+man_ek+kanelis+cukurs1)*aboli
   print(izmaksas)
elif mcitrons=='j' and cukurs==0:
   izmaksas=(udens+cukurs1+man_ek+kanelis)*aboli
   print(izmaksas)
elif mudens=='j' and cukurs==1:
   izmaksas=(citrons+man_ek+kanelis+cukurs_iev)*aboli
   print(izmaksas)
elif mcitrons=='j' and cukurs==1:
   izmaksas=(udens+man_ek+kanelis+cukurs_iev)*aboli
   print(izmaksas)
elif mmandeluek=='j' and cukurs==0:
   izmaksas=(citrons+udens+kanelis+cukurs1)*aboli
   print(izmaksas)
elif mmandeluek=='j' and cukurs==1:
   izmaksas=(citrons+udens+kanelis+cukurs_iev)*aboli
   print(izmaksas)
elif mkanelis=='j' and cukurs==0:
   izmaksas=(citrons+udens+man_ek+cukurs1)*aboli
   print(izmaksas)
elif mkanelis=='j' and cukurs==1:
   izmaksas=(citrons+udens+man_ek+cukurs_iev)*aboli
   print(izmaksas)
elif mcukurs=='j' and cukurs==0 and mudens=='j':
   izmaksas=(citrons+man_ek+kanelis)*aboli
   print(izmaksas)
elif mcukurs=='j' and cukurs==1 and mudens=='j':
   izmaksas=(citrons+man_ek+kanelis)*aboli
   print(izmaksas)
elif mcukurs=='j' and cukurs==0 and mcitrons=='j':
   izmaksas=(udens+man_ek)+kanelis*aboli
   print(izmaksas)
elif cukurs=='j' and cukurs==1 and mcitrons=='j':
   izmaksas=(udens+man_ek+kanelis)*aboli
   print(izmaksas)
elif mcukurs=='j' and cukurs==0 or cukurs==1 and man_ek=='j':
    izmaksas=(udens+citrons+kanelis)*aboli
    print(izmaksas)
elif mcukurs=='j' and mkanelis=='j' and cukurs==0 or cukurs==1:
   izmaksas=(udens+citrons+man_ek)*aboli
   print(izmaksas)
elif mudens=='j' and mkanelis=='j' and cukurs==0:
   izmaksas=(citrons+man_ek+cukurs1)*aboli
   print(izmaksas)
elif mudens=='j' and mkanelis=='j' and cukurs==1:
   izmaksas=(citrons+man_ek+cukurs_iev)*aboli
   print(izmaksas)
elif mudens=='j' and mmandeluek=='j' and cukurs==0:
   izmaksas=(citrons+kanelis+cukurs1)*aboli
   print(izmaksas)
elif mudens=='j' and mmandeluek=='j' and cukurs==1:
   izmaksas=(citrons+kanelis+cukurs_iev)*aboli
   print(izmaksas)
elif mudens=='j' and mcitrons=='j' and cukurs==0:
    izmaksas = (kanelis+cukurs1+man_ek)*aboli
    print(izmaksas)
elif mudens=='j' and mcitrons=='j' and cukurs==1:
    izmaksas = (kanelis+cukurs_iev+man_ek)*aboli
    print(izmaksas)
elif mcitrons=='j' and mkanelis=='j' and cukurs==0:
   izmaksas=(man_ek+cukurs1+udens)*aboli
   print(izmaksas)
elif mcitrons=='j' and mkanelis=='j' and cukurs==1:
   izmaksas=(man_ek+cukurs_iev+udens)*aboli
   print(izmaksas)
elif mmandeluek=='j' and mkanelis=='j' and cukurs==0:
   izmaksas=(udens+cukurs1+citrons)*aboli
   print(izmaksas)
elif mmandeluek=='j' and mkanelis=='j' and cukurs==1:
   izmaksas=(udens+cukurs_iev+citrons)*aboli
   print(izmaksas)
