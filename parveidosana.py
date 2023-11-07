#int pārveidošana par str
a=5
b=7
print('Skaitlis:',a + b )
print('Teksts',str(a)+str(b)) #concat
#izveidot 2 mainīgos ar str tipu, pirmā vērtība '1,2,3', otrs '456'
#pārveidot šos datus par int tipu
#noteikt datu tipu
a,b='123','456'
a_tips, b_tips= int(a), int(b)
print(a_tips+b_tips, type(a_tips,b_tips))