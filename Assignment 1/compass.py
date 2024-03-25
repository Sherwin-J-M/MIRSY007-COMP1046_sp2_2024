import random

class Island:
    def __init__(self, size, water_density):
        self.size = size
        self.water_density = water_density
        self.map = []

    def create_island(self):
        water_tiles = int(self.size[0] * self.size[1] * self.water_density / 100)
        self.map = [['~' for _ in range(self.size[1])] for _ in range(self.size[0])]
        for _ in range(self.size[0]):
            row = []
            for _ in range(self.size[1]):
                row.append('_')
            self.map.append(row)
                
        water_coordinates = random.sample(range(self.size[0] * self.size[1]), water_tiles)
        for index in water_coordinates:
            row = index // self.size[1]
            col = index % self.size[1]
            self.map[row][col] = 'W'

    def display_island(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j],end = ' ')
            print()


output = Island([10,20],10)
output.create_island()
output.display_island()