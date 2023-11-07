saraksts=[2,5,9,4,6,3,2,8]
saraksts.append('Cepums')#Šis elements tiks pievienots saraksta beigās
print(saraksts)

#izmet no beigām
saraksts.pop()
print(saraksts)

saraksts.insert(3, 'Hello!') #ievieto 3. no kreisās
print(saraksts)


saraksts.remove(6)#izdzēš norādīto vērtību
print(saraksts)

#funkcijas del pielietojums
tests=[1,2,3,4,5,6,7,8]
del tests[2]
print(tests)

del tests[3:6]
print(tests)

cipari=[1,2,3,4,5,6,7,8]
del cipari[2:5:2]
print(cipari)