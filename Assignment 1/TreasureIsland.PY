'''
File: TreasureIsland.py
Description: A brief description of this Python module.
This is the code for the Treasure Island game, which has been coded the structure based on the user input
through user input the code does various function from moving the pirate, finding the treasure, selecting the difficulty of the map, using the compass, and the game instructions
This code has been structured in a way that does not take invalid input from the use and has been almost made error free (Hopefully) with all the functions accordingly to what it is assigned to do.
Thank you and please enjoy

Author: Sherwin John Miranda
ID: 110417362
Username: MIRSY007
This is my own work as defined by the University's Academic Misconduct Policy.
'''


# import functions
import random


# Creation of Class 'Pirate'
class PIRATE():
    def __init__(self, name, row, column):
        self.__pirate_name = name
        self.__row = row
        self.__column = column
        self.__pirate_direction = ''
        self.__pirate_postion = [row, column]
        self.__pirate_direction = 0
        self.__thirst = 0
        self.__previous_directon = []

    def get_name(self):
        return self.__pirate_name  # returns the name the user has given

    # Code for moving the pirate within the map
    def direction(self, island):
        # This is the user input for which direction he wants the pirate to move
        loop = True
        while loop == True:
            self.__pirate_direction = input(
                "\n\nWhere? \n1) North \n2) South \n3) West \n4) East \nEnter: ")
            # Pirate moves based on the input, If pirate goes outside the map it display as message and return false and looped which is coded within the 'GAME' class
            # When the direction is chosen either "row" or "column" gets reduced or increased by '1' which helps change pirates direction
            if self.__pirate_direction.upper() == 'NORTH' or self.__pirate_direction == '1':
                if self.__row > 0:
                    self.__row -= 1
                    self.__pirate_postion = [self.__row, self.__column]
                    print(f"\n=================================\n{self.__pirate_name} is moving a tile North \n=================================\n")
                    loop = False
                else:
                    print("Cannot go outside the map")
                    self.direction(island)

            # The parameter Island is used to check whether the pirate is going outside the boundary
                # It is accessed from the "Island" class which is implemented within "GAME" class
            elif self.__pirate_direction.upper() == 'SOUTH' or self.__pirate_direction == '2':
                if self.__row < island[0] - 1:
                    self.__row += 1
                    self.__pirate_postion = [self.__row, self.__column]
                    print(f"\n=================================\n{self.__pirate_name} is moving a tile SOUTH \n=================================\n")
                    loop = False
                else:
                    print("Cannot go outside the map")
                    self.direction(island)

            elif self.__pirate_direction.upper() == 'WEST' or self.__pirate_direction == '3':
                if self.__column > 0:
                    self.__column -= 1
                    self.__pirate_postion = [self.__row, self.__column]
                    print(f"\n=================================\n{self.__pirate_name} is moving a tile WEST \n=================================\n")
                    loop = False
                else:
                    print("Cannot go outside the map")
                    self.direction(island)

            elif self.__pirate_direction.upper() == 'EAST' or self.__pirate_direction == '4':
                if self.__column < island[1] - 1:
                    self.__column += 1
                    self.__pirate_postion = [self.__row, self.__column]
                    print(f"\n=================================\n{self.__pirate_name} is moving a tile EAST \n=================================\n")
                    loop = False
                else:
                    print("Cannot go outside the map")
                    self.direction(island)    
    
    # Given to set a previous direction to use when pirate come in contact with water
    def set_previous_direction(self):
        if self.__pirate_direction.upper() == 'NORTH' or self.__pirate_direction == '1':
            self.__row += 1
            self.__pirate_postion = [self.__row, self.__column]

        elif self.__pirate_direction.upper() == 'SOUTH' or self.__pirate_direction == '2':
            self.__row -= 1
            self.__pirate_postion = [self.__row, self.__column]

        elif self.__pirate_direction.upper() == 'WEST' or self.__pirate_direction == '3':
            self.__column += 1
            self.__pirate_postion = [self.__row, self.__column]

        elif self.__pirate_direction.upper() == 'EAST' or self.__pirate_direction == '4':
            self.__column -= 1
            self.__pirate_postion = [self.__row, self.__column]

    # Used to replace the previous direction of pirate to "E" when the pirate changes direction
    def set_Explored_direction(self):
        self.prev_row = self.__row
        self.prev_column = self.__column
        if self.__pirate_direction.upper() == 'NORTH' or self.__pirate_direction == '1':
            self.prev_row += 1

        elif self.__pirate_direction.upper() == 'SOUTH' or self.__pirate_direction == '2':
            self.prev_row -= 1

        elif self.__pirate_direction.upper() == 'WEST' or self.__pirate_direction == '3':
            self.prev_column += 1

        elif self.__pirate_direction.upper() == 'EAST' or self.__pirate_direction == '4':
            self.prev_column -= 1

        self.__previous_directon = [self.prev_row, self.prev_column]
        return self.__previous_directon

    # Return the pirates position which was changed in the above function "direction(self, user,island)"

    def get_direction(self):
        return self.__pirate_postion

    # Code to bring thirst level to 0 when accesed
    def drink_grog(self):
        print(f"{self.__pirate_name} is drinking grog")
        print(f"Thirst level : {self.__thirst}\n")

    def set_thirst(self):
        self.__thirst += 10

    def set_reset_thirst(self):
        self.__thirst = 0

    # Returns the pirates level of thirst
    def get_thirst(self):
        return self.__thirst


