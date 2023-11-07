'''atbilde='j'
while atbilde=='j':
    print ('Nekusties!')
    atbilde= input('Vai briesmonis ir draudzīgs(j/n)?')
print('Bēdz prom!')'''

#pārbaudīt vai lietotājs prot reizināt ar 7
#programma atkārto darbību līdz brīdim, kad uzdoti visi 12 jautājumi
reiz= int(input('Reizinātājs'))
for i in range(1,13): #Cikla mainīgais no 1 līdz 12
    print('Cik ir',i,'reiz',reiz, '?')
    minejums= input()
    if minejums== 'stop':
        break #pārtrauc programmu
    if minejums=='izlaist':
        continue #izlaiž 1 jautājumu un turpina tālāk
    atb=i*reiz
    if int(minejums)==atb:
        print('Pareizi!')
    else:
        print('Nepareizi, atbilde ir',atb)
    #ja ir nepareizi, tad atgriežas pie jautājuma
    #reizinātāju ievada lietotājs
