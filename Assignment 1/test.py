# import functions
import random


# Creation of Class 'Pirate'
class Pirate():
    def __init__(self, name, row, column):
        self.pirate_name = name
        self.row = row
        self.column = column
        self.pirate_direction = ''
        self.pirate_postion = [row, column]
        self.thirst = 0

    def get_name(self):
        return self.pirate_name

    def direction(self, user):
        self.pirate_direction = user
        if self.pirate_direction.upper() == 'NORTH' or self.pirate_direction.upper() == 'A':
            self.row -= 1
            self.pirate_postion = [self.row, self.column]
            print(f"\n=================================\n{
                  self.pirate_name} is moving a tile North \n=================================\n")

        elif self.pirate_direction.upper() == 'SOUTH' or self.pirate_direction.upper() == 'B':
            self.row += 1
            self.pirate_postion = [self.row, self.column]
            print(f"\n=================================\n{
                  self.pirate_name} is moving a tile SOUTH \n=================================\n")

        elif self.pirate_direction.upper() == 'WEST' or self.pirate_direction.upper() == 'C':
            self.column -= 1
            self.pirate_postion = [self.row, self.column]
            print(f"\n=================================\n{
                  self.pirate_name} is moving a tile WEST \n=================================\n")

        elif self.pirate_direction.upper() == 'EAST' or self.pirate_direction.upper() == 'D':
            self.column += 1
            self.pirate_postion = [self.row, self.column]
            print(f"\n=================================\n{
                  self.pirate_name} is moving a tile EAST \n=================================\n")

    def get_direction(self):
        return self.pirate_postion

    def drink_grog(self):
        self.thirst = 0
        print(f"{self.pirate_name} is drinking grog")
        print(f"Thirst level : {self.thirst}\n")

    def get_thirst(self):
        return self.thirst


class Island():
    def __init__(self, row, column, water_percent):
        self.row = row
        self.column = column
        self.water_percent = water_percent
        self.map = []

    def Creation_island(self):
        self.map = [["UE" for j in range(self.column)]
                    for i in range(self.row)]
        water_tile = int(self.row * self.column * self.water_percent / 100)
        for i in range(water_tile):
            row = random.randint(0, self.row - 1)
            column = random.randint(0, self.column - 1)
            self.map[row][column] = 'W '
        self.Treasure_location = []

    def Treasure(self):
        t_row = random.randint(0, self.row - 1)
        t_column = random.randint(0, self.column - 1)
        self.Treasure_location = [t_row, t_column]
        self.map[t_row][t_column] = 'T '

    def Pirate_location(self, pirate_location):
        self.map[pirate_location[0]][pirate_location[1]] = 'P'

    def find_water(self, pirate_location):
        statement = False
        if self.map[pirate_location[0]][pirate_location[1]] == 'W':
            statement = True
        return statement

    def get_treasure_location(self):
        return self.Treasure_location

    def Display_island(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j], end=' ')
            print()

    def display_treasure(self):
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


class Compass():
    def __init__(self, name, pirate_pos, treasure_pos):
        self.name = name
        self.pirate_pos = pirate_pos
        self.treasure_pos = treasure_pos
        self.treasure_locator = []

    def determine_location(self):
        self.treasure_locator = (
            self.pirate_pos[0] - self.treasure_pos[0]) + (self.pirate_pos[1] - self.pirate_pos[1])
        if self.treasure_locator > 7:
            print(f"==============================================\nColder - {
                  self.name} is far from the treasure \n==============================================\n")

        elif self.treasure_locator < 7 and self.treasure_locator > 3:
            print(f"==============================================\nWarmer - {
                  self.name} is quite close to the Treasure \n==============================================\n")

        elif self.treasure_locator < 3:
            print(f"==============================================\nHotter - {
                  self.name} is very close to the treasure\n==============================================\n")