# Island creation
class ISLAND():
    # These parameter are given in the class "GAME"
    def __init__(self, row, column, water_percent):
        self.__row = row
        self.__column = column
        self.__water_percent = water_percent
        self.__map = []
        self.__mapsize = [self.__row, self.__column]
        self.__Treasure_location = []

    # Creation of the island
    def Creation_island(self):
        # This creates the map with all values as "UE" then some of the values changed to the below
        self.__map = [["UE" for j in range(self.__column)]
                      for i in range(self.__row)]

        # To calculate the amount of water needed within the map
        water_tile = int(self.__row * self.__column *
                         self.__water_percent / 100)

        # Then that water is added randomly to the location in the map
        for i in range(water_tile):
            row = random.randint(0, self.__row - 1)
            column = random.randint(0, self.__column - 1)
            self.__map[row][column] = 'W '

    # Randomly placing the Treasure within the map
    def set_Treasure(self):
        # To give a random location for the Treasure
        t_row = random.randint(0, self.__row - 1)
        t_column = random.randint(0, self.__column - 1)

        # To ensure the Treasure is not placed on the water tile
        while self.__map[t_row][t_column] == 'W ':
            t_row = random.randint(0, self.__row - 1)
            t_column = random.randint(0, self.__column - 1)
        # Just used to verify if treasure is implemented within the map or not
        # self.__map[t_row][t_column] = 'T '

        # This is for Determine treasure location whihc is used in the class "Compass"
        self.__Treasure_location = [t_row, t_column]

    # To get the map size which is used to check the maps boundary level (Used in teh Class "GAME" and "PIRATE")

    def get_mapsize(self):
        return self.__mapsize

    # Add Pirate to the map
    def Pirate_location(self, pirate_location):     
        self.__map[pirate_location[0]][pirate_location[1]] = 'P '
        
    def set_Explored_Location(self, pirate_location):
        self.__map[pirate_location[0]][pirate_location[1]] = 'E '

    # To determine if the pirate as stepped on water or not

    def find_water(self, pirate_location):
        statement = False
        # If pirate steps on water then it returns "TRUE"
        if self.__map[pirate_location[0]][pirate_location[1]] == 'W ':
            statement = True
        return statement

    # Returns the Treasure location, also used in the class "COMPASS"
    def get_treasure_location(self):
        return self.__Treasure_location

    # Displays the Map when the game starts
    def Display_island(self):
        for map in self.__map:
            # These print statements with special symbols like '|' and '-' are used to a clean visual display
            print("|----" * (self.__column) + '|')
            print('| '+" | ".join(map) + " |")
        print("|----" * (self.__column) + '|')

    def display_treasure(self):
        # To display the Treasure once the pirate finds it
        # Used print(r"....) as without it, it thinks print(... \ ) as a escape sequence
        print(
            r"  <------------------------------------------------------------------------> ")
        print(
            r"  \  -------------------------------------------------------------------  /")
        print(r"   \ \                                                                 / /")
        print(r"    \ \                                                               / /")
        print(r"     \ \                                                             / /")
        print(r"      \ \                                                           / /")
        print(r"       \ \                                                         / /")
        print(r"        \ \                                                       / /")
        print(r"         \_\_____________________________________________________/_/")
        print(r"         / _______________________________________________________ \. ")
        print(r"       ./ /                                                       \ \.")
        print(
            r"      ./ /    [Precious Stones]                  [Pearls]          \ \.")
        print(r"     ./ /                                                           \ \.")
        print(
            r"    ./ /                          [Treasure]                         \ \.")
        print(r"   ./ /                                                               \ \.")
        print(
            r"  ./ /                                                                 \ \.")
        print(
            r" ./ /          [Gold]                                [Diamond]          \ \.")
        print(
            r"./ /_____________________________________________________________________\ \.")
        print(
            r"----------------------------------------------------------------------------")
        print(
            r"\                                  |  0  |                                 /")
        print(
            r" \                                 |  |  |                                /")
        print(r"  \                                |_____|                               /")
        print(r"   \                                                                    /")
        print(r"    \                                                                  /")
        print(r"     \________________________________________________________________/")

