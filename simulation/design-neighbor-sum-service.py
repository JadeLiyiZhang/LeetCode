class neighborSum(object):

    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.value_to_position = {}
        
        for i in range(self.n):
            for j in range(self.n):
                self.value_to_position[grid[i][j]] = (i, j)

    def adjacentSum(self, value):
        if value not in self.value_to_position:
            return 0
        
        i, j = self.value_to_position[value]
        sums = 0
        
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < self.n and 0 <= y < self.n:
                sums += self.grid[x][y]
                
        return sums

    def diagonalSum(self, value):
        if value not in self.value_to_position:
            return 0
        
        i, j = self.value_to_position[value]
        sums = 0
        
        for x, y in [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
            if 0 <= x < self.n and 0 <= y < self.n:
                sums += self.grid[x][y]
                
        return sums
# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)