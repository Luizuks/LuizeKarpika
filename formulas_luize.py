import math

rlr=float(input("Ievadiet rinķa līnijas rādiusu:")) #lietotājs ievada rādiusa garumu
print(rlr) #rādiusa izvade
rlg= 2*math.pi*rlr #programma aprēķina rinķa līnijas garumu
print('Rinķa līnijas garums:' "{:.2f}".format(rlg)) #rinķa līnijas garuma izvade
rll=math.pi*math.pow(rlr,2) #programma aprēķina rinķa līnijas laukumu
print('Rinķa līnijas laukums:'"{:.2f}".format(rll)) #rinķa līnijas garuma izvade
k1=float(input('Ievadiet taisnlenķa trijstūra pirmās katetes garumu:')) #lietotājs ievada pirmās katetes garumu
k2=float(input('Ievadiet taisnlenķa trijstūra otrās katetes garumu:')) #lietotājs ievada otrās katetes garumu
h=math.sqrt(math.pow(k1,2)+math.pow(k2,2)) #programma aprēķina hipotenūzas garumu trijstūrim
print('Taisnlenķa trijstūra hipotenūzas garums:'"{:.2f}".format(h)) ##hipotenūzas garuma izvade
import random
cipars=random.random()#gadijuma skaitļa ģenerēšana
print("Gadījuma skaitlis no 0-1:", cipars) #skaitļa izvade