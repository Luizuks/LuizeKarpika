print('Metamā kauliņa mešanas sacensības ')
speletajs1=input('Ievadiet pirmā spēlētāja vārdu:')
speletajs2=input('Ievadiet otrā spēlētāja vārdu:')
metsk= int(input('Ievadiet metienu skaitu:'))
punkti2, punkti1=0,0

for  i in range(1,metsk+1):
        punkti1+=int(input(f'Ievadiet {speletajs1} {i}, metiena rezultātu: '))
        punkti2+=int(input(f'Ievadiet {speletajs2} {i}, metiena rezultāts:'))
print('\t---')

print(f'Spēlētāja {speletajs1} punktu summa: {punkti1}')
print(f'Spēlētāja {speletajs2} punktu summa: {punkti2}')
if punkti2>punkti1:
        print(f'Uzvar! {speletajs2}')
elif punkti2<punkti1:
        print(f'Uzvar! {speletajs1}')
else:
        print('Neizšķirts!')