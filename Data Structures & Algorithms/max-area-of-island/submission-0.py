class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        max_size = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                max_size = max(self.dfs(grid, r, c, visited), max_size)
        
        return max_size
    
    def dfs(self, grid, r, c, visited):

        if r < 0 or r > len(grid) - 1:
            return 0
        
        if c < 0 or c > len(grid[0]) - 1:
            return 0

        if (r, c) in visited:
            return 0
        
        visited.add((r, c))

        if grid[r][c] == 0:
            return 0
        
        size = 1

        size += self.dfs(grid, r+1, c, visited)
        size += self.dfs(grid, r-1, c, visited)
        size += self.dfs(grid, r, c+1, visited)
        size += self.dfs(grid, r, c-1, visited)

        return size
        