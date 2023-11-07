sk1=int(input('Ievadiet pirmo skaitli:')) #Lietotājs ievada pirmo skaitli
sk2=int(input('Ievadiet otro skaitli:'))  #Lietotājs ievada otro skaitli
if 5<sk1<15 and 5<sk2<15: #izvērtē skaitļu robežas 
    print('Tu esi izpildījis uzdevumu!')
elif 5<sk1<15 or 5<sk2<15:  #izvērtē skaitļu robežas 
    print('viens skaitlis neatbilst nosacījumiem!')
else:
    print('Nav izpildīts!')
 