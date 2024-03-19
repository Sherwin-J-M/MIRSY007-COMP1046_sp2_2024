class Pirate():
    def __init__(self,name,row,column):
        self.pirate_name = name
        self.pirate_direction = input("\nA) North \nB) South \nC) East \nD) West \nWhich direction would you like to go ")
        self.row = row
        self.column = column
        self.pirate_postion = [self.row,self.column]
        self.thirst = 0
    
    def direction(self):
        if self.pirate_direction.upper() == 'NORTH' or self.pirate_direction.upper() == 'A':
            self.row -= 1
            self.pirate_postion = [self.row,self.column]
            print(f"{self.pirate_name} is moving a tile North")
        
        elif self.pirate_direction.upper() == 'SOUTH' or self.pirate_direction.upper() == 'B':
            self.row += 1
            self.pirate_postion = [self.row,self.column]
            print(f"{self.pirate_name} is moving a tile SOUTH")
        
        elif self.pirate_direction.upper() == 'WEST' or self.pirate_direction.upper() == 'C':
            self.column -= 1
            self.pirate_postion = [self.row,self.column]
            print(f"{self.pirate_name} is moving a tile WEST")
        
        elif self.pirate_direction.upper() == 'EAST' or self.pirate_direction.upper() == 'D':
            self.column += 1
            self.pirate_postion = [self.row,self.column]
            print(f"{self.pirate_name} is moving a tile EAST")
        
    def postion(self):
        return self.pirate_postion

    def drink_grog(self):
        self.thirst = 0
        print(f"{self.pirate_name} is drinking grog")
        print(f"Thirst level : {self.thirst}")



class Treasure():
    def __init__(self,row,column):
        self.treasure_positon = [row,column]



class Compass(Pirate,Treasure):
    def __init__(self, name, row, column, treasure_row, treasure_column):
        Pirate.postion(self)
        Treasure.__init__(self, treasure_row, treasure_column)
        self.treaure_locator = []

    def determine_location(self):
        self.locator = self.pirate_postion[0] - self.treasure_positon[0] + self.pirate_postion[1] - self.treasure_positon[1]
        if self.treaure_locator > 7:
            print(f"Colder - {self.pirate_name} is far from the treasure ")
        
        elif self.treaure_locator < 7 and self.treaure_locator > 3:
            print(f"Warmer - {self.pirate_name} is quite close to the Treasure")
        
        elif self.treaure_locator < 3:
            print(f"Hotter - {self.pirate_name} is very close to the treasure")


output = Compass("Jack",2,4,5,7)
output.determine_location