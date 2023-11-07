suna_vecums=int(input('Ievadiet suņa vecumu ar skaitļiem:'))
if suna_vecums<0:
    print('Suņa vecums nevar būt 0')
elif suna_vecums>0 and suna_vecums<3:
    print('Suņa vecums cilvēka gados ir', suna_vecums*10.5)
else:
    print('Šuņa vecums cilvēka gados ir', suna_vecums*4+2*10.5)