# import functions
import random




class Pirate():
    def __init__(self,name,row,column):
        self.pirate_name = name
        self.row = row
        self.column = column
        self.pirate_direction = ''
        self.pirate_postion = [row,column]
        self.thirst = 0
    
    def get_name(self):
        return self.pirate_name
    
    def direction(self,user):
        self.pirate_direction = user
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

    def get_direction(self):
        return self.pirate_postion

    def drink_grog(self):
        self.thirst = 0
        print(f"{self.pirate_name} is drinking grog")
        print(f"Thirst level : {self.thirst}")

            

class Island():
    def __init__(self,row,column,water_percent):
        self.row = row
        self.column = column
        self.water_percent = water_percent
        self.map = []
    
        

    def Creation_island(self):
        self.map = [["UE" for j in range(self.column)] for i in range(self.row)]
        water_tile = int(self.row * self.column * self.water_percent / 100)
        for i in range(water_tile):
             row = random.randint(0,self.row - 1)
             column = random.randint(0,self.column - 1)
             self.map[row][column] = 'W '
        self.Treasure_location = []
    
    def Treasure(self):
        t_row = random.randint(0,self.row - 1)
        t_column = random.randint(0,self.column - 1)
        self.Treasure_location = [t_row,t_column]
        self.map[t_row][t_column] = 'T '
    
    def Pirate_location(self,pirate_location):
        self.map[pirate_location[0]][pirate_location[1]] = 'P'
        

    
    def get_treasure_location(self):
        return self.Treasure_location

    def Display_island(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j], end = ' ')
            print()

class Compass():
    def __init__(self,name, pirate_pos, treasure_pos):
        self.name = name
        self.pirate_pos = pirate_pos
        self.treasure_pos = treasure_pos
        self.treasure_locator = []
        


    def determine_location(self):
        self.treasure_locator = (self.pirate_pos[0] - self.treasure_pos[0]) + (self.pirate_pos[1] - self.pirate_pos[1])
        if self.treasure_locator > 7:
            print(f"Colder - {self.name} is far from the treasure ")
        
        elif self.treasure_locator < 7 and self.treasure_locator > 3:
            print(f"Warmer - {self.name} is quite close to the Treasure")
        
        elif self.treasure_locator < 3:
            print(f"Hotter - {self.name} is very close to the treasure") 




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
            print("Quitting ...")

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







class Game():
    def display_game(self,user):
        if user == 'Y':
            user_input = input("Before starting the game, would you like to read the instructions to the game [Y/N] : ")
            if user_input.lower() == 'y':
                instruction_output = game_instruction()
                instruction_output.instruction()
            island_size = []
            print("\nIsland Difficulty")
            print("1. Arrd - 10x10 ")
            print("2. Arrd..rr - 20x10")
            print("3. Very Arrrrd - 30x30")
            island_input = int(input("Select the game dificulty [1/2/3]: "))
            if island_input == 1:
                island_size = [10,10]
                water_density = 10
                print("hi")
            elif island_input == 2:
                island_size = [20,10]
                water_density = [20]
            elif island_input == 3:
                island_size = [30,30]
                water_density = [35]
            print(f"island_size[0] : {island_size[0]}")
            print(f"island_size[1] : {island_size[1]}")
            island_output = Island(island_size[0],island_size[1],water_density)
            island_output.Creation_island()
            island_output.Treasure()
            island_output.Display_island()

            # Pirate
            user_input = input("\nName of your Pirate \n")
            row = random.randint(0,island_size[0])
            column = random.randint(0,island_size[1])
            pirate_output = Pirate(user_input,row,column)
            pirate_name = pirate_output.get_name()
            user = 'n'
            while user.lower() != 'y':
                user_direction = input("Which direction would you like to go\nA) North \nB) South \nC) East \nD) West \n")
                pirate_output.direction(user_direction)
                pirate_postition = pirate_output.get_direction()

                # Island
                treasure_postion = island_output.get_treasure_location()
                island_output.Pirate_location(pirate_postition)
                if treasure_postion == pirate_postition:
                    print("You won")
                    exit()

                user_compass = input("WOuld you like to see your location in the compass[Y/N] : ")
                if user_compass.lower() ==  'y':
                    compass_output = Compass(pirate_name,pirate_postition,treasure_postion)
                    compass_output.determine_location()
                display_map = input("Do you want to display the map [y/n] \n")
                if display_map.lower() == 'y':
                    island_output.Display_island()
                else:
                    print("alright")
                print("pirate postion : ", pirate_postition)
                print("treasure_postion : ",treasure_postion)
                user = input("Quit game [Y/N] \n")
            






user = input("Would you like to the play the game 'Treasure Island' [Y/N] \n")
while user.lower()!= 'y' and user.lower() != 'n':
    print("\nInvalid input\n")
    user = input("Would you like to the play the game 'Treasure Island' [Y/N] \n")

output = Game()

output.display_game('Y')