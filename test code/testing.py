# import functions
import random




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

        return self.pirate_postion
        

    def drink_grog(self):
        self.thirst = 0
        print(f"{self.pirate_name} is drinking grog")
        print(f"Thirst level : {self.thirst}")



class Treasure():
    def __init__(self,row,column):
        self.treasure_positon = [row,column]

    def treasure_location(self):
        return self.treasure_positon



class Compass(Pirate,Treasure):
    def __init__(self, row, column):
        super().__init__(row, column)
        self.treaure_locator = []

    def determine_location(self):
        self.locator = [self.pirate_postion[0] - self.treasure_positon[0],self.pirate_postion[1] - self.treasure_positon[1]]
        if self.treaure_locator > 7:
            print(f"Colder - {self.pirate_name} is far from the treasure ")
        
        elif self.treaure_locator < 7 and self.treaure_locator > 3:
            print(f"Warmer - {self.pirate_name} is quite close to the Treasure")
        
        elif self.treaure_locator < 3:
            print(f"Hotter - {self.pirate_name} is very close to the treasure")

class Island():
    def __init__(self,size,water_density):
        self.size = size
        self.water_density = water_density
        self.map = []

    def Creation_island(self):
        water = int(self.size[0] * self.size[1] * self.water_density/100)
        water_tiles = random.sample
        
    
    def Display_island(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j], end = ' ')
            print()


class game_instruction():
    def instruction(self):
        print("\nGame Instruction")
        print("1. About the Island \n2. About the pirate \n3. About the compass \n4. About the treasure \n5. Quit game instruction?")
        user_choice = int(input("\nEnter your choice : "))
        if user_choice == 1:
            self.about_Island()

        elif user_choice == 2:
            self.about_pirate()

        elif user_choice == 3:
            self.about_compass()

        elif user_choice == 4:
            self.about_Treasure()

        elif user_choice == 5:
            quit()

        else:
            print("Invalid input!")
            self.instruction()
    
    def about_Island(self):
        print("\nAbout the Island")
        
    def about_pirate(self):
        print("\nAbout the Pirate")

    def about_compass(self):
        print("\nAbout the Compass")

    def about_Treasure(self):
        print("\nAbout the Treasure")

# Assigning all 'Class'  to a variable





island_output = Island()





class Game():
    def __init__(self,user):
        self.pirate = Pirate(user)
        self.Treasure = Treasure()
        self.compass = Compass()

    def display_game(self):
        if self.user_input.upper() == 'Y':
            user_input = input("Before starting the game, would you like to read the instructions to the game [Y/N] : ")
            if user_input.lower() == 'y':
                instruction_output = game_instruction()
                instruction_output.instruction()
            user_input = input("\nWhat would you like to name your pirate as? ")
            pirate_output = Pirate(user_input,2,3)
            pirate_output.direction()
            treasure_output = Treasure(4,4)
            treasure_output.treasure_location()
            user_compass = input("WOuld you like to see your location in the compass[Y/N] : ")
            if user_compass.lower() ==  'y':
                compass_output = Compass()
                






output = Game('Y')

output.display_game()
        