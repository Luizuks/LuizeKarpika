#izdrukāt skaitļus 0,1,2,3,4,5
#for i in range(5): #deflautā sāksies ar 0
   # print(i)
#print('--------------------------------')
#izdrukāt skaitļus 3,5,7
#for i in range(3,8,2):
    #print(i)

'''n=int(input('Ievadiet skaitli:'))
for i in range(1,11):
    print(n,'+',i, '=', n+1)
print('--------------------------------')'''
#atrast skaitļu 2 un 4 dalītājus
#uz ekrāna parādīt tos, kas dalās ar 2, tos, kas dalās gan ar 4 gan ar 2 un ar abiem
#range 50

for i in range(51):
    if i%2==0 and i%4==0:
        print(i,'skaitlis dalās gan ar 4, gan ar 2')
    elif i%2==0:
        print(i, 'Skaitlis dalās ar 2')
    else:
        print(i)