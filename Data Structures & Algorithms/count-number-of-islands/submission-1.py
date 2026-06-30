class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                count += self.dfs(r, c, grid, visited)
        
        return count
    
    def dfs(self, r, c, grid, visited):

        if r <0 or r >= len(grid):
            return 0
        if c< 0 or c >= len(grid[0]):
            return 0
        
        if (r, c) in visited:
            return 0
        
        if grid[r][c] == "0":
            return 0

        visited.add((r, c))

        self.dfs(r + 1, c, grid, visited)
        self.dfs(r - 1, c, grid, visited)
        self.dfs(r, c + 1, grid, visited)
        self.dfs(r, c - 1, grid, visited)

        return 1
        



        

        