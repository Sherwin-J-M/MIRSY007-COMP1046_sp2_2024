'''
File: IslandGame.py
Description: A brief description of this Python module.
Author: Sherwin john Miranda
ID: 1104173621
Username: MIRSY007
This is my own work as defined by the University's Academic Misconduct Policy.
'''



import random 
class Pirate():
    def __init__(self,name):
        self.name = name
        self.direction = input("Which direction would you like to go \nN - North \nS - South \nE - East \nW - West \nEnter your choice [N/S/E/W] : ")
        self.thirst = 0
        self.x = 0
        self.y = 0
        self.travel = []


    def movement(self):
        if self.direction.lower() == 'n' :
            self.y += 1
            print(f"{self.name} is moving a tile North")
        
        elif self.direction.lower() == 's' :
            self.y -= 1
            print(f"{self.name} is moving a tile South")

        elif self.direction.lower() == 'e' :
            self.x += 1
            print(f"{self.name} is moving a tile East")
        
        elif self.direction.lower() == 'w' :
            self.x -= 1
            print(f"{self.name} is moving a tile West")
        
    def drink_grog(self):
        self.thirst = 0
        print(f"{self.name} is drinking grog")
    
        
        


class Treasure():
    def __init__(self,x,x1,y,y1):
        self.x = random.randint(x,x1)
        self.y = random.randint(y,y1)

class Compass():
    pass
    

class Island():
    def __init__(self,row,column,water_percent):
        self.row = row
        self.column = column
        self.water_percent = water_percent
        self.map = []

    def Creation_island(self):
        self.map = [["UE" for j in range(self.column) for i in range(self.row)]]
        water_tile = int(self.row * self.column * self.water_percent / 100)
        for i in range(water_tile):
             row = random.randint(0,self.row - 1)
             column = random.randint(0,self.column - 1)
             self.map[row][column] = 'W '
        
        return self.map
    
    def display_island(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j], end = ' ')
            print()
       


    


    def pirate_location(self):
        pass

    def water_location(self):
        pass

    def treasure_location(self):
        pass




class Game():
    def __init__(self):
        pass

    def start_game(self):
        print("Welcome to Treasure Island")
        self.difficulty()
        self.pirate = Pirate()
        self.pirate.__init__("enter")
        self.island = Island(10,10) #Default value 
        self.island.Creation_island()
        self.island.Display_island()
        
    
    def difficulty(self):
        print("Select your difficulty level")
        print("[1] Arrrd - 10 by 10 grid and 10% of the island containing water.")
        print("[2] Arrrd..rrr - 20 by 10 grid and 20% of the island containing water.")
        print("[3] Very Arrrrd - 30 by 30 grid and 30% of the island containing water.")

        user_choice = int(input("Choice [[1]/[2]/[3] : " ))
        if user_choice == 1:
            self.island = Island(10,10)
        elif user_choice == 2:
            self.island = Island(20,10)
        elif user_choice == 3:
            self.island = Island(30,30)
        else:
            print("Invalid choice! Please try again.")
            self.difficulty()
        
    

    
    def instruction(self):
        pass

    def game_quit(self):
        pass


game = Game()
game.start_game()