class game_instruction():
    def instruction(self):
        print("\n+===========================+  \n|      Game Instruction     |\n+===========================+")
        print("| 1. About the Island       | \n----------------------------- \n| 2. About the pirate       | \n----------------------------- \n| 3. About the compass      | \n----------------------------- \n| 4. About the treasure     | \n----------------------------- \n| 5. Quit game instruction? | \n+===========================+\n")
        user_choice = input("Enter your choice : ")
        if user_choice == '1':
            self.about_Island()
            self.instruction()

        elif user_choice == '2':
            self.about_pirate()
            self.instruction()

        elif user_choice == '3':
            self.about_compass()
            self.instruction()

        elif user_choice == '4':
            self.about_Treasure()
            self.instruction()

        elif user_choice == '5':
            print("Quitting ...\n\n")

        else:
            print("\n----- Invalid input! -----")
            print("\n--- Please try again :) --")
            self.instruction()

    def about_Island(self):
        print("\nAbout the Island")
        print("-----------------")

    def about_pirate(self):
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
        print("")

    def about_compass(self):
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
        print("==================================================================")
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
        print("| 2. It is not visible to the pirate                                               |")
        print("| 3. Treasure is placed on the land and is not placed under water                  |")
        print("+----------------------------------------------------------------------------------+\n\n")


class Game():
    def display_game(self, user):
        if user == 'Y':
            user_input = input(
                "\nBefore starting the game, would you like to read the instructions to the game [Y/N] : ")
            if user_input.lower() == 'y':
                instruction_output = game_instruction()
                instruction_output.instruction()
            island_size = []
            print("+=====================+")
            print("|   Game Difficulty   |")
            print("+=====================+")
            print("| 1. Arrd             |")
            print("| 2. Arrd..rr         |")
            print("| 3. Very Arrrrd      |")
            print("+=====================+")
            island_input = int(input("Select Difficulty : "))
            if island_input == 1:
                island_size = [10, 10]
                water_density = 10
            elif island_input == 2:
                island_size = [20, 10]
                water_density = 20
            elif island_input == 3:
                island_size = [30, 30]
                water_density = 35

            island_output = Island(
                island_size[0], island_size[1], water_density)
            island_output.Creation_island()
            island_output.Treasure()
            island_output.Display_island()

            # Pirate
            user_input = input("\nName your Pirate : ")
            row = random.randint(0, island_size[0])
            column = random.randint(0, island_size[1])
            pirate_output = Pirate(user_input, row, column)
            pirate_name = pirate_output.get_name()
            pirate_thirst = pirate_output.get_thirst()

            user = 'n'
            while user.lower() != 'y':

                # Save the previous pirate location - Used to rewind the pirate location when in contact iwht water

                user_direction = input(
                    "\n\nWhere? \nA) North \nB) South \nC) East \nD) West \nEnter: ")
                pirate_output.direction(user_direction)
                pirate_postition = pirate_output.get_direction()
                find_water = island_output.find_water(pirate_postition)
                if find_water == True:
                    print("\nContacted water\n")

                # Pirate thirst level
                if pirate_thirst > 50 and pirate_thirst < 74:
                    print(f"{pirate_name} is feeling thirsty")
                elif pirate_thirst > 75 and pirate_thirst < 99:
                    print(f"{pirate_name} is feeling very thirsty")

                while pirate_thirst >= 100:
                    print(f"{pirate_name} cannot move drink grog")
                    user_input = input(
                        f"Drink grog [Y/N] else {pirate_name} dies \n")
                    if user_input.lower() == 'y':
                        pirate_output.drink_grog()
                        pirate_thirst = 0

                # Island
                treasure_postion = island_output.get_treasure_location()
                island_output.Pirate_location(pirate_postition)
                if treasure_postion == pirate_postition:
                    print("Congrajulation you found the Treasure")
                    island_output.display_treasure()
                    exit()

                user_compass = input(
                    "Would you like to see your location in the compass[Y/N] : ")
                if user_compass.lower() == 'y':
                    compass_output = Compass(
                        pirate_name, pirate_postition, treasure_postion)
                    compass_output.determine_location()
                display_map = input(
                    "\nDo you want to display the Treasure map [y/n] \n")
                if display_map.lower() == 'y':
                    island_output.Display_island()
                pirate_thirst += 10
                print(f"Pirate thirst level : {pirate_thirst}")


user = input("Would you like to the play the game 'Treasure Island' [Y/N] : ")
while user.lower() != 'y' and user.lower() != 'n':
    print("\nInvalid input\n")
    user = input(
        "Would you like to the play the game 'Treasure Island' [Y/N] \n")

output = Game()

output.display_game('Y')
