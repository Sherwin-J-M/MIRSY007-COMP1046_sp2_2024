class Pirate:
    def __init__(self):
        self.name = input("Enter the pirate's name : ")
        self.thirst = 0
        self.position = None
        self.trail = []
        self.travel = None

    def move(self):
        x = 0
        y = 0
        user_input = input("Which direction would you like to move \nA) North \nB) South \nC) West \nD) EAST \nEnter : ")
        if user_input.lower() == "north" or user_input.lower() == "a": 
            self.travel = 'North'
            x -= 1
        elif user_input.lower() == "south" or user_input.lower() == "b":
            self.travel = 'South'
            x += 1
        elif user_input.lower() == "west" or user_input.lower() == "c":
            self.travel = 'West'
            y -= 1
        elif user_input.lower() == "east" or user_input.lower() == "d":
            self.travel = 'East'
            y += 1

        print(f"{self.name} has moved one tile {self.travel}")
        self.position = (x, y)
        self.trail.append(self.position)
        
    def drink_grog(self):
        self.thirst = 0

pirate = Pirate()
pirate.move()