# Compass creation to determine the treasure


class COMPASS():
    # These parameter  are provided in the "GAME" class
    def __init__(self, name, pirate_pos, treasure_pos):
        self.__name = name
        self.__pirate_pos = pirate_pos  # Takes the pirate postion
        self.__treasure_pos = treasure_pos  # Takes the Treasure postion
        self.__treasure_locator = []

    # Determines the Treasure location using from the mentioned above variable/function
    def determine_location(self):
        # This is used to determine distance between pirate and treasure
        self.__treasure_locator = abs(self.__pirate_pos[0] - self.__treasure_pos[0]) + abs(self.__pirate_pos[1] - self.__treasure_pos[1])
        
        # Displays the message based on the distance
        if self.__treasure_locator > 7:
            print(f"==============================================\nColder - {self.__name} is far from the treasure \n==============================================\n")

        elif self.__treasure_locator <= 7 and self.__treasure_locator > 3:
            print(f"==============================================\nWarmer - {self.__name} is quite close to the Treasure \n==============================================\n")

        elif self.__treasure_locator <= 3:
            print(f"==============================================\nHotter - {self.__name} is very close to the treasure\n==============================================\n")

# Basic instructions for the user to understand the game


class GAME_INSTRUCTION():
    # This entire section is just about game instruction
    def Instruction(self):
        print("\n+===========================+  \n|      Game Instruction     |\n+===========================+")
        print("| 1. About the Island       | \n----------------------------- \n| 2. About the pirate       | \n----------------------------- \n| 3. About the compass      | \n----------------------------- \n| 4. About the treasure     | \n----------------------------- \n| 5. Quit game instruction? | \n+===========================+\n")
        # User gives their input
        user_choice = input("Enter your choice : ")

        # Once users enter their input, the chosen shows the required instruction by accessing from the below respective function
        if user_choice == '1':
            self.about_Island()
            self.Instruction()

        elif user_choice == '2':
            self.about_Pirate()
            self.Instruction()

        elif user_choice == '3':
            self.about_Compass()
            self.Instruction()

        elif user_choice == '4':
            self.about_Treasure()
            self.Instruction()

        elif user_choice == '5':
            print("Quitting ...\n\n")

        elif user_choice.lower() == 'quit':
            print("*** Quitting the game ....  ***")
            exit()

        else:
            print("\n----- Invalid input! -----")
            print("\n--- Please try again :) --")
            self.Instruction()

    def about_Island(self):
        print("\nAbout the Island")
        print("-----------------")
        print("An Island has a size and a density which are determined by the selected options")
        print("Islanc consists of :")
        print(" - UE -> UnExplored area ")
        print(" - E  -> Explored area")
        print(" - T  -> Treasure")
        print(" - W  -> Water")
        print(" - P  -> Pirate")

    def about_Pirate(self):
        print("\nAbout the Pirate")
        print("-----------------\n\n")
        print(r"                  ______  ")
        print(r"                 /      \ ")
        print(r"                /        \         ------> Pirate hat")
        print(r"            ___/          \___ ")
        print(r"           |__________________|    ")
        print(r"              |       \__   |  ")
        print(r"              | ( * ) {__}  |      ------> Eye patch")
        print(r"              \          \ / ")
        print(r"               \  [----]  /  ")
        print(r"                \________/     ")
        print(r"            _______|   |_______     ")
        print(r"           /                   \          ")
        print(r"          /                     \          ")
        print(r"         /   /|              |\  \          ")
        print(r"        /   / |              | \  \           ")
        print(r"       /   /  |              |  \  \            ")
        print(r"      /   /   |              |   \  \          ")
        print(r"     /   /    |              |    \  \          ")
        print(r"    /___/     |______________|     \__\           ")
        print(r"    / /       |              |       \.\__")
        print(r"   / /        |      ___     |            \.    ------> Hook")
        print(r"  /_/         |     |   |    |         (___)")
        print(r"              |     |   |    |")
        print(r"              |     |   |    |")
        print(r"              |     |   |    |")
        print(r"              |     |   |    |")
        print(r"              |     |   |    |")
        print(r"              |_____|   |____|")
        print(r"                |  |     |  |")
        print(r"                |  |     |  |")
        print(r"                |  |     |  |")
        print(r"                |__|     \__/        ------> Wooden leg")
        print("\n*** important note : Pirate cant come in contact with water due to his wooden leg ***")
        print("")

    def about_Compass(self):
        print("\nAbout the Compass")
        print("-----------------\n\n")
        print(r"                 _______________________")
        print(r"                /            |          \.")
        print(r"               /           |\ |          \.")
        print(r"              /            | \|           \.")
        print(r"             /                             \.")
        print(r"            /                               \.")
        print(r"           /                                 \.")
        print(r"          /                                   \.")
        print(r"         /                                     \.")
        print(r"         |                   /\                 |")
        print(r"         |                  /  \                |")
        print(r"         |                 /  N \           __  |")
        print(r"         |_ \  /\  /      /______\         |_  _|")
        print(r"         |   \/  \/       \      /         |__  |")
        print(r"         |                 \ S  /               |")
        print(r"         |                  \  /                |")
        print(r"         \                   \/                 /")
        print(r"          \                                    /")
        print(r"           \                                  /")
        print(r"            \                __              /")
        print(r"             \              |__             /")
        print(r"              \              _|            /")
        print(r"               \                          / ")
        print(r"                \____________|___________/")

        print("\n\nCompass Determines how close the Pirate is from the Treasure")
        print("==================================================================")
        print("|| Feedback |              Description                           ||")
        print("||===============================================================||")
        print("||  Colder  | The player is 7 or more space away from treasure.  ||")
        print("||----------|----------------------------------------------------||")
        print("||  Warmer  | The player is between 3 and 7 spaces.              ||")
        print("||----------|----------------------------------------------------||")
        print("||  Hotter  | The player is 3 or less spaces away                ||")
        print("==================================================================")

    def about_Treasure(self):
        print("\nAbout the Treasure")
        print("-----------------\n")
        print("+----------------------------------------------------------------------------------+")
        print("| 1. This is the main objective of the game. Pirate wins if the treasure is found  |")
        print("| 2. It is hidden within the Island                                                |")
        print("| 3. Treasure is placed on the land and is not placed under water                  |")
        print("+----------------------------------------------------------------------------------+\n\n")

