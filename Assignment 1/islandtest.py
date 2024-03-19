import random
island = [['UE','UE','UE','WT','T'],['WT','UE','UE','WT','UE'],['WT','WT','WT','UE','UE'],['WT','WT','WT','UE','UE'],['WT','WT','WT','UE','UE'],['WT','WT','WT','UE','UE'],['WT','WT','WT','UE','UE']]
random.shuffle(island)
for i in range(len(island)):
    random.shuffle(island[i])
    for j in range(len(island[i])):
        print(island[i][j], end = ' ')
    print()

a1 = [-1,1]
x = random.randint(-1,1)
y = 0


if x == -1 or x == 1:
    y = 0
elif x == 0:
    y = random.randint(-1,1)

print(x)
print(y)


game = 0
while game < 5:
    island[x][y] = 'X'

    user_input = int(input("1) North \n2) South \n3) West \n4) East \nEnter direction "))
    if user_input == 1:
        x -= 1
        island[x][y] = 'X'
    elif user_input == 2:
        x += 1
        island[x][y] = 'X'
    elif user_input == 3:
        y -= 1
        island[x][y] = 'X'
    elif user_input == 4:
        y += 1
        island[x][y] = 'X'


    for i in range(len(island)):
        for j in range(len(island[i])):
            print(island[i][j], end = ' ')
        print()
    if game == 4:
        user_input = input("Quit [Y/N]? ")
        if user_input.upper() ==  'N':
            game = 0
    game += 1