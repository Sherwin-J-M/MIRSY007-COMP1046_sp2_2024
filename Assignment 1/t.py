water = 'w '
ue = 'Ue'
x = 10
l = []
for i in range(1):
    l.append('T ')
    for j in range(9):
        l.append(water)
        for k in range(10):
            l.append(ue)

import random
random.shuffle(l)
#print(l)

l1 = []
j = 0
b= 0 
for i in range(10):
    j+=10
    l1.append(l[b:j])
    b+=10
   
# print(l1)
    

for i in range(len(l1)):
    for j in range(len(l1[i])):
        print(l1[i][j], end =  '  ')
    print()


