import random
class Island():
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.map = []
        self.generate_map()

    def generate_map(self):
        for i in range(self.row):
            row = []
            for j in range(self.column):
                row.append(random.choice(['U', 'E', 'W']))
            self.map.append(row)

    def display_map(self):
        for row in self.map:
            print(" ".join(row))

island = Island(10,20)
island.display_map()