# Creation of Game


class GAME():
    def display_game(self, user):
        if user == 'Y':
            print("\n+---------------------------------------------------------------+")
            print("| *** Important - If you want to quit the game, Type 'Quit' *** |")
            print("+---------------------------------------------------------------+")
            loop = True
            while loop == True:
                read_instruction_input = input(
                    "\nArrr, matey! Be ye wantin' to read the game's instructions before we set sail? [Y/N] : ")

                if read_instruction_input.lower() == 'y':
                    instruction_output = GAME_INSTRUCTION()
                    instruction_output.Instruction()
                    loop = False

                elif read_instruction_input.lower() == 'n':
                    print("Loading game ..... \n\n")
                    loop = False

                elif read_instruction_input.lower() == 'quit':
                    print("*** Quitting the game ....  ***")
                    exit()

                else:
                    print("\n+=======================+")
                    print("| *** Invalid Input *** |")
                    print("+=======================+\n")

            # Pirate
            print(
                r"_______ ______  _______       _      _______  ___    ___  ____  _______")
            print(
                r"|_   _| |  _  \ |  ____|     / \    | ______| | |    | | |  _ \ |  ____|")
            print(
                r"  | |   | |_| | |  |___     / _ \   | |_____  | |    | | | |_| ||  |___")
            print(
                r"  | |   |    _/ |   ___|   / /_\ \  |_____  | | |    | | |    _/|   ___|")
            print(
                r"  | |   | |\ \  |  |___   / _____ \  _____| | | |____| | | |\ \ |  |___")
            print(
                r"  |_|   |_| \_\ |______| /_/     \_\|_______| |________| |_| \_\|______|")
            print(
                "======================================================================== ")
            print(
                r"                             _______ _________ __            _      ___   __  _____")
            print(
                r"                             |_   _| | ______| | |          / \     |  \  | | |  _ \.")
            print(
                r"                               | |   | |_____  | |         / _ \    |   \ | | | | \ \.")
            print(
                r"                               | |   |_____  | | |        / /_\ \   | |\ \| | | |  | |")
            print(
                r"                              _| |_   _____| | | |____   / _____ \  | | \   | | |_/ /")
            print(
                r"                             |_____| |_______| |______| /_/     \_\ | |  \__| |____/")
            print(
                "                             ==========================================================")

            loop = True
            while loop == True:
                User_name_input = input(
                    "\nAhoy there, matey! What be yer name? : ")

                if not User_name_input.strip():
                    print("Arrr, tell me your name,")
                    loop = True

                elif len(User_name_input) < 3:
                    print("Arrr, that name be too short for a pirate!")
                    loop = True

                elif User_name_input.isdigit():
                    print(
                        "Shiver me timbers! Ye be givin' me numbers instead of a name!")
                    loop = True

                elif User_name_input.lower() == 'quit':
                    print("*** Quitting the game ....  ***")
                    exit()

                else:
                    loop = False

            print(f"\nAhoy, {User_name_input}! Ye be a fine pirate indeed!\n")

            # Island
            island_size = []
            print("\n+=====================+")
            print("|   Game Difficulty   |")
            print("+=====================+")
            print("| 1. Arrd             |")
            print("| 2. Arrd..rr         |")
            print("| 3. Very Arrrrd      |")
            print("+=====================+")

            loop = True
            while loop == True:
                Island_size_input = input(
                    "Avast, ye landlubber! What kind o' challenge be ye lookin' for? : ")
                # This is the cnahge the map size according to the users input
                if Island_size_input == '1':
                    island_size = [10, 10]
                    water_density = 10
                    print("Ye be settlin' for Arrd, aye?")
                    loop = False

                elif Island_size_input == '2':
                    island_size = [20, 10]
                    water_density = 20
                    print("Ye think ye be ready for Arrd..rr, do ye?")
                    loop = False

                elif Island_size_input == '3':
                    island_size = [30, 30]
                    water_density = 35
                    print("Ye be bold to choose Very Arrrrd!")
                    loop = False

                elif Island_size_input.lower() == 'quit':
                    print("*** Quitting the game ....  ***")
                    exit()

                else:
                    print("\n+=======================+")
                    print("| *** Invalid Input *** |")
                    print("+=======================+\n")

            # Island
            Island_Function = ISLAND(
                island_size[0], island_size[1], water_density)
            Island_Function.Creation_island()
            Island_Function.set_Treasure()
            Mapsize = Island_Function.get_mapsize()

            # Pirate
            # To create a random pirate location as well as a fixed centre pirate location within the map
            loop = True
            while loop == True:
                Pirate_location_input = input("\n\nWhere be ye wantin to start yer adventure matey? \n1. Random location \n2. Centre of the Map \nInput : " )
                if Pirate_location_input == '1':
                    pirate_postion_row = random.randint(0, island_size[0] - 1)
                    pirate_postion_column = random.randint(0, island_size[1] - 1)
                    loop = False
                elif Pirate_location_input == '2':
                    pirate_postion_row = island_size[0]//2
                    pirate_postion_column = island_size[1]//2
                    loop = False

                elif Pirate_location_input.lower() == 'quit':
                    print("*** Quitting the game ....  ***")
                    exit()

                else:
                    print("\n+=======================+")
                    print("| *** Invalid Input *** |")
                    print("+=======================+\n")

            Pirate_Function = PIRATE(
                User_name_input, pirate_postion_row, pirate_postion_column)
            pirate_name = Pirate_Function.get_name()
            pirate_position = Pirate_Function.get_direction()

            #
            Island_Function.Pirate_location(pirate_position)

            Distance_Traveled = 0
            # Used to create  while loop
            user = 'n'
            while user.lower() != 'y':
                pirate_thirst = Pirate_Function.get_thirst()
                # Pirate thirst level
                if pirate_thirst > 50 and pirate_thirst < 74:
                    print(f"{pirate_name} is feeling thirsty")
                elif pirate_thirst > 75 and pirate_thirst < 99:
                    print(f"{pirate_name} is feeling very thirsty")

                loop = True
                while pirate_thirst >= 100 and loop == True:
                    print(f"{pirate_name} can't move")
                    Drink_input = input(
                        f"Would ye care for some grog to quench yer thirst [Y/N]. We wouldn't want ye to meet Davy Jones, now would we? \n")
                    if Drink_input.lower() == 'y':
                        Pirate_Function.set_reset_thirst()
                        Pirate_Function.drink_grog()
                        loop = False

                    elif Drink_input.lower() == 'n':
                        print()

                    elif Drink_input.lower() == 'quit':
                        print("*** Quitting the game ....  ***")
                        exit()

                    else:
                        print("\n+=======================+")
                        print("| *** Invalid Input *** |")
                        print("+=======================+\n")

                # If False, It does not allow the pirate to walk beyond the maps border and goes on a constant loop till he changes direction which is within the map
                print("\nTREASURE MAP")
                print("==============")
                Island_Function.Display_island()
                Pirate_Function.direction(Mapsize)
                pirate_position = Pirate_Function.get_direction()
                pirate_Explored_Location = Pirate_Function.set_Explored_direction()
                # pirate_Explored_Location = Pirate_Function.set_previous_direction()
                Island_Function.set_Explored_Location(pirate_Explored_Location)

                # To determine if Pirate is walking on water or not
                Detect_water = Island_Function.find_water(pirate_position)
                # If true, It does not allow the pirate to walk on water, so goes on a constant loop till he walks only on land or finds the treasure
                while Detect_water == True:
                    # Sets pirates location to the which was before contact with water
                    Pirate_Function.set_previous_direction()
                    print(
                        "Arrr! Water ahead! Watch yer step, matey with a wooden leg! Change course or risk a soggy fate")
                    Pirate_Function.direction(Mapsize)
                    pirate_position = Pirate_Function.get_direction()
                    Detect_water = Island_Function.find_water(pirate_position)

                # Island
                Treasure_postion = Island_Function.get_treasure_location()
                if Treasure_postion == pirate_position:
                    print("Avast! Treasure found! Yo ho ho and a bottle of rum!")
                    Island_Function.display_treasure()
                    exit()

                loop = True
                while loop == True:
                    Compass_input = input(
                        "Arrr! Fancy a glance at yer bearings on the compass? [Y/N] : ")

                    if Compass_input.lower() == 'y':
                        Compass_Function = COMPASS(
                            pirate_name, pirate_position, Treasure_postion)
                        Compass_Function.determine_location()
                        loop = False

                    elif Compass_input.lower() == 'n':
                        loop = False

                    elif Compass_input.lower() == 'quit':
                        print("*** Quitting the game ....  ***")
                        exit()

                    else:
                        print("\n+=======================+")
                        print("| *** Invalid Input *** |")
                        print("+=======================+\n")

                Island_Function.Pirate_location(pirate_position)

                Pirate_Function.set_thirst()
                pirate_thirst = Pirate_Function.get_thirst()
                Distance_Traveled += 1
                print("\n\nPirate Details")
                print(f" |-> Pirate thirst level : {pirate_thirst}")
                print(f" |-> Distance Traveled : {Distance_Traveled}Km\n\n")

# User input to start the game or not
user = input("Would you like to the play the game 'Treasure Island' [Y/N] : ")

if user.lower() == 'quit':
    print("*** Quitting the game ....  ***")
    exit()
while user.lower() != 'y' and user.lower() != 'n':
    print("\n+=======================+")
    print("| *** Invalid Input *** |")
    print("+=======================+\n")
    user = input(
        "Would you like to the play the game 'Treasure Island' [Y/N] \n- ")

output = GAME()

output.display_game(user.upper())
