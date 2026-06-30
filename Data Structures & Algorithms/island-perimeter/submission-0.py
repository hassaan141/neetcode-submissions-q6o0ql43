class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        self.total = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                self.dfs(r, c, grid, visited, self.total)
        
        return self.total
    
    def dfs(self, r, c, grid, visited, total):

        if r < 0 or r >= len(grid):
            return 0
        if c < 0 or c >= len(grid[0]):
            return 0

        if (r, c) in visited:
            return 1

        if grid[r][c] == 0:
            return 0
        
        visited.add((r, c))

        curr = 0

        curr += self.dfs(r + 1, c, grid, visited, self.total)
        curr += self.dfs(r - 1, c, grid, visited, self.total)
        curr += self.dfs(r, c + 1, grid, visited, self.total)
        curr += self.dfs(r, c - 1, grid, visited, self.total)

        self.total += 4 - curr 
        print(self.total)

        return 1