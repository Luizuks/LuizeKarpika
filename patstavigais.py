'''izveidot 3 sarakstus: 
>Lietotājs pats norādīs cik elementus likt sarakstā.
>Pirmā un otrā saraksta vērtības ievada lietotājs.
>Trešā saraksta vērtības iegūst apviwenojot pirmos 2 sarakstus
>Katra saraksta saturu glīti parādīt uz ekrāna

saraksts1=[]
saraksts2=[]
saraksts3=[]

elementi1=0
elementi2=0

elementi1=int(input('Ievadiet 1. saraksta vērtību daudzumu:'))
elementi2=int(input('Ievadiet 2. saraksta vērtību daudzumu:'))

for i in range(elementi1):
    i= +1
    s=input(f'Kāda vērtība būs elementam nr {i}:')
    saraksts1.append(elementi1)
    saraksts1[]
print(saraksts1)

for i in range(elementi2):
    i += 1
    s=input(f'Kāda vērtība būs elementam nr {i}:')
    saraksts2=[s]
print(saraksts2)

saraksts3=saraksts1+saraksts2
print(f'Trešais saraksts ir:{saraksts3}')

'''



saraksts = []
pirmsar = int(input('Ievadi pirmā saraksta elementu skaitu: '))
for i in range(0,pirmsar):
    elem = input('Ievadi elementus: ')
    saraksts.append(elem)

saraksts2 = []
otrsar = int(input('Ievadi otrā saraksta elementu skaitu: '))
for x in range(0,otrsar):
    elem2 = input('Ievadi elementus: ')
    saraksts2.append(elem2)

saraksts3 = saraksts + saraksts2
print('**************\nPirmais saraksts: ',saraksts)
print('Otrais saraksts: ',saraksts2)
print('**************\nKopējais saraksts ir: ',saraksts3,'\n**************')