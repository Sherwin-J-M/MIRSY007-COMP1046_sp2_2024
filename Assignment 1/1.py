grid = ['UE '] * 10 + ['W '] * 10
print(grid)
# random.shuffle(grid)
# grid = [grid[i:i+self.colu] for i in range(0, total_cells, cols)]

for i in range(0,10,5):
    grid = [grid[i:i+5]]
print(grid)