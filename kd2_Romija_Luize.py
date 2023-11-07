sk1=int(input('Ievadiet pirmo skaitli:')) #Lietotājs ievada pirmo skaitli
sk2=int(input('Ievadiet otro skaitli:'))  #Lietotājs ievada otro skaitli
print('Pirmais skaitlis ir:', sk1) 
print('Otrais skaitlis ir:', sk2) 
if sk1==3: #Pārbauda vai skaitlis ir 3
    print('Pirmais skaitlis ir 3, to skaitļu summa ir:',sk1+sk2) #Ja 3, tad apreiķina summu un tad izvada
else: 
    print('Pirmais skaitlis nav 3, to skaitļu starpība:',sk1-sk2)  #Ja nav 3, tad aprēķina starpību un tad izvada
